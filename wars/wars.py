from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup

time_groups = ["before_1000", "1000-1499", "1500-1799", "1800-99","1900-44", "1945-89",
"1990-2002", "2003-10", "2011-present"]

page_no = 0
df_out = None
print("df")
master_list = []
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
while page_no < 9:
    print("Page: ", page_no)
    url = "https://en.wikipedia.org/wiki/List_of_wars_"
    letter = time_groups[page_no]
    page = urlopen(url + letter)
    soup = BeautifulSoup(page)
    for row in soup.findAll('tr'):
        cells = row.findAll('td')
        if len(cells)==5:
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
            E.append(cells[4].find(text=True))
    page_no+=1
A = [x.encode('UTF8') for x in A]
B = [x.encode('UTF8') for x in B]
C = [x.encode('UTF8') for x in C]
D = [x.encode('UTF8') for x in D]
E = [x.encode('UTF8') for x in E]
df=pd.DataFrame(A,columns=['Start'])	
df=pd.DataFrame(B,columns=['Finish'])
df=pd.DataFrame(C,columns=['Name'])
df=pd.DataFrame(D,columns=['Belligerent_Victorious'])
df=pd.DataFrame(E,columns=['Defeated'])
writer = pd.ExcelWriter('temp.xlsx')
df.to_excel(writer)
writer.save()