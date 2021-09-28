lst_days = ['mon', 'tue', 'wed', 'thu']
tup_days = ('mon', 'tue')
dict_t = {
    'name': 'tae-hoon',
    'age': 34,
    'korean': True,
    'fav_foods': ['kimchi', 
    'Sashimi']

}

age = "18"

# int_age = int(age)
# print(int_age)
# print(type(int_age))

def my_function(who):
    print('Hello! ', who)

# my_function('Taehoon')

def plus(a, b=0):
    c = a + b

    return c

# print(plus(1))

def plus(a=0, b=0):
    c = a + b

    return c

# print(plus(1, 7))
# print(plus())



