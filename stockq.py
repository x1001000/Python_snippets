from requests import get
from bs4 import BeautifulSoup
page_source = get('http://www.stockq.org/funds/fund/alliancebernstein/I466.php').text
soup = BeautifulSoup(page_source,"html.parser")
tr_list = soup.find_all('tr', class_={'row1','row2'})
for tr in tr_list[2:]: # you don't need the first 2 row2 info on the top of the webpage
    td_list = tr.find_all('td')
    for td in td_list:
        print(td.text, end='\t')
    print()