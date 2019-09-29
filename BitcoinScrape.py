from selenium import webdriver
import requests
import bs4
import csv
from matplotlib import pyplot
import pandas

dateList = []
highPriceList = []
lowPriceList = []


r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20190920&end=20190926')

#Parse the Data
soup = bs4.BeautifulSoup(r.text, "lxml")

tr = soup.find_all('tr',{'class':'text-right'})

#Get data
for item in tr:
    dateList.append(item.find('td',{'class':'text-left'}).text)      
    highPriceList.append(item.find_all('td')[2].text)                
    lowPriceList.append(item.find_all('td')[3].text) 


row0=['Date', 'High', 'Low']
rows = zip(dateList,highPriceList,lowPriceList)

# Write to CSV File
with open('bitcoinPrice.csv', 'w',encoding='utf-8',newline='') as csvfile:
    links_writer=csv.writer(csvfile)
    links_writer.writerow(row0)
    for item in rows:
        links_writer.writerow(item)


# Plot Data
data = pandas.read_csv('bitcoinPrice.csv')
pyplot.plot(data.Date, data.High)
pyplot.plot(data.Date, data.Low)
pyplot.legend(['High Price', 'Low Price'])
pyplot.xlabel('Date')
pyplot.ylabel('Price')
pyplot.title('Bitcoin Price, High Vs Low')
pyplot.show()