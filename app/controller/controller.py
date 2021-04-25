
from app.view.view import View
from app.utils.database import Database
from app.utils.requester import Requester
from app.models.category import Category
from app.models.product import Product
from app.models.substitute import Substitute
from app.scripts_MySQL.tables import tables_queries


class Controller:
    def __init__(self):
        self.view = View()
        self.db = Database()
        self.req = Requester()

    # ----- Greetings -----
    def welcome(self):
        self.view.welcome()

    def goodbye(self):
        self.view.goodbye()

    # ----- DB menu -----
    def creation_db(self):
        self.db.drop_db()
        self.db.create_db()
        self.db.create_tables(tables_queries)
        self.req.get_data()

    def db_management_menu_process(self):
        choices = ["1", "2", "q"]
        loop = True
        while loop:
            choice = self.view.db_management_menu()
            if choice not in choices:
                self.view.choice_error()
            else:
                if choice == "1":
                    pass
                elif choice == "2":
                    self.creation_db()
                elif choice == "q":
                    self.goodbye()
                loop = False
        self.view.split()

    # ----- Find or display substitutes -----
    def find_or_display_substitute_menu(self):
        return self.view.find_or_display_substitute_menu()

    def choose_category_process(self):
        categories = Category.objects.all()
        loop = True
        choices = [num+1 for num in range(len(categories))]
        while loop:
            choice = self.view.show_categories(categories)
            if int(choice) not in choices:
                self.view.choice_error()
            else:
                loop = False
                self.view.split()
                return categories[int(choice) - 1]

    def choose_product_process(self, category):
        products = Product.objects.filter(category__name = category.name)
        loop = True
        choices = [num+1 for num in range(len(products))]
        while loop:
            choice = self.view.show_products(products)
            if int(choice) not in choices:
                self.view.choice_error()
            else:
                loop = False
                self.view.split()
                return products[int(choice) - 1]

    def choose_better_product_process(self, product, category):
        better_prod = ""
        if product.nutrition_grade == "a":
            self.view.best_nutrition_grade()
            better_products = Product.objects.filter(nutrition_grade = product.nutrition_grade, category__name = category.name)
            if len(better_products) <= 1:
                self.view.no_other_nutrition_grade_a()
            else:
                for better_prod in better_products:
                    if better_prod.name == product.name: better_products.remove(better_prod)
                choice = self.view.other_nutrition_grade_a(better_products)
                better_prod = better_products[int(choice) - 1]
                self.view.split()
        else:
            better_products = Product.objects.filter(nutrition_grade__lt = product.nutrition_grade, category__name = category.name)
            if len(better_products) == 0:
                self.view.no_better_nutrition_grade()
            else:
                self.view.show_product(product)
                better_products = Product.objects.filter(nutrition_grade__lt = product.nutrition_grade, category__name = category.name)
                choice = self.view.show_better_products(better_products)
                better_prod = better_products[int(choice) - 1]
                self.view.split()
        return better_prod

    def save_substitute_process(self, category, product, better_prod):
        self.view.url_substitute(category, product, better_prod)
        self.view.show_product(better_prod)
        self.view.save_substitute_menu()
        choice = self.view.prompt_choice()
        self.view.split()
        if choice == "1":
            sub = Substitute(product=product.id,substitute=substitute.id)
            try:
                Substitute.objects.save(sub)
                self.view.save_done(sub)
                self.view.split()
            except:
                self.view.save_fail(sub)
                self.view.split()
        elif choice == "2":
            pass
        else:
            self.view.choice_error()


    def find_or_display_substitute_process(self):
        choices = ["1", "2", "q"]
        loop = True
        while loop:
            choice = self.find_or_display_substitute_menu()
            if choice not in choices:
                self.view.choice_error()
            else:
                if choice == "1": # find a substitute
                    # display categories
                    category = self.choose_category_process()
                    # display choosen category
                    self.view.url_category(category=category)
                    # display products
                    product = self.choose_product_process(category=category)
                    # display choosen product
                    self.view.url_product(category=category,product= product)
                    # display better products
                    better_product = self.choose_better_product_process(product=product, category=category)
                    if better_product != "":
                        # save better product as substitute
                        self.save_substitute_process(category=category,product=product,better_prod=better_product)
                elif choice == "2":
                    # display saved substitutes
                    pass
                elif choice == "q":
                    self.goodbye()
                loop = False
        self.view.split()


    # def find_substitute_process(self):
    #     # Display all categories:
    #     categories = Category.objects.all()
    #     self.view.choose_category()
    #     self.view.show_enumerate_list(categories)
    #     choice = self.view.prompt_choice()
    #     category = categories[int(choice) - 1]
    #     self.view.split()
    #     # Display all products in the choosen category:
    #     self.view.url_category(category)
    #     products = Product.objects.filter(category__name = category.name)
    #     self.view.choose_product()
    #     self.view.show_enumerate_list(products)
    #     choice = self.view.prompt_choice()
    #     product = products[int(choice) - 1]
    #     self.view.split()
    #     # Display the choosen product:
    #     self.view.url_product(category, product)

