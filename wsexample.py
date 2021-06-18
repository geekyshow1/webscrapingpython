from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/cameras/dslr-mirrorless/pr?sid=jek,p31,trv&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_dedd804b-6298-4b36-85fa-dc56fbf15780_1_372UD5BXDFYS_MC.0KU83APBTPQK&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Electronics~Cameras%2B%2526%2BAccessories~DSLR%2B%2526%2BMirrorless_0KU83APBTPQK&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=0KU83APBTPQK"

response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

titles = []
prices = []
images = []

for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
 title = d.find('div', attrs={'class':'_4rR01T'})
 # print(title.string)

 price = d.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
 # print(price.string)

 image = d.find('img', attrs={'class':'_396cs4 _3exPp9'})
 # print(image.get('src'))

 titles.append(title.string)
 prices.append(price.string)
 images.append(image.get('src'))

print(titles)
print(prices)
print(images)