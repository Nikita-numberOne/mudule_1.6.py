my_dict = { "Nikita" : 2004, "Alexandra" : 2006 }
print(my_dict)
print( my_dict ["Nikita"])
my_dict["Alex"] = 2003
print(my_dict["Alex"])
my_dict. update({'Tom': 1999,
                 'Mia': 2001})
print(my_dict)
a = my_dict.pop('Alexandra')
print(a)
print(my_dict)
# Работа с множеством
my_set = {1, 2, 3, 4, 5, 1, 2, 3, "Set", "String", "Dog", "Set", True }
print(my_set)
list_ = [19, 29, 99, 19, 29, 777]
list_ = set(list_)
print(list_.add(55))
print(list_)
print(list_.add(1703))
print(list_)
print(list_.discard(99))
print(list_)

