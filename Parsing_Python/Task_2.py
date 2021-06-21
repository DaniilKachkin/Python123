import requests as req
import xmltodict as xml

r = req.get('http://www.cbr.ru/scripts/XML_daily.asp')
n = xml.parse(r.text)

for i in n['ValCurs']['Valute']:
    if i['Name'] == 'Японских иен':
        print('Курс рубля номиналом в', i['Nominal'], 'руб. равен:', i['Value'], i['Name'])

