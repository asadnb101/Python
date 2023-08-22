#string manipulation 

input_string = input("Enter a name: ")
occurence= input("Enter a character: ")

def reverse(input_string):
    return input_string[: : -1]

def length(input_string):
    return len(input_string)

def count(input_string, occurence):
    return input_string.count(occurence)

print(reverse(input_string))
print(length(input_string))
print(count(input_string, occurence))