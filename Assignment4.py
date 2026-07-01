"""
Assignment 4: Print Using sep
Write a Python program that:
Creates three variables:
Your name
Your country
Your favorite programming language
Displays all three values on the same line 
using the sep keyword with " | " as the separator.
"""

name=input("please enter your name")
country=input("please enter your country")
favproglanguage=input("please enter your favorite programming language")

print(name,country,favproglanguage, sep="|")