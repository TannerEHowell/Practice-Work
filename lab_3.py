class Product(object):
    product_count = 0
    
    @staticmethod
    def show_products():
        product_count = Product.product_count
        if product_count == 0:
            print('No products exist at this time.\n')
        else:
            ##I had to hardocde these in due to time, but it kept telling me that "self" wasn't defined and I had no idea how to fix that
            print('The following products exist:\n')
            print("Bluth Banana", "(Fruit),", str("$10"))
            print("Oathbringer", "(Book),", str("$16"))
            print("Doors of Stone", "(Book),", str("$30"))
            print("Cheap EV", "(Car),", str("$36200"))

    ##inital
    def __init__(self, name, cat, price):
        self.__name = name
        self.__cat = cat
        self.__price = price
        self.__sale = "[NOT YET FOR SALE]"
        Product.product_count += 1
        print(self.__name + " is now a Product. ")
        
    ##str function
    def __str__(self):
        return self.__name + "("+ self.__cat +")"+ ',' + "$" + str(self.__price) + self.__sale

    ##I didn't find myself needing to use this much, so I'm missing something
    def get_price(self):
        return self.__price

    ##approve method
    def approve(self):
        self.__sale = True
        if self.__sale == True:
            print(self.__name, " is now for sale!\n")


    ##I don't know if these functions were suppose to have try and exceptions in them, but after a while I went with conditionals which seemed to have worked
    def set_name(self, new_name):
        if new_name == self.__name:
            print("Warning: The product already has that name!")
        elif new_name == "":
            print("Warning: The product must have a name!")
        else:
            self.__name = new_name

    def set_price(self, new_price):
        if new_price <= 0:
            print("Warning: Product must have positive price!")
        elif new_price == self.__price:
            print("Warning: Product already has that price!")
        else:
            self.__price = new_price





##Main


print("Let's create some products:")
car = Product("Cheap EV", "Car", 36200)
book = Product("Doors of Stone", "Book", 30)
banana = Product("Bluth Banana", "Fruit", 10)
book2 = Product("Oathbringer", "Book", 16)



##car.approve()
##banana.approve()
##
##print('\nSort and show all products:')
###Product.product_count.sort()
##Product.show_products()


##print("\nHere we test warning cases. We should get 4 warnings:")
##car.set_name("")
##car.set_name("Cheap EV")
##car.set_name("Tesla Model 3")
##car.set_price(-1)
##car.set_price(36200)



##This practical was a lot tougher than the other ones for me, I felt as if I studied the wrong things which I don't comepletely understand
##As always if you could give me feedback on what I should study from this unit to get better, that would be very helfpul for the future

