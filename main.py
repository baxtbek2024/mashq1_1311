class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_info(self):
        return f"Mahsulot: {self.__name}, Narx: {self.__price} so'm, Zaxira: {self.__stock} dona"

    def purchase(self, quantity):
        if self.__stock <= 0:
            print(f"{self.__name} - sotuvda yo‘q.")
        elif quantity > self.__stock:
            print(f"Yetarli miqdor yo‘q! Hozirda faqat {self.__stock} dona bor.")
        else:
            self.__stock -= quantity
            print(f"{quantity} dona {self.__name} sotib olindi. Qolgan zaxira: {self.__stock} dona.")
            if self.__stock == 0:
                print(f"{self.__name} - sotuvda yo‘q endi.")

    def _set_stock(self, new_stock):
        self.__stock = new_stock


class InventoryManager:
    def update_stock(self, product, new_stock):
        product._set_stock(new_stock)
        print(f"{product._Product__name} zaxirasi {new_stock} dona qilib yangilandi.")


product1 = Product("Telefon", 2500000, 5)
print(product1.get_info())
product1.purchase(2)
product1.purchase(3)
product1.purchase(1)
manager = InventoryManager()
manager.update_stock(product1, 10)
print(product1.get_info())
