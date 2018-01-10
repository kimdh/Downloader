"""
packtpub 무료책을 자동으로 받아오기
"""
import http.cookiejar
import re
import sys
import urllib

import requests
from bs4 import BeautifulSoup


def getbook(email, password):
    """ geturl and getbook """
    print("free-learing 주소를 얻어 오는 중...")
    base_url = "https://www.packtpub.com/"
    authentication_url = "https://www.packtpub.com/packt/offers/free-learning"
    header = {'User-Agent': 'Mozilla/5.0'}
    req = requests.post(authentication_url, headers=header)
    req.encoding = 'utf-8'

    # 무료책 받는 url 찾기
    bs4_packt = BeautifulSoup(req.text, "html.parser")
    get_book_url = base_url + str(bs4_packt.find('a', attrs={'class': 'twelve-days-claim'})['href'])
    print(get_book_url)

    # Cookie 를 저장
    ckj = http.cookiejar.LWPCookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(ckj))
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    # 정보입력
    value = {
        'op': 'Login',
        'email': email,
        'password': password,
        'form_id': 'packt_user_login_form'
    }

    print('책 얻어오는 중...' + get_book_url)
    data = urllib.parse.urlencode(value).encode("utf-8")
    opener.open(authentication_url, data)
    opener.open(get_book_url)


if __name__ == "__main__":
    print('packtpub 무료책을 자동으로 받아오기')

    # 사용자정보
    USER_EMAIL = input("email 을 입력해 주세요.\n")

    # email 형식 체크
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if not EMAIL_REGEX.match(USER_EMAIL) or USER_EMAIL == "":
        print('email 형식이 틀렸습니다..')
        sys.exit(1)
    USER_PASS = input('비밀번호를 입력해 주세요.\n')

    getbook(USER_EMAIL, USER_PASS)
    print("완료 되었습니다.")
