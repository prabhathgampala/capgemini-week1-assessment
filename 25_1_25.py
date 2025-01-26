                                              #---1---

#ATM simulation
# def check_balance(balance):
#     print(f"Your balance: {balance}")
# def deposit_money(balance):
#     deposit_money=float(input("enter your deposit money :"))
#     if deposit_money > 0:
#         balance += deposit_money
#         print("transaction successful")
#     return balance
# def withdraw_money(balance):
#     withdraw_money=float(input("enter your withdraw money :"))
#     if withdraw_money <= balance:
#         balance -= withdraw_money
#         print("transaction successful!")
#     return balance
# def atm():
#     balance=5000
#     while True:
#         print("1. check balance")
#         print("2. deposit money")
#         print("3. withdraw money")
#         print("4. exit")
#         choice=input("enter your choice :")
#         if choice== '1': 
#             check_balance(balance)
#         elif choice== '2': 
#             deposit_money(balance)
#         elif choice== '3': 
#             withdraw_money(balance)
#         elif choice=='4' : 
#             print("thank you")
#             break
# atm()

#----------------------------------------------------------------------------------------------------------------------------------------
                                             #---2---
#temperature conversion
# def celsius_to_fahrenheit(temperature):
#     return (celsius*9/5)+32
# def celsius_to_kelvin(temperature):
#     return celsius+273.15
# def fahrenheit_to_celsius(temperature):
#     return (fahrenheit-32)*5/9
# def fahrenheit_to_kelvin(temperature):
#     return (fahrenheit-32)*5/9+273.15
# def kelvin_to_celsius(temperature):
#     return kelvin-273.15
# def kelvin_to_fahrenheit(temperature):
#     return (kelvin-273.15)*9/5+32
# def main():
#     print("Temperature Conversion")
#     print("1. Celsius to Fahrenheit")
#     print("2. Celsius to Kelvin")
#     print("3. Fahrenheit to Celsius")
#     print("4. Fahrenheit to Kelvin")
#     print("5. Kelvin to Celsius")
#     print("6. Kelvin to Fahrenheit")
#     choice =input("enter your choice: ")
#     temperature = float(input("Enter current temperature : "))
#     if choice == 1:
#         celsius_to_fahrenheit(temperature)
#     elif choice == 2:
#         celsius_to_kelvin(temperature)
#     elif choice == 3:
#         fahrenheit_to_celsius(temperature)
#     elif choice == 4:
#         fahrenheit_to_kelvin(temperature)
#     elif choice == 5:
#         kelvin_to_celsius(temperature)
#     elif choice == 6:
#         kelvin_to_fahrenheit(temperature)
# main()
 

#-----------------------------------------------------------------------------------------------------------------------------------
                                           #---3---

#prime numbers in arange
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# start = int(input("Enter start: "))
# end = int(input("Enter end: "))
# print(f"Prime numbers are: {[num for num in range(start, end + 1) if is_prime(num)]}")


#---------------------------------------------------------------------------------------------------------------------------------------------------------
                                              #---4----
                           
#student grading system
# def calculate_grade(percentage):
#     if percentage >= 90:
#         return 'A'
#     elif percentage >= 75:
#         return 'B'
#     elif percentage >= 50:
#         return 'C'
#     else:
#         return 'Fail'
# def main():
#     name = input("Enter the student's name: ")
#     subject1 = float(input("Enter marks for subject 1: "))
#     subject2 = float(input("Enter marks for subject 2: "))
#     subject3 = float(input("Enter marks for subject 3: "))
#     subject4 = float(input("Enter marks for subject 4: "))
#     subject5 = float(input("Enter marks for subject 5: "))
#     total_marks = subject1 + subject2 + subject3 + subject4 + subject5
#     percentage = (total_marks / 500) * 100
#     grade = calculate_grade(percentage)
#     print(f"Name: {name}")
#     print(f"Total Marks: {total_marks}")
#     print(f"Percentage: {percentage}")
#     print(f"Grade: {grade}")
# main()

#-------------------------------------------------------------------------------------------------------------------------------------------------------
                                                #---5---

#fizzbuzz problem
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                  #---6---
#second largest number
# def second_largest(numbers):
#     numbers = list(set(numbers)) 
#     numbers.sort() 
#     return numbers[-2] if len(numbers) > 1 else None 
# numbers = [6,89,56,888,45]
# result = second_largest(numbers)
# print("Second largest number:", result)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                      #---7---
                                                                                     
#leap year checker
# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
# years = input("Enter years : ").split()
# for year in years:
#     year = int(year) 
#     if leap_year(year):
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                     #---8---

#bill splitter
# total_amount = float(input("Enter the total bill amount: "))
# num_people = int(input("Enter the number of people: "))
# tip_percentage = float(input("Enter the tip percentage: "))
# amount = split_bill(total_amount, num_people, tip_percentage)
# if isinstance(amount, float):
#     print(f"Each person should pay: {amount}")
# else:
#     print(amount)

# def split_bill(total_amount, num_people, tip_percentage):
#     tip_amount = total_amount * (tip_percentage / 100)
#     total_with_tip = total_amount + tip_amount
#     if num_people > 0:
#         amount_per_person = total_with_tip / num_people
#         return round(amount_per_person, 2)  
#     else:
#         return "Number of people must be greater than 0"

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                            #---9---
#string analysis tool
# def analyze_string(input_string):
#     vowels = "aeiouAEIOU"
#     digits = "0123456789"
#     vowel_count = 0
#     consonant_count = 0
#     digit_count = 0
#     special_count = 0
#     for char in input_string:
#         if char.isalpha():  
#             if char in vowels:
#                 vowel_count += 1
#             else:
#                 consonant_count += 1
#         elif char.isdigit():  
#             digit_count += 1
#         else:  
#             special_count += 1
#     reversed_string = input_string[::-1]
#     return vowel_count, consonant_count, digit_count, special_count, reversed_string
# input_string = input("Enter a string: ")
# vowel_count, consonant_count, digit_count, special_count, reversed_string = analyze_string(input_string)
# print(f"Vowels: {vowel_count}")
# print(f"Consonants: {consonant_count}")
# print(f"Digits: {digit_count}")
# print(f"Special characters: {special_count}")
# print(f"Reversed string: {reversed_string}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                              #---10----
#pattern generator
# def generate_pattern(n, reverse=False):
#     if reverse:
#         for i in range(n, 0, -1):
#             print('*' * i)
#     else:
#         for i in range(1, n + 1):
#             print('*' * i)
# n = int(input("Enter the number of rows: "))
# reverse = input("Do you want to print in reverse? (yes/no): ").strip().lower()
# generate_pattern(n, reverse == 'yes')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                         #---11---

#palindrome number
# value = input("Enter a string or number : ")  
# if value == value[::-1]:
#     print(f"{value} is a palindrome.")
# else:
#     print(f"{value} is not a palindrome.")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                          #---12---

#factorial checker
# def factorial(n):
#     if n < 0:
#         return "it is a  negative number"
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# num = int(input("Enter a number: "))
# print(f"The factorial of {num} is:", factorial(num))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    #---13---

#bank loan eligibility
# def check_loan_eligibility(salary, age, credit_score):
#     reasons = []
#     if age < 18 or age > 60:
#         reasons.append("Age must be between 18 and 60")
#     if salary < 25000:
#         reasons.append("Salary must be at least 25,000")
#     if credit_score < 650:
#         reasons.append("Credit score must be 650 or above")  
#     if reasons:
#         return "Loan Rejected", reasons
#     else:
#         return "Loan Approved", ["You meet all eligibility criteria"]
# salary = float(input("Enter your salary: "))
# age = int(input("Enter your age: "))
# credit_score = int(input("Enter your credit score: "))
# status, messages = check_loan_eligibility(salary, age, credit_score)
# print("\nResult:", status)
# for message in messages:
#     print("-", message)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                        #---14---

#multiplication table generator
# def generate_multiplication_table(number, start, end):
#     print(f"\nMultiplication Table for {number} (from {start} to {end}):")
#     for i in range(start, end + 1):
#         print(f"{number} x {i} = {number * i}")
# print("Multiplication Table Generator")
# print("-" * 35)
# num = int(input("Enter the number for the multiplication table: "))
# start_range = int(input("Enter the starting range: "))
# end_range = int(input("Enter the ending range: "))
# generate_multiplication_table(num, start_range, end_range)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                        #---15---

#number guessing game
# import random
# random_number=random.randint(1,100)
# print("Welcome to the Number Guessing Game")
# attempts=0
# print("Let's go, Guess the number")
# while(True):
#     number=int(input('Enter the number :'))
#     if(number>random_number):
#         print("It's too high")
#     elif(number==random_number):
#         print('You won the Game')
#         break
#     else:
#         print("It's too low")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    #---16---

#shopping cart
# lists=[]
# def add():
#     name=input("Enter the item name: ")
#     price=int(input('Enter the price: '))
#     lists.append([name,price]) 
# def view():
#     for i in lists:
#         print(i)
# def total():
#     ans=0
#     for i in lists:
#         ans+=i[1]
#     return ans
# print("*Welcome to shopping*")
# while True:
#     option=int(input("1.Add Item\n2.View Cart Items\n3.Total Price\n4.Exit\nEnter the option: "))
#     if(option==1):
#         add()
#     elif(option==2):
#         view()
#     elif(option==3):
#         print(total())
#     else:
#         print("Thank you for shopping")
#         break

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                      #---17---

#odd and even separator
# def separate_odd_even(numbers):
#     odd_numbers = []
#     even_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
#     return odd_numbers, even_numbers
# print("Odd and Even Separator")
# print("-" * 30)
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# odd, even = separate_odd_even(numbers)
# print("\nEven numbers:", even)
# print("Odd numbers:", odd)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                        #---18--- 
 
#word counter
# def count_words(sentence):
#     words = sentence.split()
#     word_count = {}
#     for word in words:
#         word = word.lower()  
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count
# print("Word Counter")
# print("-" * 30)
# sentence = input("Enter a sentence: ")
# word_count = count_words(sentence)
# print("\nWord occurrences:")
# for word, count in word_count.items():
#     print(f"'{word}': {count}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                        #---19----

#BMI calculator
# def calculate_bmi(weight, height):
#     # Calculate BMI
#     bmi = weight / (height ** 2)
#     if bmi < 18.5:
#         category = "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         category = "Normal weight"
#     elif 25 <= bmi < 29.9:
#         category = "Overweight"
#     else:
#         category = "Obese"   
#     return bmi, category
# print("BMI Calculator")
# print("-" * 30)
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
# bmi, category = calculate_bmi(weight, height)
# print(f"\nYour BMI is: {bmi}")
# print(f"BMI Category: {category}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                            #---20---

#password strength checker
# password=input("Enter the password: ")
# n=len(password)
# upper=0
# low=0
# digit=0
# special=0
# if(n<8):
#     print("Password is weak")
# else:
#     for i in password:
#         if i.isalpha():
#             if i.lower()==i:
#                 low+=1
#             else:
#                 upper+=1
#         elif(i.isdigit()):
#             digit+=1
#         else:
#             special+=1
#     if(upper and low and special and digit):
#         print("Password is Strong")
#     else:
#         print("Password is weak")
