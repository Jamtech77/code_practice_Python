#Inheritance繼承chef
from chef import Chef
class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The chinese chef makes fried rice.")

    def make_special_dish(self):
        print("The chinese chef makes ramen.")
