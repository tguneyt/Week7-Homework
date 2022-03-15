'''
Tayyip Guney 13.03.2022

Write a program that list according to email addresses without email domains in a text.
Example:

Input:
The advencements in biomarine studies franky@google.com with the investments necessary and 
Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...
Output :
franky
sinatra123
'''

import re

f_text='The advencements in biomarine studies 123franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...'
# f_text='asd.34@gma12il.com hello t.guney11@gmail.comasd t_guney.66@gmail.com' 

pat =  r"[\w.+-]+@[\w-]+\.[\w.-]+" # pattern for email
matched_text = re.findall(pat,f_text)  # find all match

for i_txt in matched_text:
    # print(i_txt)
    i_txt=i_txt.split("@")  # separate username from domain
    print(i_txt[0]) 
