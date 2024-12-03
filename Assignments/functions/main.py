# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

#1 greet
def greet(name):    
    return ("Hello, " + name + "!") 
print(greet("Bob"))

#2 add
def add(a, b, c):
    return a + b + c
print(10 + 5 + 2)
print(add(10, 5,2))

#3 positive
def positive(x):
    return x > 0
print(positive(107))
print(positive(-20))
print(positive(0))

#4 negative
def negative(y):
    return y < 0
print(negative(-5))
print(negative(7))
print(negative(0))