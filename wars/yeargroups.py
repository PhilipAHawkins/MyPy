"""
will grab a list of war articles available on wiki and a link to the wiki page for that war
--phil

So, this was a fail. APparently pd.read_html can't do non-ascii and this was failing, like, all the time. Live & learn.
"""

import pandas as pd

time_groups = ["before_1000", "1000-1499", "1500-1799", "1800-99","1900-44", "1945-89",
"1990-2002", "2003-10", "2011-present"]

prefix = "https://en.wikipedia.org/wiki/List_of_wars_"
master_dfs = pd.DataFrame()
for page in time_groups:
    my_url = prefix + page
    print("url is: ", my_url)
    page_tables = pd.read_html(my_url, index_col=0, attrs={"class":"wikitable"}, encoding=str)
    print(len(page_tables))
    for i in range(len(page_tables)-1):
        print("\nPage is: ", page, "table number is: ", i)
        append_df = page_tables[i]
        append_df['Page'] = page
        append_df['Table'] = i
        master_dfs.append(append_df, ignore_index=True)
master_dfs.to_csv("temp.csv", encoding='utf-8')

"""data cleaning i'm seeing so far:
    Convert "Name" col to replace spaces with underscores for easier linking in future list.
    If Year starts with "c. ", it's an estimated year. need a way to record when that happens, possibly new col of df.
    Sometimes there isn't a year given, so just repeat the year above that.
"""