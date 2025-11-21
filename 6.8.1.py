def first_two(text):
    return text[:2]


text = input("Enter a string: ")
print(first_two(text))


def last_three(text):
    return text[-3:]

text = input("Enter a string: ")
print(last_three(text))

def every_second(text):
    return text[::2]

text = input("Enter a string: ")
print(every_second(text))


def reverse_string(text):
    return text[::-1]

text=input("Enter a string: ")
print(reverse_string(text))


def forward_and_backward(text):
    return text + text[::-1]

text= input("Enter a string: ")
print(forward_and_backward(text))

