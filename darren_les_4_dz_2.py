import requests
from bs4 import BeautifulSoup
url = 'https://minfin.com.ua/currency/nbu/'

currency_rates = requests.get(url)
main_text = currency_rates.text
soup = BeautifulSoup(main_text, 'html.parser')

table = soup.find('table', {'class' : 'table-auto'})
tr = table.find('td', {'class' : 'responsive-hide'})
tr = tr.text

tr = tr[:7]

doll = 'Курс доллара в гривнях: ' + str(tr)
print(doll)