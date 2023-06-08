import tkinter


class restaurant:
    restaurant_rating = 0

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("ресторан открыт")

    def rating(self):
        print("Текущий рейтинг (0-10):", self.restaurant_rating)
        self.restaurant_rating = int(input("Введите рейтинг: "))
        if self.restaurant_rating > 10:
            self.restaurant_rating = 10
        if self.restaurant_rating < 0:
            self.restaurant_rating = 0
        print("Обновленный рейтинг (0-10):", self.restaurant_rating)


class iceCream(restaurant):

    def __init__(self, name, type):
        super().__init__(name, type)

    flavors = ["Шоколадное", "Ваниль", "Ягодное"]
    place = "Полевая Сабировская д.45"
    time = ["10:00", "20:00"]
    types = ["мороженое на палочке", "мягкое мороженое", "мороженное в стаканчик"]

    def flavors_show(self):
        print(*self.flavors)

    def flavors_add(self):
        self.flavors.append(input("Добавить вкус: "))

    def flavors_remove(self, x):
        if x in self.flavors:
            self.flavors.remove(x)

    def flavors_avaible(self):
        x = input("поиск вкуса: ")
        if x in self.flavors:
            print("Avaible")
        else:
            print("unavaible")

    def types_show(self):
        print(*self.types)

    def zakaz(self, type, flavor):
        if type in self.types and flavor in self.flavors:
            print(f"Вы заказали {type} со вкусом {flavor}")
        else:
            print("к сожалениюна данный момент  такого мороженного нет в меню")


icer = iceCream("Мороженко", "мороженка")

icer.flavors_show()
icer.describe_restaurant()
print(icer.time)
icer.flavors_add()
icer.flavors.remove("Ягодное")
icer.flavors_show()
icer.flavors_avaible()
icer.zakaz(input("Вид мороженного: "),input(": "))



import tkinter as tk


class IceCream:
    def __init__(self, flavors):
        self.flavors = flavors

    def has_flavor(self, flavor):
        """
        Проверяет, есть ли определенный сорт мороженого в списке flavors.

        :param flavor: проверяемый сорт мороженого
        :return: True, если сорт мороженого есть в списке, False в противном случае
        """
        return flavor in self.flavors


class IceCreamStand:
    def __init__(self, flavors):
        self.ice_cream = IceCream(flavors)
        self.orders = []

    def add_order(self, order):
        """
        Добавляет заказ в список заказов.

        :param order: заказ, который нужно добавить
        """
        self.orders.append(order)

    def get_available_flavors(self):
        """
        Возвращает строку со списком доступных сортов мороженого.

        :return: список доступных сортов мороженого
        """
        return ', '.join(self.ice_cream.flavors)


class IceCreamGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Кафе мороженого")

        # создаем объект IceCreamStand с сортами мороженого
        self.ice_cream_stand = IceCreamStand(['ванильное', 'шоколадное', 'клубничное', 'ягодное', 'банановое'])

        # создаем виджеты для отображения списка доступных сортов и добавления заказов
        self.available_flavors_label = tk.Label(self.master, text="Доступные сорта: %s" % self.ice_cream_stand.get_available_flavors())
        self.available_flavors_label.pack(pady=10)

        self.order_frame = tk.Frame(self.master)
        self.order_frame.pack(pady=10)

        self.new_order_button = tk.Button(self.order_frame, text="+", width=5, command=self.add_order)
        self.new_order_button.pack(side=tk.LEFT)

        self.orders_listbox = tk.Listbox(self.order_frame, width=30)
        self.orders_listbox.pack(side=tk.LEFT)

        self.delete_order_button = tk.Button(self.order_frame, text="-", width=5, command=self.delete_order)
        self.delete_order_button.pack(side=tk.LEFT)

        # добавляем тестовые заказы для демонстрации
        self.ice_cream_stand.add_order("Ванильное")
        self.ice_cream_stand.add_order("Клубничное")

        # отображаем список заказов
        for order in self.ice_cream_stand.orders:
            self.orders_listbox.insert(tk.END, order)

    def add_order(self):
        """
        Добавляет новый заказ в список заказов и обновляет виджет ListBox.
        """
        flavor = tk.simpledialog.askstring("Добавить заказ", "Введите сорт мороженого:")
        if flavor and self.ice_cream_stand.ice_cream.has_flavor(flavor.lower()):
            self.ice_cream_stand.add_order(flavor.capitalize())
            self.orders_listbox.insert(tk.END, flavor.capitalize())

    def delete_order(self):
        """
        Удаляет выбранный заказ из списка заказов и обновляет виджет ListBox.
        """
        selection = self.orders_listbox.curselection()
        if selection:
            self.orders_listbox.delete(selection)
            self.ice_cream_stand.orders.pop(selection[0])


root = tk.Tk()
gui = IceCreamGUI(root)
root.mainloop()