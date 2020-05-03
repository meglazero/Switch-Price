from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from time import sleep
import random

walmart = [
    'https://www.walmart.com/ip/Nintendo-Switch-Bundle-with-Mario-Kart-8-Deluxe-Gray/391444954',
    'https://www.walmart.com/ip/Nintendo-Switch-Console-with-Gray-Joy-Con-Zelda-Bundle/385350311',
    'https://www.walmart.com/ip/Nintendo-Switch-Gaming-Console-Neon-Blue-and-Neon-Red-Joy-Con/839855732',
    'https://www.walmart.com/ip/Nintendo-Switch-Eevee-Edition-Bundle/996499558',
    'https://www.walmart.com/ip/Wireless-Legend-Nintendo-Memory-Bundle-Nintendo-Micro-Pro-SD-Neon-Console-Zelda-Joy-con-64GB-Blue-Controller-The-32GB-Card-Red-4-Switch-Extra-Swtich-/909214805',
    'https://www.walmart.com/ip/Nintendo-Switch-Console-with-Gray-Joy-Con/994790027',
    'https://www.walmart.com/ip/Wireless-Nintendo-Memory-Bomberman-Bundle-Nintendo-Micro-Pro-SD-R-Console-Joy-con-64GB-Gray-32GB-Card-4-Switch-Extra-Swtich-items-Controller-Super/809049588',
    'https://www.walmart.com/ip/Wireless-Legend-Nintendo-Memory-Bundle-Nintendo-Micro-Pro-SD-Console-Zelda-Joy-con-64GB-Gray-Controller-The-32GB-Card-4-Switch-Extra-Swtich-items/336276217',
    'https://www.walmart.com/ip/Nintendo-Switch-Gaming-Console-with-Gray-Joy-Con/925458955',
    'https://www.walmart.com/ip/Nintendo-Switch-Gaming-Console-with-Neon-Blue-and-Neon-Red-Joy-Con/215355362'
]

target = [
    'https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con/-/A-77464001',
    'https://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-77464002',
    'https://www.target.com/p/nintendo-switch-mario-kart-8-deluxe-bundle-with-gray-joy-con/-/A-78590208',
    'https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con-discontinued-by-manufacturer/-/A-52189185',
    'https://www.target.com/p/nintendo-switch-with-gray-joy-con-discontinued-by-manufacturer/-/A-52052007'
]

bestBuy = [
    'https://www.bestbuy.com/site/nintendo-switch-32gb-console-gray-joy-con/6364253.p?skuId=6364253',
    'https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255',
    'https://www.bestbuy.com/site/combo/nintendo-switch-consoles/9a9bf66d-e475-47bc-8860-7c44535f323e',
    'https://www.bestbuy.com/site/combo/nintendo-switch-consoles/8cfdae25-e006-446b-9433-1e7496c3dc75',
    'https://www.bestbuy.com/site/combo/nintendo-switch-consoles/5367bef9-f278-45de-b749-3cdd6aad2156',
    'https://www.bestbuy.com/site/combo/nintendo-switch-consoles/50fd30b0-690e-4cee-b87e-8f09ad1f85d7'
]

elecExpress = [
    'https://www.electronicexpress.com/catalog/72927/nintendo-switch-blue-red-ninswitchblu',
    'https://www.electronicexpress.com/catalog/72597/nintendo-switch-gray-ninswitchgry',
    'https://www.electronicexpress.com/catalog/189463/nintendo-switch-animal-crossing-bundle',
    'https://www.electronicexpress.com/catalog/189582/nintendo-ninswitchsons-nintendo-switch-gray-controllers-team-sonic-racing',
    'https://www.electronicexpress.com/catalog/188304/nintendo-switch-gray-mariokart8'
]

amazon = [
    'https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy‑/dp/B07VGRJDFY/',
    'https://www.amazon.com/Nintendo-Switch-Gray-Mario-Deluxe-Download/dp/B07YZQSC5Y/',
    'https://www.amazon.com/Nintendo-Switch-Super-Mario-Deluxe-Download/dp/B081PPW52P/',
    'https://www.amazon.com/Nintendo-Switch-Neon-Mario-Deluxe-Download/dp/B07YZQ9QMD/',
    'https://www.amazon.com/Nintendo-Switch-Neon-Red-Blue-Joy/dp/B01MUAGZ49/',
    'https://www.amazon.com/Nintendo-Switch-Console-Bundle-Pikachu-Pokemon/dp/B07H9HDDK7/',
    'https://www.amazon.com/Nintendo-Switch-Console-Mario-Kart-Deluxe/dp/B07JJLLFXJ/',
    'https://www.amazon.com/Nintendo-Switch-Gray-Joy/dp/B01LTHP2ZK/',
    'https://www.amazon.com/Nintendo-Switch-32GB-Console-Neon-Joy/dp/B01N2BH02P/',
    'https://www.amazon.com/Nintendo-Switch-Console-Gray-Joy/dp/B01MFADJFV/',
    'https://www.amazon.com/Nintendo-Switch-Neon-Blue-Red-Joy/dp/B071LCFLH6/',
    'https://www.amazon.com/Nintendo-Switch-Bundle-Mario-Credit-Carrying/dp/B082J3NL2S/',
    'https://www.amazon.com/Nintendo-Switch-System-Console-Tennis-1-2-Switch/dp/B07H44VHHQ/',
    'https://www.amazon.com/Nintendo-Switch-items-Bundle-Joy/dp/B0773D1GWV/',
    'https://www.amazon.com/Nintendo-Switch-Super-Mario-Odyssey/dp/B075N7RDTM/',
    'https://www.amazon.com/Nintendo-Switch-Console-Bundle-Pikachu-Pokemon/dp/B07H9HH4VS/',
    'https://www.amazon.com/Nintendo-Switch-Deluxe-Accessories-Bundle/dp/B07KSSR2ZF/',
    'https://www.amazon.com/Nintendo-Switch-Fortnite-Double-Console-Bundle/dp/B07H2PG89M/',
    'https://www.amazon.com/dp/B07HCTJC91/',
    'https://www.amazon.com/Nintendo-Switch-Console-Super-Mario-Bundle/dp/B07N6HP6QN/',
    'https://www.amazon.com/Nintendo-Swtich-items-Bundle-Joy/dp/B06XJ59HM7/'
]

amazon_xpath= [
    '/html/body/div[2]/div[2]/div[9]/div[5]/div[1]/div[2]/div/div/div/form/div/div[1]/div/div/div/div[1]/div/div/div/div/span',
    '/html/body/div[2]/div[2]/div[6]/div[5]/div[1]/div[2]/div/div/div/div/div/form/div/div[1]/div/div/div/div[1]/div/div/div/div/span',
    '//*[@id="priceblock_ourprice"]',
    '//*[@id="priceblock_ourprice"]',
    '//*[@id="priceblock_ourprice"]',
    '//*[@id="priceblock_ourprice"]',
    '//*[@id="priceblock_ourprice"]',
    '/html/body/div[2]/div[2]/div[6]/div[5]/div[1]/div[2]/div/div/div/div/div/form/div/div[1]/div/div/div/div[1]/div/div/div/div/span',
    '//*[@id="priceblock_ourprice"]',
    '//*[@id="priceblock_ourprice"]',
    '//*[@id="priceblock_ourprice"]',
    '/html/body/div[2]/div[2]/div[6]/div[4]/div[1]/div[2]/div/div/div/div/div/form/div/div/span[2]/span/div/span',
    '//*[@id="priceblock_ourprice"]',
    '//*[@id="priceblock_ourprice"]',
    '//*[@id="priceblock_ourprice"]',
    '/html/body/div[2]/div[2]/div[6]/div[5]/div[1]/div[2]/div/div/div/div/div/form/div/div/span[2]/span/div/span',
    '/html/body/div[2]/div[2]/div[6]/div[4]/div[1]/div[2]/div/div/div/div/div/form/div/div[1]/div/div/div/div[1]/div/div/div/div/span',
    '/html/body/div[2]/div[2]/div[6]/div[4]/div[1]/div[2]/div/div/div/div/div/form/div/div/span[2]/span/div/span',
    '/html/body/div[2]/div[2]/div[6]/div[4]/div[1]/div[2]/div/div/div/div/div/form/div/div/span[2]/span/div/span',
    '/html/body/div[2]/div[2]/div[6]/div[4]/div[1]/div[2]/div/div/div/div/div/form/div/div/span[2]/span/div/span',
    '//*[@id="priceblock_ourprice"]'
]

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options)

# url = 'https://www.whoishostingthis.com/tools/user-agent/'

# amazRand = round(random.random() * (len(amazon) - 1))
# url = amazon[amazRand]

#---------------------
# url = bestBuy[2]
# driver.get(url)
# sleep(2)
#---------------------

# response = requests.get(url, timeout=5)
# content = BeautifulSoup(response.content, "html.parser")

# title = content.find('span', attrs={'id': 'productTitle'})
# price = content.find('span', attrs={'class': 'offer-price'})
# oos = content.find('section', attrs={'class': 'product-availability'})

#---------------------------------------------------------------------------------------------------------------------------------
# try:
#     print(url)
#     title = driver.find_element_by_xpath('/html/body/div[4]/main/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/h1')
#     title = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[1]/div[1]/div/div/div[1]/h1')
#     print(title.text.strip())
#     price = driver.find_element_by_xpath('/html/body/div[4]/main/div[1]/div[3]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div/span[1]')
#     price = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/span[1]')
#     try: 
#         print(price.text.strip('$'))
#     except:
#         print(price.text)
#     oos = driver.find_element_by_xpath('/html/body/div[4]/main/div[1]/div[3]/div[2]/div/div/div[8]/div[1]/div/div/button')
#     oos = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[3]/div[1]/div/div/button')
#     print(oos.text.strip())
# except:
#     # print(driver.find_element_by_tag_name('title').text)
#     print('Failed for some reason')
#---------------------------------------------------------------------------------------------------------------------------------

for w in walmart:
    url = w
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    title = content.find('h1', attrs={'class': 'prod-ProductTitle'}).text
    price = content.find('span', attrs={'class': 'price-characteristic'}).text + '.' + content.find('span', attrs={'class': 'price-mantissa'}).text
    print(url)
    title = title.strip()
    print(title)
    try:
        price = price.strip('$')
    except:
        price = price.strip()
    print(price)

    if float(price) < 350.00:
        print('Good to purchase')
    else:
        print('Too expensive')

    sleep(5)

for e in elecExpress:
    url = e
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    title = content.find('span', attrs={'id': 'pdp-description'}).text
    price = content.find('span', attrs={'id': 'pdpValue'}).text
    oos = content.find('section', attrs={'class': 'product-availability'}).text

    print(url)
    title = title.strip()
    print(title)
    try:
        price = price.strip('$')
    except:
        price = price.strip()
    print(price)

    oos = oos.strip()
    print(oos)

    if float(price) < 350.00 and oos != 'Out of Stock':
        print('Good to purchase')
    else:
        print('Too expensive or out of stock')

    sleep(5)

i = 0
for a in amazon:
    url = a
    driver.get(url)

    sleep(2)

    try:
        print(url)
        title = driver.find_element_by_xpath('//*[@id="productTitle"]').text
        title = title.strip()
        print(title)
        price = driver.find_element_by_xpath(amazon_xpath[i]).text
        try: 
            price = price.strip('$')
        except:
            price = price.strip()
        print(price)

        if float(price) < 350.00:
            print('Good to purchase')
        else:
            print('Too expensive')
    except:
        print(driver.find_element_by_tag_name('title').text)
        print('Failed for some reason')

    i += 1
    sleep(5)

for t in target:
    url = t
    driver.get(url)

    sleep(2)

    try:
        print(url)
        title = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div[2]/h1/span').text
        title = title.strip()
        print(title)
        price = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div[1]/div[1]/div[1]').text
        try: 
            price = price.strip('$')
        except:
            price = price.strip()
        print(price)

        oos = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[3]/div[1]/div/div/div/div[3]/div[1]/div[2]').text
        oos = oos.strip()
        print(oos)
    except:
        print('Failed for some reason')

    if float(price) < 350.00 and oos != 'Temporarily out of stock':
        print('Good to purchase')
    elif float(price) < 350.00 and oos == 'No longer available':
        print('No longer available')
    else:
        print('Too expensive or out of stock')

    sleep(5)

for b in bestBuy:
    url = b
    driver.get(url)

    sleep(2)

    try:
        print(url)

        try:
            title = driver.find_element_by_xpath('/html/body/div[4]/main/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/h1').text
        except:
            title = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[1]/div[1]/div/div/div[1]/h1').text
        title = title.strip()
        print(title)
        try:
            price = driver.find_element_by_xpath('/html/body/div[4]/main/div[1]/div[3]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div/span[1]').text
        except:
            price = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/span[1]').text
        try: 
            price = price.strip('$')
            print(price)
        except:
            price = price.strip()
            print(price)
        try:
            oos = driver.find_element_by_xpath('/html/body/div[4]/main/div[1]/div[3]/div[2]/div/div/div[8]/div[1]/div/div/button').text
        except:
            oos = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[3]/div[1]/div/div/button').text
        oos = oos.strip()
        print(oos)
    except:
        print('Failed for some reason')

    if float(price) < 350.00 and oos != 'Sold Out':
        print('Good to purchase')
    else:
        print('Too expensive or out of stock')

    sleep(5)

driver.quit()