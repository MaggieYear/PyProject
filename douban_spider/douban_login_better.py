import requests
from lxml import etree
from PIL import Image


def get_captcha(url, headers):
    data = {    # 传输数据
        'source': None,
        'redir': 'https://www.douban.com/people/177871085/',
        'form_email': '改为用户名',
        'form_password': '改为密码',
        'captcha-solution': '',
        'captcha-id': ''
        }

    req = requests.get(url=url, headers=headers)
    info = req.text

    html = etree.HTML(info)     # 获取验证码链接和ID
    captcha_solutions = html.xpath('//div[@class="item item-captcha"]/div/img/@src')
    data['captcha-id'] = html.xpath('//input[@name="captcha-id"]/@value')

    img = requests.get(captcha_solutions[0])
    with open('1.jpg', 'wb') as f:
            f.write(img.content)
    im = Image.open('1.jpg')
    im.show()
    data['captcha-solution'] = input('请输入验证码：')

    session = requests.Session()
    resp = session.post(url, data=data, headers=headers)

    return session


def get_myindex(url, session):
    req = session.get(url)
    html = req.text
    print(html)

if __name__ == '__main__':

    url = 'https://www.douban.com/accounts/login'

    agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    headers = {'User-Agent': agent}

    session = get_captcha(url, headers)
    my_url = 'https://www.douban.com/people/177871085/'
    get_myindex(my_url, session)


#
# print(resp.text)

# print(captcha_solutions)







