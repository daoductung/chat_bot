import requests
import bs4


def crawl_point(nam):
    js = {}
    url = 'https://diemthi.tuyensinh247.com/diem-chuan/dai-hoc-su-pham-ky-thuat-hung-yen-SKH.html?y=' + str(nam)
    response = requests.get(url)
    html = response.content

    soup = bs4.BeautifulSoup(html, "lxml")
    for link in soup.find_all('table'):
        for tr in link.find_all('tr')[1:2]:
            if tr.get_text().strip() != '':
                js['DH'] = tr.find_all('td')[4:6][0].get_text()
                js['THPT'] = tr.find_all('td')[4:6][1].get_text()

    return js


print(crawl_point(2019))
