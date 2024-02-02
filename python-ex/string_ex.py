a = "Hello, World!"
print(a[1])
print(a[4])
#slicing string
b = "Hello, World!"
print(b[2:5])

#sliced to the end
b = "Hello, World!"
print(b[2:])

#string modification
a = "Hello, World!"
print(a.upper())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Format Strings
age = 36
txt = "My name is John, and I am {} years old"
print(txt.format(age))

# Escape character
txt = "We are the  \"juneBatch\" of primus learning"
print(txt)