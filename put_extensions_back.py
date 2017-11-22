# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:09:50 2017

@author: phhawkins
What's that, you say? You changed all your files to txt and now
you need them back again? Look no further! Since the 
change_extensions_fast.py file preserved the previous
filetype in the filename, we just need to put it back where
it was before.
"""
import os
my_path = 'C:/Users/phhawkins/Documents/testdir/testdir2/testdir3'

for my_file in os.listdir(my_path):
    if my_file.endswith('.txt'):
        no_txt = my_file.replace('.txt','')
        list_txt = list(no_txt)
        i = len(list_txt) -1 - list_txt[::-1].index('_')
        before_txt = ''.join(list_txt[0:i])
        after_txt = ''.join(list_txt[i+1:len(list_txt)])
        new_filename = before_txt + "."+ after_txt
        new_name = my_path + "/" + new_filename
        in_file = my_path + "/" + my_file
        os.rename(in_file,new_name)