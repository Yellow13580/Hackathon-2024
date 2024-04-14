
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver
grocery_items = [
    # Fresh Produce
    'Apples', 'Bananas', 'Oranges', 'Lemons', 'Limes', 'Pineapple', 'Watermelon', 'Strawberries', 'Blueberries', 'Raspberries',
    'Blackberries', 'Grapes', 'Watermelon', 'Cantaloupe', 'Honeydew Melon', 'Peaches', 'Nectarines', 'Plums', 'Kiwi', 'Mangoes',
    'Papayas', 'Pears', 'Avocados', 'Tomatoes', 'Lettuce', 'Spinach', 'Broccoli', 'Carrots', 'Potatoes', 'Onions', 'Celery',
    'Cucumbers', 'Bell Peppers', 'Garlic', 'Ginger', 'Mushrooms', 'Zucchini', 'Corn', 'Green Beans', 'Asparagus', 'Eggplant',
    'Artichokes', 'Cabbage', 'Cauliflower', 'Sweet Potatoes', 'Radishes', 'Brussels Sprouts', 'Beets', 'Romaine Lettuce', 'Arugula',
    'Kale', 'Collard Greens', 'Turnips', 'Fennel', 'Scallions', 'Parsley', 'Cilantro', 'Basil', 'Thyme', 'Rosemary', 'Mint',

    # Dairy and Eggs
    'Milk', 'Eggs', 'Butter', 'Yogurt', 'Cheese', 'Cream Cheese', 'Sour Cream', 'Half and Half', 'Whipping Cream', 'Cottage Cheese',
    'Heavy Cream', 'Ricotta Cheese', 'Goat Cheese', 'Feta Cheese', 'Mozzarella Cheese', 'Cheddar Cheese', 'Parmesan Cheese', 'Almond Milk',
    'Soy Milk', 'Coconut Milk', 'Oat Milk', 'Rice Milk', 'Creamer', 'Whipped Topping',

    # Meat and Seafood
    'Ground Beef', 'Chicken Breasts', 'Pork Chops', 'Bacon', 'Salmon Fillets', 'Tilapia Fillets', 'Shrimp', 'Ground Turkey', 'Turkey Breast',
    'Canned Tuna', 'Canned Salmon', 'Frozen Shrimp', 'Beef Jerky', 'Deli Ham', 'Deli Turkey', 'Lunch Meat', 'Hot Dogs', 'Sausages', 'Fish Sticks',
    'Frozen Chicken Nuggets', 'Frozen Burgers', 'Frozen Pizza', 'Frozen Vegetables', 'Frozen Fruits',

    # Bakery
    'Bread', 'Bagels', 'English Muffins', 'Hamburger Buns', 'Hot Dog Buns', 'Dinner Rolls', 'Tortillas', 'Pita Bread', 'Croissants',
    'Pastries', 'Donuts', 'Muffins', 'Cookies', 'Brownies', 'Cupcakes', 'Cake', 'Pie', 'Baklava', 'Cinnamon Rolls', 'Scones', 'Biscuits',
    'Crackers', 'Chips', 'Granola Bars', 'Cereal', 'Oatmeal', 'Pancake Mix', 'Waffle Mix', 'Flour', 'Sugar', 'Baking Powder', 'Baking Soda',
    'Vanilla Extract', 'Chocolate Chips', 'Cocoa Powder', 'Honey', 'Maple Syrup', 'Pancake Syrup', 'Jam', 'Peanut Butter', 'Almond Butter',
    'Nutella', 'Marshmallows', 'Graham Crackers', 'Cake Mix', 'Brownie Mix', 'Cookie Mix', 'Pie Crust', 'Whipped Cream',

    # Beverages
    'Water', 'Soda', 'Juice', 'Tea', 'Coffee', 'Sports Drinks', 'Energy Drinks', 'Milk Alternatives', 'Kombucha', 'Lemonade', 'Iced Tea',
    'Powdered Drink Mix', 'Alcohol',

    # Snacks
    'Chips', 'Popcorn', 'Pretzels', 'Crackers', 'Nuts', 'Trail Mix', 'Beef Jerky', 'Granola', 'Dried Fruit', 'Cereal Bars', 'Fruit Snacks',
    'Rice Cakes', 'Pudding Cups', 'Applesauce Cups', 'Yogurt Cups', 'Cheese Crackers', 'Granola Bars', 'Chocolate Bars', 'Candy', 'Gum',

    # Pantry Staples
    'Rice', 'Pasta', 'Beans', 'Canned Tomatoes', 'Canned Soup', 'Broth', 'Canned Vegetables', 'Canned Beans', 'Canned Fruit', 'Peanut Butter',
    'Jelly', 'Syrup', 'Honey', 'Flour', 'Sugar', 'Salt', 'Pepper', 'Spices', 'Olive Oil', 'Vegetable Oil', 'Vinegar', 'Soy Sauce', 'Teriyaki Sauce',
    'Hot Sauce', 'BBQ Sauce', 'Ketchup', 'Mustard', 'Mayonnaise', 'Salad Dressing', 'Cereal', 'Oatmeal', 'Pancake Mix', 'Baking Mixes',
    'Bread Crumbs', 'Cake Mix', 'Brownie Mix', 'Cookies']

with open("Output.txt", "w") as text_file:
    def targetFetch():
        text_file.write("Target:")
    # instantiate options
        options = webdriver.ChromeOptions()
#ask user what they would like to search
        #query = input("what would you like from Target? ")
 # run browser in headless mode
        options.headless = True

# instantiate driver
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)

# load website
        url = 'https://www.target.com/s?searchTerm=' + k

# get the entire website content
        driver.get(url)
        time.sleep(3)
# initialize array containing product info
        product = []
#loop four times for first four products
        for i in range(1, 5):
                text_file.write("INSERT INTO ITEM VALUES (")
# grab name of product
                elements = driver.find_elements(By.XPATH, "//div/div[1]/div/div[4]/div/div/section/div/div[" + str(i) + "]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/a")
                product_info = [element.text for element in elements]
                product.append(product_info)
                text_file.write(str(product_info))
#grab product price
                elements = driver.find_elements(By.XPATH, "//div/div[1]/div/div[4]/div/div/section/div/div[" + str(i) + "]/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/span[1]/span")
                product_info = [element.text for element in elements]
                product.append(product_info)
                text_file.write(str(product_info))
#grab product price per metric
                elements = driver.find_elements(By.XPATH, "//div/div[1]/div/div[4]/div/div/section/div/div[" + str(i) + "]/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/span[2]")
                product_info = [element.text for element in elements]
                product.append(product_info)
                text_file.write(str(product_info))
                print("INSERT INTO ITEM VALUES("+str(product)+");")
                product.clear()
                text_file.write(");\n")
    def walmartFetch():
        text_file.write("Walmart:")
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
    # instantiate options
        options = webdriver.ChromeOptions()
    # ask user what they would like to search
        #query = input("what would you like from Walmart? ")
    # run browser in headless mode
        options.headless = True

    # instantiate driver
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver = undetected_chromedriver.Chrome()
    # load website
        url = 'https://www.walmart.com/search?q=' + k

    # get the entire website content
        driver.get(url)
        time.sleep(1)
    # initialize array containing product info
        product = []
    # loop four times for the first four products
        for i in range(1, 5):
    #grab product title
            elements = driver.find_elements(By.XPATH, "//section/div/div[" + str(i) + "]/div/div/div/div[2]/span/span")
            product_info = [element.text for element in elements]
            product.append(product_info)
            text_file.write(str(product_info))
    #grab product price
            elements = driver.find_elements(By.XPATH, "//section/div/div[" + str(i) + "]/div/div/div/div[2]/div[1]/div[1]")
            product_info = [element.text for element in elements]
            product.append(product_info)
            text_file.write(str(product_info))
    #grab product price per metric
            elements = driver.find_elements(By.XPATH, "//section/div/div[" + str(i) + "]/div/div/div/div[2]/div[1]/div[2]")
            product_info = [element.text for element in elements]
            product.append(product_info)
            text_file.write(str(product_info))
            print(product)
            product.clear()
            text_file.write("\n")
    for k in grocery_items:
        targetFetch()