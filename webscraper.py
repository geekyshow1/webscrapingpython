from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/cameras/dslr-mirrorless/pr?sid=jek,p31,trv&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_dedd804b-6298-4b36-85fa-dc56fbf15780_1_372UD5BXDFYS_MC.0KU83APBTPQK&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Electronics~Cameras%2B%2526%2BAccessories~DSLR%2B%2526%2BMirrorless_0KU83APBTPQK&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=0KU83APBTPQK"

response = requests.get(url)
# print(response.status_code)
# print(response.content)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find('a'))
# print(soup.find(id="next-page-link-tag"))

# for link in soup.find_all('a'):
#  print(link.get('href'))

# for image in soup.find_all('img'):
#  print(image.get('src'))

# product = soup.find_all('div', class_='_3pLy-c row')
# print(product)

# product = soup.find('div', attrs={'class':'_3pLy-c row'})
# print(product)