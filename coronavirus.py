import requests
from bs4 import BeautifulSoup as bs

def nCov():
    happen = ['Проведено тестов: ', 'заболевших: ', 'за последние сутки: ', 'выздоровело: ', 'умерло: ']
    i = 0
    result = []

    url = 'https://стопкоронавирус.рф'

    source_code = requests.get(url)
    html = bs(source_code.text, 'html.parser')
    countdown = html.find_all('div', {"class": "cv-countdown"})
    
    for info in countdown:
        stat = info.find_all('span')
        for data in stat:
    	    result.append(happen[i] + str(data)[6:-7].replace('&gt;', '>'))
    	    i += 1
    return (str(result)[2:-2]).replace("\', \'", '\n')