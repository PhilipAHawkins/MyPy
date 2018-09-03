Project that scrapes information from Wiki tables on airports found across the world

The data is then shaped into a dataframe and Nominatim is used to find coordinates for the
airport if at all possible. The CSV output is ideal for dropping into software like Tableau 
or a D3 project featured elsewhere in the repo.

Last step is an algorithm that calculates the Great Arc path that an airplace might take as 
it traveled over the earth, which is different from any map of the airplane's trip that simply 
draws a straight line from one airport to another.

The original intent was to use this in Tableau with all data and calculations done before
loading into the software but they're releasing a new version that automatically does
all the math for you upon request so... lol.