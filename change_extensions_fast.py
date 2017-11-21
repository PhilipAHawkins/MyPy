# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:16:37 2017

@author: phhawkins

Changes file extensions in a folder of files
and also appends the previous filetype to 
the filename for preservation. So if you ever
need to quickly change a folder's worth of contents 
to txt but also need to remember what filetype you 
changed it from, this is your tool.

If you don't want a file ext to be changed,
you can set that too with dont_change.
"""
import os
my_path = 'C:/Users/phhawkins/Documents/testdir/testdir2/testdir3'
new_ext = ".txt"
dont_change = ".html"

for my_file in os.listdir(my_path):
    my_filename, my_ext = os.path.splitext(my_file)
    if my_ext != dont_change:
        in_file = my_path + "/" + my_file
        out_file = my_path + "/" + my_filename
        my_ext= my_ext.strip(".")
        new_name = out_file + "_" + my_ext + new_ext
        os.rename(in_file,new_name)