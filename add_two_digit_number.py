#num_char = len(input("What is your name? "))
#print("Your name has " + str(num_char) + " characters.")

two_digit_number = input("Type a two digit number: ")

#print(type(two_digit_number))

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#print(first_digit)
#print(second_digit)

result = int(first_digit + second_digit)
print(result)