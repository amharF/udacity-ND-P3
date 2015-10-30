from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from catalog_database_setup import Base, Category, GroceryItem, User
 
engine = create_engine('sqlite:///supermarketcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Amhar Ford", email="amhar.ford@gmail.com",
             picture='https://lh5.googleusercontent.com/-fEdEA2m4s20/AAAAAAAAAAI/AAAAAAAAEXY/wJ66AgeAHLQ/photo.jpg')
session.add(User1)
session.commit()


#Category for Dairy
category1 = Category(name = "Dairy")

session.add(category1)
session.commit()

groceryItem1 = GroceryItem(name = "cheese", description = "Cheese is a food \
			derived from milk that is produced in a wide range of flavors, \
			textures, and forms by coagulation of the milk protein casein. It\
			 comprises proteins and fat from cow's milk.", price = "$3.20", 
			item_image = "http://www.automationheroes.com/wp-content/uploads/\
			2013/11/tumblr_static_cheese_205_1362800142.jpg",
			category = category1)

session.add(groceryItem1)
session.commit()

groceryItem2 = GroceryItem(name = "milk", description = "Milk is a white \
			liquid produced by the mammary glands of cows.", price = "$0.90", 
			item_image = "http://www.wainwrightdairy.com/wp-content/uploads/\
			2015/04/milk2.jpg", 
			category = category1)

session.add(groceryItem2)
session.commit()

groceryItem3 = GroceryItem(name = "yoghurt", description = "Yoghurt is a food\
			 produced by bacterial fermentation of milk. The bacteria used to\
			  make yogurt are known as \'yogurt cultures\'.", price = "$1.40",
			item_image = "http://www.womenshealthmag.com/sites/\
			womenshealthmag.com/files/images/chobani-yogurt_0.jpg",
			category = category1)

session.add(groceryItem3)
session.commit()

groceryItem4 = GroceryItem(name = "cream", description = "Cream is a dairy \
			product composed of the higher-butterfat layer skimmed from the \
			top of milk before homogenization.", price = "$1.60", 
			item_image ="http://www.coldstonecreamery.com/assets/img/products\
			/mixins/whippedcream.jpg", category = category1)

session.add(groceryItem4)
session.commit()

groceryItem5 = GroceryItem(name = "butter", description = "Butter is a solid \
			dairy product made by churning fresh or fermented cream or milk, \
			to separate the butterfat from the buttermilk.", price = "$3.20", 
			item_image = "https://upload.wikimedia.org/wikipedia/commons/f/\
			fd/Western-pack-butter.jpg", category = category1)

session.add(groceryItem5)
session.commit()


#Category for Vegetables
category2 = Category(name = "Vegetables")

session.add(category2)
session.commit()

groceryItem1 = GroceryItem(name = "potatoes", description = "The potato is a \
			starchy, tuberous crop from the perennial nightshade Solanum \
			tuberosum L. The word \'potato\' may refer either to the plant \
			itself or to the edible tuber.", price = "$3.00", item_image = "\
			https://upload.wikimedia.org/wikipedia/commons/a/ab/Patates.jpg",
			category = category2)

session.add(groceryItem1)
session.commit()

groceryItem2 = GroceryItem(name = "carrots", description = "The carrot is a \
			root vegetable, usually orange in colour, though purple, red, \
			white, and yellow varieties exist. It has a crisp texture when \
			fresh.", price = "$1.80", item_image = "http://media.mercola.com/\
			assets/images/food-facts/carrot-fb.jpg", category = category2)

session.add(groceryItem2)
session.commit()

groceryItem3 = GroceryItem(name = "lettuce", description = "Lettuce is an \
			annual plant of the daisy family Asteraceae. It is most often \
			grown as a leaf vegetable, but sometimes for its stem and seeds.",
			price = "$0.80", item_image = "http://16acresgardencenter.com/\
			wp-content/uploads/2014/06/Lettuce.jpg",
			category = category2)

session.add(groceryItem3)
session.commit()

groceryItem4 = GroceryItem(name = "cucumber", description = "Cucumber is a \
			widely cultivated plant in the gourd family, Cucurbitaceae. \
			It is a creeping vine that bears cylindrical fruits that are used\
			 as culinary vegetables.", price = "$0.90", item_image ="http://\
			i.livescience.com/images/i/000/076/219/iFF/cucumbers.jpg",
			category = category2)

session.add(groceryItem4)
session.commit()

groceryItem5 = GroceryItem(name = "onions", description = "The onion, also \
			known as the bulb onion or common onion, is a vegetable and is \
			the most widely cultivated species of the genus Allium.", 
			price = "$3.20", item_image = "https://upload.wikimedia.org/\
			wikipedia/commons/f/fd/Western-pack-butter.jpg",
			category = category1)

session.add(groceryItem5)
session.commit()


#Category for Fruit
category3 = Category(name = "Fruit")

session.add(category3)
session.commit()

groceryItem1 = GroceryItem(name = "apples", description = "The apple tree is \
			a deciduous tree in the rose family best known for its sweet, \
			pomaceous fruit, the apple. It is cultivated worldwide as a fruit\
			 tree, and is the most widely grown species in the genus Malus.", 
			price = "$3.10", item_image = "http://media.mercola.com/assets/\
			images/food-facts/apple.jpg", category = category3)

session.add(groceryItem1)
session.commit()

groceryItem2 = GroceryItem(name = "bananas", description = "The banana is an \
			edible fruit, botanically a berry, produced by several kinds of \
			large herbaceous flowering plants in the genus Musa. In some \
			countries, bananas used for cooking may be called plantains.",
			price = "$1.60", item_image = "https://www.organicfacts.net/\
			wp-content/uploads/2013/05/Banana21.jpg", category = category3)

session.add(groceryItem2)
session.commit()

groceryItem3 = GroceryItem(name = "oranges", description = "The orange is the\
			 fruit of the citrus species Citrus x sinensis in the family \
			Rutaceae. The fruit of the Citrus x sinensis is considered a swee\
			t orange, whereas the fruit of the Citrus x aurantium is consider\
			ed a bitter orange.", price = "$2.60", item_image = "https://uplo\
			ad.wikimedia.org/wikipedia/commons/7/7b/Orange-Whole-&-Split.jpg",
			category = category3)

session.add(groceryItem3)
session.commit()

groceryItem4 = GroceryItem(name = "lemons", description = "The lemon is a \
			species of small evergreen tree native to Asia. The tree's \
			ellipsoidal yellow fruit is used for culinary and non-culinary \
			purposes throughout the world, primarily for its juice, which has\
			 both culinary and cleaning uses.", price = "$1.70", item_image =
			"https://upload.wikimedia.org/wikipedia/commons/c/c7/Lemon-Whole-\
			Split.jpg", category = category3)

session.add(groceryItem4)
session.commit()

groceryItem5 = GroceryItem(name = "pears", description = "The pear is any of \
			several tree and shrub species of genus Pyrus in the family Rosac\
			eae. It is also the name of the pomaceous fruit of these trees.", 
			price = "$2.40", item_image = "http://images2.wikia.nocookie.net/\
			__cb20110210142733/recipes/images/d/db/Packham_pear.jpg", 
			category = category3)

session.add(groceryItem5)
session.commit()


#Category for Meat
category4 = Category(name = "Meat")

session.add(category4)
session.commit()

groceryItem1 = GroceryItem(name = "pork chops", description = "A pork chop is\
			 a chop of pork cut perpendicularly to the spine of the pig and \
			usually containing a rib or part of a vertebra, served as an \
			individual portion.", price = "$3.80", item_image = "https://www.\
			hiddenvalley.com/cache/0f1bb4c47aabfa3e5c306bddd2a2f5f1.jpg", 
			category = category4)

session.add(groceryItem1)
session.commit()

groceryItem2 = GroceryItem(name = "lamb chops", description = "A lamb chop is\
			 a cut of meat from a lamb,cut perpendicularly to the spine, and \
			usually containing a rib or riblet part of a vertebra and served \
			as an individual portion.", price = "$5.60", item_image = "http:\
			//blog.sanuraweathers.com/wp-content/uploads/2012/03/LambChops_61\
			51.jpg", category = category4)

session.add(groceryItem2)
session.commit()

groceryItem3 = GroceryItem(name = "beef steak", description = "A steak is a \
			meat generally sliced perpendicular to the muscle fibers, \
			potentially including a bone.", price = "$6.70", item_image = 
			"http://ubons.net/wp-content/uploads/2012/01/Beef-steak.jpg",
			category = category4)

session.add(groceryItem3)
session.commit()

groceryItem4 = GroceryItem(name = "whole chicken", description = "The chicken\
			 is a domesticated fowl, a subspecies of the red junglefowl. As o\
			 ne of the most common and widespread domestic animals, with a \
			population of more than 24 billion in 2003,[1] there are more \
			chickens in the world than any other species of bird. Humans keep\
			 chickens primarily as a source of food, consuming both their mea\
			 t and their eggs.", price = "$8.90", item_image = "http://www.th\
			 ebutchersblocksc.com/chicken_001.jpg", category = category4)

session.add(groceryItem4)
session.commit()

groceryItem5 = GroceryItem(name = "beef burgers", description = "A patty, in \
			American, Canadian, South African, Australian and New Zealand \
			English, is a flattened, usually round, serving of ground beef. \
			The meat is compacted and shaped, cooked, and served.", price = 
			"$2.50", item_image = "https://upload.wikimedia.org/wikipedia/\
			commons/d/d2/Pre-formed_hamburger.JPG", category = category4)

session.add(groceryItem5)
session.commit()

#Category for Bakery
category5 = Category(name = "Bakery")

session.add(category5)
session.commit()

groceryItem1 = GroceryItem(name = "wholemeal bread", description = "Whole-\
			wheat bread or wholemeal bread is a type of bread made using \
			flour that is partly or entirely milled from whole or almost-\
			whole wheat grains, see whole-wheat flour and whole grain. It is \
			one kind of brown bread.", price = "$2.40", item_image = "https:/\
			/upload.wikimedia.org/wikipedia/commons/4/46/Vegan_no-knead_whole\
			_wheat_bread_loaf,_September_2010.jpg", category = category5)

session.add(groceryItem1)
session.commit()

groceryItem2 = GroceryItem(name = "corn bread", description = "Cornbread is a\
			 generic name for any number of quick breads containing cornmeal.\
			  They are usually leavened by baking powder.", price = "$2.20", 
			item_image = "http://wickedgoodkitchen.com/wp-content/uploads/\
			2013/11/Grandmas-Sweet-Buttermilk-Cornbread-4.jpg", 
			category = category5)

session.add(groceryItem2)
session.commit()

groceryItem3 = GroceryItem(name = "white bread", description = "White bread \
			typically refers to breads made from wheat flour from which the \
			bran and the germ layers have been removed from the whole \
			wheatberry as part of the flour grinding or milling process, \
			producing a light-colored flour.", price = "$1.80", item_image = 
			"https://thenypost.files.wordpress.com/2014/05/whitebread.jpg",
			category = category5)

session.add(groceryItem3)
session.commit()

groceryItem4 = GroceryItem(name = "hot cross bun", description = "A hot cross\
			 bun is a spiced sweet bun made with currants or raisins and mark\
			 ed with a cross on the top, traditionally eaten on Good Friday \
			 in the United Kingdom, Ireland, Australia, New Zealand, South Afr\
			 ica, Canada, India, and United States, and now available all year \
			 round in some places.", price = "$2.00", item_image = "https://\
			 foodimentaryguy.files.wordpress.com/2011/09/www-chatmagazine-co-\
			 uk.jpg", category = category5)

session.add(groceryItem4)
session.commit()

groceryItem5 = GroceryItem(name = "croissant", description = "A croissant is \
			a buttery, flaky, viennoiserie or Vienna-style pastry named for \
			its well-known crescent shape. Croissants and other viennoiserie \
			are made of a layered yeast-leavened dough.", price = "$1.00", 
 			item_image = "http://www.creationfood.ca/wp-content/uploads/2015/\
 			02/croissants-korea-AFPrelax-151113.jpg", category = category5)

session.add(groceryItem5)
session.commit()

#Category for Beverages
category6 = Category(name = "Beverages")

session.add(category6)
session.commit()

groceryItem1 = GroceryItem(name = "coffee", description = "Coffee is a brewed\
			 drink prepared from roasted coffee beans, which are the seeds of\
			  berries from the Coffea plant.", price = "$2.60", item_image = 
			"http://images.wisegeek.com/cup-of-coffee-with-creamer-and-coffee\
			-beans.jpg", category = category6)

session.add(groceryItem1)
session.commit()

groceryItem2 = GroceryItem(name = "apple juice", description = "Apple juice i\
			s a fruit juice made by the maceration and pressing of apples.", 
			 price = "$1.40", item_image = "https://upload.wikimedia.org/wiki\
			 pedia/commons/2/23/Apple_juice_with_3apples.jpg", 
			 category = category6)

session.add(groceryItem2)
session.commit()

groceryItem3 = GroceryItem(name = "tea", description = "Tea is an aromatic be\
			verage commonly prepared by pouring hot or boiling water over cur\
			ed leaves of the Camellia sinensis, an evergreen shrub native to \
			Asia. After water, it is the most widely consumed drink in the wo\
			rld.", price = "$1.40", item_image = "http://weknowyourdreams.com\
			/image.php?pic=/images/tea/tea-07.jpg", category = category6)

session.add(groceryItem3)
session.commit()

groceryItem4 = GroceryItem(name = "orange juice", description = "Orange juice\
			 is the liquid extract of the fruit of the orange tree. It is mad\
			 e by squeezing the fresh orange, drying and later re-hydrating t\
			 he juice, or concentration of the juice and later adding water t\
			 o the concentrate.", price = "$1.60", item_image = "http://autho\
			 ritynutrition.com/wp-content/uploads/2013/10/orange-juice.jpg", 
			category = category6)

session.add(groceryItem4)
session.commit()

groceryItem5 = GroceryItem(name = "cola", description = "Cola is a sweetened,\
			 carbonated soft drink, derived from drinks that originally conta\
			 ined caffeine from the kola nut and cocaine from coca leaves, fl\
			 avored with vanilla and other ingredients.", price = "$1.80", 
			 item_image = "http://www.wellbeing.com.au/uploads/news/Cola.jpg"
			 , category = category6)

session.add(groceryItem5)
session.commit()



print "added grocery items!"

