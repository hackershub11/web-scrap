from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
quotes="http://intra.iitj.ac.in:8080/Aryabhatta_New/attendanceReport.do"
uClient=uReq(quotes)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html, "html.parser")
quotes=page_soup.findAll("div",{"class":"tagline"})
print(quotes[0].text.strip())


