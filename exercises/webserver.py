from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

"""import CRUD operations from SQLalchemy"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

"""connect to database and create session"""

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


"""indicates what code to execute based on the type of HTTP request
that is sent to the server"""

class webServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:

			"""homepage listing all the restaurants"""

			if self.path.endswith("/restaurants"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				restaurants = session.query(Restaurant).all()
				output = ""
				output += "<html><body>"
				output += "<h1><a href = '/restaurants/new'> Make a New \
							Restaurant Here</a></h1>"
				for entry in restaurants:
					output += entry.name
					output += "</br>"

					"""provide option to edit restaurant"""

					output += "<a href ='/restaurants/%d/edit'> edit</a> " % entry.id
					output += "</br>"

					"""provide option to delete restaurant"""

					output += "<a href ='/restaurants/%d/delete'> delete</a>" % entry.id
					output += "</br></br></br>"
			
				output += "</body></html>"

				self.wfile.write(output)
				print output
				return

			"""page to add a new restaurant"""	

			if self.path.endswith("restaurants/new"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<html><body>"

				"""form to enter new restaurant name"""

				output += "<form method='POST' enctype='multipart/form-data'\
					action='/restaurants/new'><h2>Make a new restaurant</h2><input name=\
					'newRestaurantName' type='text' placeholder='New Restaurant Name'>\
					<input type='submit' value='Create'></form>"
				output += "</body></html>"

				self.wfile.write(output)
				print output
				return

			"""page to edit restaurant"""

			if self.path.endswith("/edit"):
				restaurantIDpath = self.path.split("/")[2]
				restaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDpath).one()
				if restaurantQuery != []:
					self.send_response(200)
					self.send_header('Content-type', 'text/html')
					self.end_headers()
					output = ""
					output += "<html><body>"
				

					"""form to enter edited name of restaurant"""

					output += "<form method='POST' enctype='multipart/form-data'\
						action='restaurant/%s/edit'>" % restaurantIDpath
					output += "<h2> Enter new name for %s:</h2>" % restaurantQuery.name
					output += "<input name='editedRestaurantName' type='text'\
				 		placeholder='Change %s'>" % restaurantQuery.name
					output += "<input type='submit' value='Rename'></form>"
					output += "</body></html>"

					self.wfile.write(output)
					print output
					return
			
			"""page to delete restaurant"""

			if self.path.endswith("/delete"):
				restaurantIDpath = self.path.split("/")[2]
				restaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDpath).one()
				if restaurantQuery != []:
					self.send_response(200)
					self.send_header('Content-type', 'text/html')
					self.end_headers()
					output = ""
					output += "<html><body>"
					
					"""button to delete restaurant"""
					output += "<form method='POST' enctype='multipart/form-data'\
						action='restaurant/%s/delete'>" % restaurantIDpath	
					output += "<h2> Are you sure you want to delete %s?</h2>" % restaurantQuery.name
					output += "<input name='deleteRestaurant' type='submit' value='Delete'></form>"
					output += "</body></html>"

					self.wfile.write(output)
					print output
					return


		except IOError:
			self.send_error(404, 'File Not Found %s' % self.path)

	def do_POST(self):
		try:

			"""update database with new restaurant name"""

			if self.path.endswith("/restaurants/new"):
				ctype, pdict = cgi.parse_header(
					self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('newRestaurantName')

					"""use Restaurant class to create new entry"""

					newRestaurant = Restaurant(name = messagecontent[0])
					session.add(newRestaurant)
					session.commit()

					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurants') #send browser back to homepage
					self.end_headers()

			"""update database with edited restaurant name"""

			if self.path.endswith("/edit"):
				ctype, pdict = cgi.parse_header(
					self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('editedRestaurantName')

					restaurantIDpath = self.path.split("/")[2]
					restaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDpath).one()

				if restaurantQuery != []:
					restaurantQuery.name = messagecontent[0]
					session.add(restaurantQuery)
					session.commit()

					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurants') #send browser back to homepage
					self.end_headers()

			"""delete restaurant from database"""

			if self.path.endswith("/delete"):
				ctype, pdict = cgi.parse_header(
					self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('deleteRestaurant')

					restaurantIDpath = self.path.split("/")[2]
					restaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDpath).one()

				if restaurantQuery != []:
					session.delete(restaurantQuery)
					session.commit()

					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurants') #send browser back to homepage
					self.end_headers()
			
			"""
			self.send_response(301)
			self.end_headers()

			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				fields = cgi.parse_multipart(self.rfile, pdict)
				messagecontent = fields.get('message')

			output = ""
			output += "<html><body>"
			output += "<h2> Okay, new restaurant created: </h2>"
			output += "<h1> %s </h1>" % messagecontent[0]
			output += "</body></html>"
			self.wfile.write(output)
			print output"""

		except:
			pass


"""instantiate server and specify what port it will listen on"""

def main():
	try: 
		port = 8080
		server = HTTPServer(('',port), webServerHandler)
		print "Web server running on port %s" % port
		server.serve_forever()

	except KeyboardInterrupt:
		print "^C entered, stopping web server..."
		server.socket.close()

if __name__ == '__main__':
	main()