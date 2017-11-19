

def greet_customer(name, num_apples=6):
    print('Hello, ' + name)
    print('We have ' + str(num_apples) + ' apples in stock.')


greet_customer('Mark')
greet_customer('Brooke', 6)
greet_customer('Greg', 2)
