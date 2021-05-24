import sys

print (sys.version)
print(sys.executable)

def greet(wh_to_great):
    greeting = 'Hello, {}'.format(wh_to_great)
    return greeting

print(greet('World'))
print(greet('Grant'))
print('asdfasdf')