import requests
# from bs4 import BeautifulSoup
def get_leetcode_data():
    response = requests.get('https://leetcodestats.cyclic.app/aadilsehrawat/')
    if response.status_code == 200:
        data = response.json()
        totalSolved = data.get('totalSolved')
        easySolved = data.get('easySolved')
        mediumSolved = data.get('mediumSolved')
        hardSolved = data.get('hardSolved')
        return {'totalSolved': totalSolved, 'easySolved': easySolved, 'mediumSolved': mediumSolved, 'hardSolved': hardSolved}
    else:
        return None