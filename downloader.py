"""
다운로드
"""
import sys
import urllib.parse
import urllib.request


def get_redirected_file(dori_url):
    """ get_redirected_file """
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = {'name': 'Michael Foord',
              'location': 'Northampton',
              'language': 'Python'}
    headers = {'User-Agent': user_agent}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(dori_url, data, headers)
    with urllib.request.urlopen(req) as response:
        # the_page = response.read()
        print('Redirected URL: ', response.url)
    return response.url


def report(blocknr, blocksize, size):
    """ display download progress """
    current = blocknr * blocksize
    percent = 100.0 * current / size
    if percent > 100:
        percent = 100
    sys.stdout.write("\r{0:.2f}%".format(percent))


def downloadfile(dred_url):
    fname = dred_url.split('/')[-1]
    print('Redirected FileName: ', fname)
    urllib.request.urlretrieve(dred_url, fname, report)


if __name__ == "__main__":
    UrlMap = {
        "1": "https://go.microsoft.com/fwlink/?Linkid=850640",
        "2": "http://upd.emule-security.org/ipfilter.zip",
        "3": "https://tuxproject.de/projects/vim/complete-x64.7z",
        "x": "exit"
    }
    Select = input('1. VSCode Insider\n2. ipfilter\n3. Vim builds for Windows\nx. Exit\n\n=> ')

    if Select == 'x' or not Select in UrlMap:
        sys.exit(0)
    Original_Url = UrlMap.get(Select)

    print("URL: ", Original_Url)
    Redirected_Url = get_redirected_file(Original_Url)
    downloadfile(Redirected_Url)
