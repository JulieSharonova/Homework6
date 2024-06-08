print(my_dict)
print(my_dict['Anastasia'])
print(my_dict.get('Masha'))
my_dict.update({'Misha': 2001,
                'Vova': 1985})
print(my_dict)
a = my_dict.pop('Misha')
print(my_dict)
print(a)

my_set = {1, 1, 3.5, 3.7, 3.5, False, False}
print(set(my_set))
my_set.update({5, 9})
print(my_set)
my_set.discard(False)
print(my_set)