import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()

apiKey = 'MbNWQfHAsg9gatULkp04nACdeqPBrJqihYNQSEWo'

def fetchMars():
  URL_APOD = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?"
  date = '2022-10-10'
  tags = {
      'api_key':apiKey,
      'earth_date':date,
      'hd':'True'
  }
  query = requests.get(URL_APOD, params=tags).json()
  answer = (query)
  return answer['photos'][:3]
fetchMars()
