import json
import urllib2

__author__ = 'JI'
import xml.etree.ElementTree as ET


def getLoc(counName):
    url = "https://restcountries.eu/rest/v1/name/" + counName
    response = urllib2.urlopen(url)
    parse_json = json.loads(response.read())
    for country in parse_json:
        return country['latlng']


tree = ET.parse('sample.xml')
root = tree.getroot()
i = 0
year = '0'
origin_country = '-1'
dest_country = '0'

# get the num of ppl
for country in root.findall('record'):
    origin_country = country[1].text
    dest_country = country[0].text
    origin_lati = 'NA'
    dest_lati = 'NA'

    if getLoc(origin_country)[0]:
        origin_lati = '[' + (str)(getLoc(origin_country)[0]) + ',' + (str)(getLoc(origin_country)[1]) + ']'

    if getLoc(dest_country)[0]:
        dest_lati = '[' + (str)(getLoc(dest_country)[0]) + ',' + (str)(getLoc(dest_country)[1]) + ']'

    if year is not country[2].text:
        year = country[2].text
        print('----Year ' + year + '----')
    print('From:' + origin_country + ' to ' + dest_country)
    print('Number of ppl: ' + country[3].text)
    print('latitude: from ' + origin_lati + ' to ' + dest_lati + '\n')
