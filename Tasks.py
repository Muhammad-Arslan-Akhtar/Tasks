#!/usr/bin/env python
# coding: utf-8

# ### PIAIC61773

# # Write python program to check whether the number is positive or negative
1. Take the value of the integer and store in a variable.
2. Use an if statement to determine the number is positive or negative.
3. Exit.
# In[ ]:


print(str.upper("*****Program to check whether the number is positive or negative*****"))
print("_____________________________________________________________________")
choice = False
while True:
    num = int(input("\nEnter any integer number:"))
    if(num>0):
        print(num," is positive integer")
        print("______________________\n")
    elif(num==0):
        print(num," is zero, which is neither postive nor negative")
        print("_________________________________________________\n")
    else:
        print(num," is negative integer")
        print("_______________________\n")
    opt=str(input("Do you want to continue (y/n):"))
    if(opt=='y' or opt=='Y'):
        choice==True
    if(opt == 'n' or opt =='N'):
        print("\nThank you and hope to see you again :)")
        print("_____________________________________")
        break
exit()


# # Write python program to take the marks of 5 subjects and display the grade
1. Take in the marks of 5 subjects from the user and store it in different variables.
2. Find the average of the marks.
3. Use an else condition to decide the grade based on the average of marks.
4. Exit.
# In[ ]:


choice = False
while True:
    print(str.upper("***student grading system***"))
    print("____________________________")
    physics = float(input("Enter Marks Of Physics: "))
    english = float(input("Enter Marks Of English: "))
    math = float(input("Enter Marks Of Mathematics: "))
    computer = float(input("Enter Marks Of Computer: "))
    chemistry = float(input("Enter Marks Of Chemistry: "))
    average = float((physics + english + math + computer + chemistry)/5)
    print("\nYour average is : ",average)

    if(average >= 90):
        grade = 'A+'
    elif(average >= 85 and average < 90):
        grade = 'A'
    elif(average >= 80 and average < 85):
        grade = 'A-'
    elif(average >= 77 and average < 80):
        grade = 'B+'
    elif(average >= 73 and average < 77):
        grade = 'B'
    elif(average >= 70 and average < 73):
        grade = 'B-'    
    elif(average >= 65 and average < 70):
        grade = 'C+'
    elif(average >= 60 and average < 65):
        grade = 'C'
    elif(average >= 55 and average < 60):
        grade = 'C-'
    elif(average >= 50 and average < 55):
        grade = 'D'
    elif(average < 50):
        grade = 'F'

    if(average >= 50):
        print("Congratulations, Your Grade is ",grade,"\n\n")
        print("____________________________________")
    elif(average < 50):
        print("Better luck next time. Your grade is: ",grade,"\n\n")
        print("________________________________________")
        
        
    opt=str(input("Do you want to continue (y/n):"))
    print("_______________________________")
    print("\n\n") 
    if(opt=='y' or opt=='Y'):
        choice==True
    if(opt == 'n' or opt =='N'):
        print("\nThank you and hope to see you again :)")
        print("_____________________________________")
        break    
exit()


# # Write python program to read 2 numbers and print their Quotient and Remainder
1. Take in the first and second number and store it in separate variables.
2. Then obtain the quotient using division and the remainder using using modulus operator.
3. Exit.
# In[ ]:


choice = False
while True:
    print(str.upper("***quotient and reamainder***"))
    print("___________________________")
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    quotient = num1/num2
    print("The Quotient is : ",quotient)
    remainder = num1%num2
    print("The Remainder is: ",remainder)
    print("\n_______________________________")
    opt = str(input("Do you want to continue(y/n): "))
    print("\n_______________________________")
    if(opt=='y' or opt=='Y'):
        choice==True
    elif(opt=='n' or opt=='N'):
        print("Thank you and hope to see you again :)")
        print("______________________________________")
        break
exit()


# # Write python program to print all integers that are not divisible by either 2 or 3 and lie between 1 and 50.
1. Use a for-loop ranging from 0 to 51
2. Then use an if statement to check if the number isn't divisible by both 2 and 3.
3. Print the numbers satisfying the condition.
4. Exit.
# In[ ]:


print("Numbers\n_______")
for num in range(0,51):
    print(num)
print("____________________________________")
print("Numbers which are not divisible by 2\n____________________________________")
for x in range(0,51):
    if(x%2!=0):
        print(x, "is not divisible by 2")
print("____________________________________")
print("Numbers which are not divisible by 3\n____________________________________")
for y in range(0,51):    
    if(y%3!=0):
        print(y, "is not divisible by 3")
print("____________________________________")

exit()
    

        


# ## Write a python program to Exchange the values of two numbers without using a temporary variable
Problem Solution
1. Take the values of both the elements from the user.
2. Store the values in seperate variables.
3. Add both the variables and store it in the first variable.
4. Subtract the second variable from the first and store it in the second variable.
5. Then, subtract the first variable from the second variable and store it in the first variable.
6. Print the swapped values.
7. Exit.Method 1:
# In[1]:


num1 = float(input("Enter First Value: "))
num2 = float(input("Enter Second Value: "))

print("\nvalue 1 before swapping is: "+str(num1))
print("value 2 before swapping is: "+str(num2))


# 1      1      2
num1 = num1 + num2
# 3

# 2     3       2
num2 = num1 - num2
# 1

# 3     3      1
num1 = num1 - num2

print("\nvalue 1 after swapping is: "+str(num1))
print("value 2 after swapping is: "+str(num2))
exit()

Mthod 2:
# In[1]:


num1 = float(input("Enter First Value: "))
num2 = float(input("Enter Second Value: "))

print("\nvalue 1 before swapping is: "+str(num1))
print("value 2 before swapping is: "+str(num2))



num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2

print("\nvalue 1 after swapping is: "+str(num1))
print("value 2 after swapping is: "+str(num2))
exit()

Method 3:
# In[1]:


num1 = float(input("Enter First Value: "))
num2 = float(input("Enter Second Value: "))

print("\nvalue 1 before swapping is: ",num1)
print("value 2 before swapping is: ",num2)

num1, num2 = num2, num1

print("\nvalue 1 after swapping is: ",num1)
print("value 2 after swapping is: ",num2)
exit()


# ## Write a python program to find Area of a Triangle Given All 3 Sides
Problem Solution
1. Take all the three sides of the triangle and store it in three seperate variables.
2. Then using the Heron's formula, compute the area of triangle.
3. Print the area of triangle.
4. Exit.By Heron's Formula:
# In[3]:


print(str.upper("***area of a triangle***"))
print("_______________________")
choice = False
while True:
    base = float(input("Enter Base of triangle: "))
    hypotenuse = float(input("Enter Hypotenuse of traingle: "))
    height = float(input("Enter Height of traingle: "))

    s = (base+hypotenuse+height)/2
    area = (s*(s-base)*(s-hypotenuse)*(s-height))**(1/2)

    print("\nArea of a triangle is: ",area)
    opt = str(input("Do you want to continue (y/n):" ))
    print("_________________________________________")
    if(opt=='y' or opt=='Y'):
        choice==True
    elif(opt=='n' or opt=='N'):
        print("\nThank you and hope to see you again :)")
        print("_____________________________________")
        break
exit()


# ## Write python program to print largest even and largest odd number in a list
1. Take the number of elements to be in the list from the user.
2. Take in the elements from the user using a for loop and append to a list.
3. Using a for loop, get the elements one by one from the list and check if it odd or even and append them to different lists.
4. Sort both the lists individually and get the length of each list.
5. print the last elements of the sorted lists.
6. Exit.
# In[6]:


n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
c=[]
d=[]
for i in b:
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()
count1=0
count2=0
for k in c:
    count1=count1+1
for j in d:
    count2=count2+1
print("Largest even number:",c[count1-1])
print("Largest odd number",d[count2-1])
exit()


# ## Write python program to find the second largest number in a list
1. Take in the number of elements and store it in a variable.
2. Take in the element of the list one by one.
3. Sort the list in ascending order.
4. Print the second last element of the list.
5. Exit.
# In[10]:


list1 = [] 
num = int(input("Enter number of elements in list: ")) 
 
for i in range(1, num + 1): 
    ele = int(input("Enter elements: ")) 
    list1.append(ele) 
    
list1.sort() 
print("Second largest element is:", list1[-2]) 
exit()


# ## Write python program to find the union of two lists
1. Define a function which accepts two lists and returns the union of them.
2. Declare two empty lists and initialise to an empty list.
3. Consider a for loop to accept values for two lists.
4. Take the number of elements in the list and store it in a variable.
5. Accept the values into the list using another for loop and insert into the list.
6. Repeat 4 and 5 for the second list also.
7. Find the union of the two lists.
8. Pint the union.
9. Exit.
# In[6]:


def Union(list1, list2): 
    final_list = list1 + list2 
    return final_list 

list1 = [] 
list2 = []
num1 = int(input("Enter number of elements in list 1: "))
num2 = int(input("Enter number of elements in list 2: "))
 
for i in range(1, num1 + 1): 
    ele = int(input("Enter element of list 1: ")) 
    list1.append(ele)
for j in range(1, num2 + 1): 
    ele = int(input("Enter element if list 2: ")) 
    list2.append(ele) 
print(Union(list1, list2))
exit()


# In[1]:


# Maintained repetition  
def Union(list1, list2): 
    final_list = list1 + list2 
    return final_list 
 
list1 = [3, 6, 2, 54, 17, 16, 26 ,72] 
list2 = [52, 78, 75, 12, 26, 32, 77, 74] 
print(Union(list1, list2))


# In[2]:


# Maintained repetition and order  
def Union(list1, list2): 
    final_list = sorted(list1 + list2) 
    return final_list 
  

list1 = [23, 15, 2, 14, 14, 16, 20 ,52] 
list2 = [2, 48, 15, 12, 26, 32, 47, 54] 
print(Union(list1, list2))


# In[3]:


# Without repetition  
def Union(list1, list2): 
    final_list = list(set(list1) | set(list2)) 
    return final_list 
  

list1 = [23, 15, 2, 14, 14, 16, 20 ,52] 
list2 = [2, 48, 15, 12, 26, 32, 47, 54] 
print(Union(list1, list2))

