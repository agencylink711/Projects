
# Simple function
def greet():
    print("hello to everyone")
    print("Just take a break if you are tired")
    print("after going outside, come back inside")

greet()

'''-----------------------------------------------------------'''

# Function that allows for input
def greet_with_name(name):
    print(f"hello {name}")
    print(f"Just take a break {name} if you are tired")
    print(f"hey, after going outside {name}, come back inside")

# it's only when we call the function, that we actually pass over the value that is store inside the variable name
greet_with_name("Mary")


'''-----------------------------------------------------------'''

# Functions that allow for multiple inputs (POSITIONAL ARGUMENTS)

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Just take a break {name} if you are tired in {location}")
    print(f"hey, after going outside in {location}, {name}, come back inside")

greet_with("Thomas", "Bad Nauheim")


'''-----------------------------------------------------------'''


# Functions that allow for multiple inputs (KEYWORD ARGUMENTS)

def greet_with_arg(name="Hannah", location="Hamburg"):
    print(f"Hello {name}")
    print(f"Just take a break {name} if you are tired in {location}")
    print(f"hey, after going outside in {location}, {name}, come back inside")

greet_with_arg(name="Hannah", location="Hamburg")


'''-----------------------------------------------------------'''

