#function that allows for input
# def greet_with_name(name):
#     print(f'Hello {name}')
#     print(f'How do you do {name}?')

# greet_with_name('solomon')

#functions with more than 1 inputs
def greet_with(name, location):
    print(f'Hello {name}, what is it like in {location}?')

greet_with('Medhanie', 'Eritrea')
greet_with('Solomon', 'Australia')
greet_with('Minnie', 'Disney Land')

#function with keyword arguments
greet_with(name = 'Bookie', location = 'Mars')