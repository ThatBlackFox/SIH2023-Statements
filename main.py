from bs4 import BeautifulSoup
import csv

with open('toscrape.html','r') as f:
    resp = f.read()

soup = BeautifulSoup(resp, 'lxml')
colms = soup.find_all('thead')
colms = colms[2:]
print(len(colms))

f = open('problemstatements.csv','w')
write = csv.writer(f)
     
write.writerow(['ID','Title','Description','Organization','Category','Domain Bucket','Youtube Link','Dataset link'])
for thead in colms:
    div_tags = thead.find_all('td')
    il = []
    for tags in div_tags:
        try:
            il.append(tags['div'].text.strip())
        except:
            il.append(tags.text.strip())
    il[0]='SIH'+il[0]
    write.writerow(il)

f.close()
    
