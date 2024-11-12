from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape= requests.get("https://quotes.toscrape.com/")
soup=BeautifulSoup(page_to_scrape.text,"html.parser")
quotes=soup.find_all("span", attrs={"class":"text"})
authors=soup.find_all("small", attrs={"class":"author"})

file=open("scraped_quotes.csv","w")
writer=csv.writer(file)
writer.writerow( ["quotes","authors"])

for quote, auther  in zip (quotes, authors):
    print(quote.text+ "-"+ auther.text)
    writer.writerow([quote.text, auther.text])

