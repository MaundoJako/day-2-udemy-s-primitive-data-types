# Data Types TASK
#Task - Adding the two digits from a number together ---- 38 == 3 + 8 = 11
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#print(type(two_digit_number))
#Now we know it is a string it needs to be converted into an integer


print(int(two_digit_number[0]) + int(two_digit_number[1]))

#### Second way Below

#first_digit = two_digit_number[0]
#second_digit = two_digit_number[1]

#result = (int(first_digit) + int(second_digit))
#print(result)