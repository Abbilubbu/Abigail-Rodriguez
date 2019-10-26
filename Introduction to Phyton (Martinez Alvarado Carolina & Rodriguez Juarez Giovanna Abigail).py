#!/usr/bin/env python
# coding: utf-8

# # Introduction to Phyton

# By. Rodriguez Juarez Giovanna Abigail & Martinez Alvarado Carolina

# ## >Exercise 1 (A good first program)
# 
# (In this part the author shows the common program called "Hello World", but we can write any sentence that we want like this)

# In[86]:


print("Hello world!")
print("Hello again")
print("Believe in yourself")
print("Say 'yes' or 'not'")
print("I will survive") # Also the author shows how will be printed the code depending on the different OS, he talks about the text editors.


# ## >Exercise 2 (Comments and Pound Characters)
# 
# The comment is a note or a reminder that you can put in your code with the help of the "#" starting the line. This doesn't affect to our code.  

# In[87]:


# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print(" I like to study Mechatronis") # and the comment after is ignored

# You can also use a comment to "disable" or comment out code:
# print("This will not run")

#print("This will not run")


# ## >Exercise 3 (Numbers and Math)
# 
# We can realize mathematical operation with this, so the symbols to represent this operation are:
# - plus +
# - minus -
# - slash /
# - asterisk *
# - percent %
# - less than <
# - greather than >
# - less-than-equal <=
# - greather-than-equal >=

# In[89]:


print("I will count my clothes")

print("Pants", 20 - 7)
print("Shirts", 13 + 8)

print("I wil count my skirts:")

print(2 + 4 - 3 * 8 / 2)

print("Is this true 5 * 5 < 6 + 6?")

#The operation is made and then the result is added to the line of the code


# ## >Exercise 4 (Variables and Names)
# 
# The variables are important in the programming languages, they are used to name the code. "=" this symbol is necessary to give the valor to the variable.
# 

# In[91]:


chocolates = 100
lollipops = 80
cookies = 50
marshmallows = 75

print("There are", chocolates, "chocolates availables.")
print("There are only", lollipops, "lollipops availables.")
print("We have", cookies, "to eat.")
print("There are only", marshmallows, "to eat.")
#So with this examples we can identify how to put the variables to use them in the code.


# ## Exercise 5 (More Variables and Printing)
# 
# The string is the text that is put between the (double quotes), but also here in this part we can see some variables in the same string like this:
# 

# In[92]:


my_country = 'Mexico' 
my_career = 'Mechatronics'
my_language = 'Spanish'
my_name = 'Carolina Martinez'

#Here we have put the variables then we put the variable in the string:

print(f"The country {my_country} is where I live.")
print(f"I enjoy study {my_career}.")
print(f"I sepak {my_language}.")
print(f"My name is {my_name}.")
print(f"{my_country} is in America, in this continent {my_language} is the most spoken language.") 

#We put a "f" of "format" at the beginning because we have a embed variable in a string, for example if we only put a normal sentence like in the exercise 1 we musn´t add the letter "f".


# ## >Exercise 6 (Strings and Text)
# 
# (In this exercise we will learn to call variables using strings!)
# 
# A string is a method with which you can call variables already defined within the text using two auxiliaries:
# - {" ... "} => Brackets (With which we will call the variable)
# - f" ... " => Format (Which indicates that the text inside the quotes is part of a string)
# 
# ### _Example_

# In[17]:


A = 31
B = 22
C = 28
D = 23
E = 24

AC = A + C
ABCDE = A + B + C + D + E

H = "students."
G = "In mecatronics"

print(f"1.-{G} of 3rd quarter there are:\n>{ABCDE} {H}")
print(f"\n2.-{G} if us sum the total of students in each group there are:\n>{AC} {H}")


# ## >Exercise 7 - 9
# 
# (In the next 3 exercises a review of everything previously learned will be given!)

# In[84]:


# More Printing!


# "Print" with a normal text
print("1.-Now we are going to do a bunch of exercises where you just type code in and make it run. I won’t be explaining this exercise because it is more of the same. The purpose is to build up your chops.\nSee you in a few exercises, and do not skip! Do not paste!")

# "Print" with a string
a = 17
b = 5
print(f"\n2.-When I had {a} passed {b} years!\n")

print("." * 20) # This command separates one paragraph from another in line form.

A1 = "t"
A2 = "m"
A3 = "o"
A4 = "a"
A5 = "e"
A6 = "l"
A7 = "c"
A8 = "v"
A9 = "I"
A95 = "r"
A63 = "n"
A34 = "i"
A81 = "s"

print("\n")
print(A9 , end=' ') # The comma before the "end" marks that between print and print open a space; the number of desired spaces is placed inside the parenthesis.
print(A6 + A3 + A8 + A5 , end=' ')
print(A2 + A5 + A7 + A4 + A1 + A95 + A3 + A63 + A34 + A7 + A81, end=' ')
print("<3")


# In[83]:


# Printing, printing!

#".format" is another way to define a variable without calling it from above. This can be placed followed by the instruction.
# Now, this time a string defined by 5 square brackets will be made.

ABC = "{} {} {} {} {} {}"

print("    Mecatronics 3rd quarte\nNumber of students per group\n")
print(ABC.format("   Group", "3A", "3B", "3C", "3D","3E"))
print(ABC.format("   Stud.", "31", "22", "28", "23", "24"))


# In[78]:


# Printing, printing, printing!

# The word after "," is too a way to call a variable.

AA = "3A, 3B, 3C, 3D and 3E"
AB = "3A.-Arturo\n 3B.-Lizet\n 3C.Walter\n 3D.-Sharon\n 3E.Carl"

print("*In mecatronics there are 5 groups:",AA)
print("*In each group there is a leader:\n",AB)
print("""
*Some of their grades are:
 Arturo - 10
 Lizet - 9.6
 Walter - 9.9
 Sharon - 9.5
 Carl - 9.7
""") # We can put consecutive lines if we place 3 quotes in a row.


# ## >Exercise 10 (What Was That?)
# 
# (Through commands, some text features will be edited!)

# In[82]:


print("\"The next list is about the people how fail the quarter for group!:\"") # "\"" It allows put comillas
print("""
\t*3A
Laura \\ Michael \\ Luis\n
\t*3B
Manuela \\ Abby \\ Moises \\ Rodolgo\n
\t*3C
Rumario \\ Esther \\ Constancia \\ Luis \\ Tulio\n
\t*3D
Cornelio \\ Juan \\ Marcos\n
\t*3E
.......................
""") # With "\t" you can do a list.


# In[ ]:




