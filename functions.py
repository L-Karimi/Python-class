def greetings(name,age):
    year = 2022-age
    return print(f"Hello {name},yes you were born in {year}")
def greet(*name):
         print(f'Hello {name}')
         
#Write a function that accepts any number of integers and returns the sum of all of them.
#eg.sum 1,2,3,4=11
"""def sum(num1, *args):
    total = num1
    for num in args:
        total = total + num
    return total
def greet_multiple(**kwargs):
     return print(kwargs)
def greet_multiple(**kwargs):
    keys=kwargs.keys()
if 'country' in keys:
    print(f"Hello {kwargs['name']} you are from {kwargs['country']}")
elif 'age' in keys:
    year =2022 - kwargs["age"]
    print (f"Hello {kwargs['name']}you were born in {'year'}")
elif  not kwargs:
    print(f"Hello arguments") """