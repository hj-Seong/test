import requests
from bs4 import BeautifulSoup


def todayTemp():
    uri = '''
        https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8
    '''
    response = requests.get(uri)

    if(response.status_code ==200):
        soup = BeautifulSoup(response.text, 'html.parser')
        tarket = soup.select_one("#main_pack .todaytemp")
        temp = { 'today_temp' : tarket.text }
    return temp