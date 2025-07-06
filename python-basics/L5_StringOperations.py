str_value = "I am a Boy"
str_value_2 = "123"
str_value_3 = 'Hello'
str_value_4 = "5.9"
str_value_5 = "False"


print(f"{str_value}\n{str_value_2}\n{str_value_3}\n{str_value_4}")

# length check
print(len(str_value))
print(len(str_value_4))
print(len(str_value_3))

# type check
print(type(str_value))
print(type(str_value_4))
print(type(str_value_3))

# type conversion
int_data = int(str_value_2)
print(type(int_data))

bool_data = bool(str_value_5)
print(type(bool_data))

# join two strings
print(str_value_2+str_value_3)

# check the string is numeric type or character type or alphanumeric type
print(str_value_2.isalnum()) # true
print(str_value_2.isnumeric()) #true
print(str_value_2.isalpha()) # false
print(str_value_5.isupper()) # false

# convert string to lower case upper case and camel case or title case
print(str_value.lower())
print(str_value.upper())
print(str_value.title())

#  trim or strip the space

str_value = " Hello World  "
print(str_value.strip())
print(str_value.lstrip())
print(str_value.rstrip())

#  print each character of string with space
str_value = "Hello"
print(" ".join(str_value))

# iterate string  character
for i in str_value:
    print(i)

# find the string contains text or not

str_value = "write a novel"
if "novel" in str_value:
    print("String contains novel")
else:
    print("String does not contains novel")


# Find the number of character or word occurance in side the string
# Note Count arguments are  Case Sensitive
str_value = " I am 30 years old and I am married"
print(str_value.count("K")) # 0
print(str_value.count("30")) # 1
print(str_value.count("I")) # 2

# spilt the string with index
print(str_value[3:9])

#  Reverse String using slicing concept
print(str_value[::-1])

# Revere string using for loop
my_string = " Hello World"


# Using for loop
for i in range(0, len(my_string) - 1):
    val = len(my_string) - 1 - i
    print(my_string[val])

# or regular expressions





