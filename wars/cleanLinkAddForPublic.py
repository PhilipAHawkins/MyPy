import pandas as pd
import openpyxl
import numpy as np

# unsure if i want each belligerent on one line or joined into one string.
# proceeding with them on one line as the data gave me for now.

wb = openpyxl.load_workbook('war_list.xlsx')
ws = wb['war_list']
my_links = []
war_number = 0
war_id=[]
for i in ws['C'][1:]:
    try:
        my_text = i.hyperlink.target
        my_links.append("https://wikipedia.org" + my_text[17:])
        war_id.append(war_number + 1)
        war_number+=1
    except:
        my_links.append(np.NaN)
        war_id.append(np.NaN)
data = pd.read_excel('war_list.xlsx', "war_list")
data['link'] = my_links
data['war_number'] = war_id
data.to_excel("List_of_Wars_Throughout_History.xlsx")
