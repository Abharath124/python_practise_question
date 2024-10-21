#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q-1
vow = "aeiouAEIOU"

def is_vowel(char):
    if char in vow:
        return True
    else:
        return False
char = input("Enter a character: ")

if is_vowel(char):
    print(f"'{char}' is a vowel.")
else:
    print(f"'{char}' is not a vowel.")


# In[3]:


#Q-2
def calculate_fee(days):
    fee = 0
    if days <= 5:
        fee = days * 2
    elif days <= 10:
        fee = (5 * 2) + ((days - 5) * 3)
    elif days <= 15:
        fee = (5 * 2) + (5 * 3) + ((days - 10) * 4)
    else:
        fee = (5 * 2) + (5 * 3) + (5 * 4) + ((days - 15) * 5)
    return fee

days = int(input("Enter the number of days the book is used: "))

if days > 0:
    total_fee = calculate_fee(days)
    print(f"The total fee for {days} days is: Rs. {total_fee}")
else:
    print("Invalid input. Days must be a positive number.")


# In[4]:


#Q-3
def check_weirdness(n):
    if n % 2 != 0:
        print("WEIRD")
    elif n % 2 == 0:
        if 2 <= n <= 5:
            print("NOT WEIRD")
        elif 6 <= n <= 20:
            print("WEIRD")
        elif n > 20:
            print("NOT WEIRD")
            
n = int(input("Enter a positive integer: "))

if n > 0:
    check_weirdness(n)
else:
    print("Invalid input. Please enter a positive integer greater than 0.")


# # Assignment-2

# In[8]:


#Q-1
user = int(input("Enter a number:"))
user1 = int(input("Enter a number:"))
print()
add = user + user1
sub = user - user1
mul = user * user1
div = user / user1
mod = user % user1
expo = user ** user1
fd = user // user1

print(f"Addition:{add}\nSubstraction:{sub}\nMultiplication:{mul}\nDivision:{div}\nModulus:{mod}\nExponent:{expo}\nFloor Division:{fd}")


# In[21]:


#Q-2
f_num = int(input("Enter a number:"))
s_num = int(input("Enter a number:"))

if f_num > s_num:
    print("First number is greter")
else:
    print("Second number is greater")

if f_num == s_num:
    print("first number equal to second number")
else:
    print("Both are not equal")

if f_num <= s_num:
    print("First number less than equal to second number")
else:
    print("First number is not equal to second number")  


# In[28]:


#Q-3
first = bool(int(input("Enter a number:")))
sec = bool(int(input("Enter a number:")))
print()

r1 = first and sec

r2 = first or sec

r3 =  not first
r4 = not sec

print("And:",r1,"OR:",r2,"Not:",r3,"Not:",r4)


# # Part-2 Strings

# In[4]:


#Q-4
user = str(input("Enter a txt:")) 
print(len(user))
first_char = user[0]
second_char = user[-1]
print("First charcter:",first_char)
print("Last charcter:",second_char)
print("Reverse:",user[::-1])
upper_str = user.upper()
lower_str = user.lower()
print("Uppercase and lowercase:",upper_str,"&",lower_str)


# In[9]:


#Q-5
name = str(input("Enter a name:"))
age = int(input("Enter a age:"))
print(f"Hello {name} You are {age} Years old")


# In[15]:


#Q-6
sen = input("Enter a Sentence:")
search = input("Enter a word to search:")
if search in sen:
    position = sen.index(search)
    print(search,position )
else:
    print(search)


# In[73]:


#Q-7
li=list(map(int(input().split())))


total_sum = sum(li)
print(total_sum) 


largest = max(li)
smallest = min(li)

print("Largest Number:",largest)
print("Smallest Number:",smallest)


# In[47]:


# Q-8
fruits = ["Banana","Appele","Kiwi","Avocado","Grapes"]
fruits.insert(5,"Mango")
print(fruits)


# In[84]:


#Q-9
# num = list(map(int(input().split())))
num = [22,44,66,55,33]
descending = sorted(num,reverse=True)
ascending = sorted(num,reverse=False)

print("Ascending_Order:",ascending)
print("Descending_Order:",descending)


# In[85]:


#Q-10
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("First 5 elements:",num[:5])
print("last 5 elements:",num[-5::])
print("Index 2 to index 7:",num[2:8])


# In[89]:


#Q-11
student_names = ["Bharath","Tarun","Rahul"]
student_marks = [85,89,91]
add = student_names+student_marks
print(add)


# In[ ]:




