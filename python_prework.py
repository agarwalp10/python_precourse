
#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has been defined as below.

def hello_name(username):
    """Printing out hello.USERNAME!"""
    print("hello." + username.upper() + "!")
    
print("Question 1:")    
hello_name("agarwalp10")


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Functiion prints out odd numbers from 1-100"""
    for i in range(0,100):
        if i%2 != 0:
            print(i)

print("\nQuestion 2:")
first_odds()


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
#The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Given a list, function will find max number"""
    max_num = max(a_list)
    return max_num

print("\nQuestion 3:")
num_list = [6,3,9,15,13,18,4,6,7]
print(max_num_in_list(num_list))


#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
#unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Checking to see if the year is a leap year or not"""
    if a_year%4 == 0 and a_year%100 !=0:
        return True
    elif a_year%400 == 0:
        return True
    else: 
        return False

print("\nQuestion 4:")
year = is_leap_year(2024)
if year == True:
    print("It's a leap year.")
elif year == False:
    print("It's not a leap year.")


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.

def is_consecutive(a_list):
    """Checking if the list has consecutive numbers"""
    for i in range(0, len(a_list)):
        if i == 0:
            continue
        elif a_list[i] == a_list[i-1] + 1:
            if i == len(a_list)-1:
                return True
            else: 
                continue
        else:
            return False 
            break

print("\nQuestion 5:")
a_list = [3,4,5,6,7,8]
print(is_consecutive(a_list))