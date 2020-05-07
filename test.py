
from requester import Requester
from settings import CATEGORIES
from models.product import Product
from models.category import Category

req = Requester()

for category in CATEGORIES:
    json_data = req.url_to_json(category) # store json from category url
    pages_nb = req.retrieve_cat_pages_nb(json_data) # store the number of pages the category

    for page in range(pages_nb+1):
        json_data = req.page_to_json(category, page) # store the current page of the category
        products = json_data["products"] # store the products of the current page
        
        for p in products:
            try:
                product = Product(name=p['product_name'], brand=p['brands'], nutrition_grade=p['nutrition_grades'], stores=p['stores'], url=p['url'], categories=p['categories'])
                product.save()
                for category in product.categories_list:
                    try:
                        category.save()
                    except:
                        continue
            except:
                continue

