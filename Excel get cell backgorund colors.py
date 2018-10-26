"""
if you're in an environment where you need to read an Excel file
and get the color of the cells in that file, 
and your machine isn't allowed openpyxl,
then this is for you.
This will read a workbook, 
changes cell colors to column values in a dataframe,
and turn into a new df
"""
from xlutils.copy import copy
import xlrd
import xlwt # your IDE may give an "unused" warning
import pandas as pd
my_wb = xlrd.open_workbook("Path/to/wb.xlsx", formatting_info=True) 
my_worksheet = my_wb.sheet_by_name("data")
# get number of columns
my_columns = len(list(filter(None,my_worksheet.col_values(0)))) + 1
# let's go ahead and put the worksheet contents into a dataframe
df = pd.read_excel("Path/to/wb.xlsx", sheetname="data")
# and also a list to store color results in
my_color_returns = []
# now we can start reading colors and appending values.
for i in range(1, my_columns):
    xfx_loop = my_worksheet.cell_xf_index(i,0) # this is reading the first column I believe
    xf_loop = my_wb.xf_list[xfx_loop]
    bgx = xf_loop.background.pattern_colour_indx # yes, "colour". lol.
    if bgx == 13: # see below for where we got this
        my_color_returns.append("this was a yellow cell")
    else:
        my_color_returns.append("this was not a yellow cell")
df['ColorResults'] = my_color_returns
# your df is now ready for anything you need to do with it.
"""
See the RGB values below. 
Above, we used bgx = 13, which is yellow. Note in the below table
that "13" reads 13: (255, 255, 0).
Those values (255, 255, and 0) are the RGB values for Excel's yellow color.

{0: (0, 0, 0), 1: (255, 255, 255), 2: (255, 0, 0), 3: (0, 255, 0), 4:
(0, 0, 255), 5: (255, 255, 0), 6: (255, 0, 255), 7: (0, 255, 255), 8:
(0, 0, 0), 9: (255, 255, 255), 10: (255, 0, 0), 11: (0, 255, 0), 12:
(0, 0, 255), 13: (255, 255, 0), 14: (255, 0, 255), 15: (0, 255, 255),
16: (128, 0, 0), 17: (0, 128, 0), 18: (0, 0, 128), 19: (128, 128, 0),
20: (128, 0, 128), 21: (0, 128, 128), 22: (192, 192, 192), 23: (128,
128, 128), 24: (153, 153, 255), 25: (153, 51, 102), 26: (255, 255,
204), 27: (204, 255, 255), 28: (102, 0, 102), 29: (255, 128, 128), 30:
(0, 102, 204), 31: (204, 204, 255), 32: (0, 0, 128), 33: (255, 0,
255), 34: (255, 255, 0), 35: (0, 255, 255), 36: (128, 0, 128), 37:
(128, 0, 0), 38: (0, 128, 128), 39: (0, 0, 255), 40: (0, 204, 255),
41: (204, 255, 255), 42: (204, 255, 204), 43: (255, 255, 153), 44:
(153, 204, 255), 45: (255, 153, 204), 46: (204, 153, 255), 47: (255,
204, 153), 48: (51, 102, 255), 49: (51, 204, 204), 50: (153, 204, 0),
51: (255, 204, 0), 52: (255, 153, 0), 53: (255, 102, 0), 54: (102,
102, 153), 55: (150, 150, 150), 56: (0, 51, 102), 57: (51, 153, 102),
58: (0, 51, 0), 59: (51, 51, 0), 60: (153, 51, 0), 61: (153, 51, 102),
62: (51, 51, 153), 63: (51, 51, 51), 64: None, 65: None, 81: None,
32767: None}

use websites like https://rgb.to/ or http://dmcritchie.mvps.org/excel/colors.htm
 to verify your RGB values.

If your color isn't one of the 56 then maybe don't use Python, as VBA does
allow you to use syntax like
Selection.Interior.Color = RGB(200, 250, 200)
Sadly, Hex selection methods are hard to come by in VBA (not impossible tho)
"""