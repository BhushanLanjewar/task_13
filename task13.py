import requests as rq

from bs4 import BeautifulSoup

bUrl = 'https://books.toscrape.com/'

bHeader = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

bResp = rq.get(url= bUrl, headers= bHeader)

bSoup = BeautifulSoup(bResp.content, 'html.parser')


all_Article_tag = bSoup.find_all('article', {'class':'product_pod'})

# # allH3 = bSoup.find('h3').find('a').attrs['title']
# # print(allH3)

# allRating = bSoup.find('p').attrs['class'][1]
# print(allRating)

# # allPrice = bSoup.find('p',{'class' : 'price_color'}).getText()
# # print(allPrice)

def numRating(num):
    if num == 'One':
        return 1
    elif num == 'Two':
        return 2
    elif num == 'Three':
        return 3
    elif num == 'Four':
        return 4
    elif num == 'Five':
        return 5
    else:
        return 0
    
bookData = []
for i in all_Article_tag:
    Title = i.find('h3').find('a').attrs['title']
    Rating = numRating(i.find('p').attrs['class'][1])
    Price = i.find('p',{'class' : 'price_color'}).getText().split('£')[1]

    bookData.append({
      'Title' : Title,
      'Rating' : Rating,
      'Price' : Price
    })

print(bookData)





