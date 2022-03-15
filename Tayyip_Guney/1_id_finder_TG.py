"""
Tayyip Guney 13.03.2022

Question 1:
Write a program that detects the ID number hidden in a text. We know that the format of the 
ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6
Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678
Output : VZ4PF94B6
"""
import re

def id_finder(text):
    pat= r"\w{2}\d\w{2}\d{2}\w\d"

    matched_text=re.search(pat,text)

    if matched_text:
        print(f'ID Number : {matched_text.group()}')
    else:
        print("*** ID Number not found ***")

# input_data = input('input a text: ')
input_data = "AEGTV5VZ4PF94B6YH678"
id_finder(input_data)

