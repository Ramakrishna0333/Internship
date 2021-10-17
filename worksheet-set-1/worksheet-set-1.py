#!/usr/bin/env python
# coding: utf-8

# ### Factorial Number

# In[3]:


a = int(input("Enter a number:"))
factorial = 1
if a<0:
    print("Factorial does not exist for negative numbers")
elif a==0:
    print("The factorial of 0 is 1")
else:
    for i in range (1,a+1):
        factorial = factorial *i
    print("The factorial of",a,"is",factorial)


# ### Prime or composite

# In[9]:


def primechecker(a):  
    if a > 1:  
        for j in range(2, int(a/2) + 1):  
            if (a % j) == 0:  
                print(a, "is a composite number")  
                break    
        else:  
            print(a, "is a prime number")  
    else:  
        print(a, "is neither prime number nor composite number")  
a = int(input("Enter an input number:"))  
primechecker(a) 


# ### Palindrome 

# In[10]:


string= input("enter string:")
if(string==string[::-1]):
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")


# ### Frequency

# In[14]:


string=input("Enter the string: ")

newstr=list(string)

newlist=[]

for j in newstr:

    if j not in newlist:

        newlist.append(j)

        count=0

        for i in range(len(newstr)):

            if j==newstr[i]:

                count+=1

        print("{},{}".format(j,count))


# ### finding third side of right angles when two sides given

# In[17]:


def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))


# In[ ]:





# In[ ]:




