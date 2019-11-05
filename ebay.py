#!/usr/bin/env python3

def main(filename = 'inventory.csv'):
    (items, budget) = get_csv(filename)
    for item in items:
        link = make_url(item)
        limit = float(budget[items.index(item)])
        print('\nITEM NAME: ' + item)
        print('\nLINK: ' + link)
        print('BUDGET LIMIT FOR THIS ITEM: $' + str(limit) + '\n')
        sortedResult = ebay_scrape(link, limit)
        if(len(sortedResult) == 0):
            print("No results found for " + item)
        for result in sortedResult:
            print('Name: ', result[0])
            print("Shipping: $" + result[1])
            print("Price : $" + result[2])
            print("Total: $" + str(result[3]))
            print("--------------------------------------------------\n")
        print('\n==================================================\n\n')

def get_csv(filename):
    import csv
    try:
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            items = []
            budget = []
            for row in readCSV:
                items.append(row[0])
                budget.append(row[1])
    except:
        print("Error")
    return items, budget

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def make_url(item):
    base_url = ('https://www.ebay.com/sch/i.html?_from=R40&_nkw=')
    new_item = None    
    item = item.replace(' ', '+')
    new_item= base_url + item
    return new_item

def ebay_scrape(url, limit):
    import requests
    import re
    from operator import itemgetter
    from bs4 import BeautifulSoup
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    resultArray = []
    for division in soup.find_all("div", {"class": "s-item__wrapper"}):
        name = division.find("h3", {"class": "s-item__title"}).get_text(separator=u" ")
        price = division.find("span", {"class": "s-item__price"}).get_text()
        shipping = division.find("span", {"class": "s-item__shipping"}).get_text()
    
        if (hasNumbers(shipping[0])):
            strShipping = re.findall("\d+\.\d+", shipping)[0]            
        else:
            strShipping = '0.0'

        strPrice = re.findall("\d+\.\d+", price)[0]
        floatShipping = float(strShipping)
        floatPrice = float(strPrice)

        totalPrice = floatShipping + floatPrice
        
        if(limit > totalPrice):
            object = [name, strShipping , strPrice, totalPrice]
            resultArray.append(object)
            # resultArray.append(totalPrice)
            # print("Name: " + name)
            # print("Shipping: $" + strShipping)
            # print("Price : $" + strPrice)
            # print("Total: $" + str(totalPrice))
            # print("--------------------------------------------------\n")
    sortedResult = sorted(resultArray, key=itemgetter(3))
    return sortedResult

main()