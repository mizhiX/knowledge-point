import requests
from fake_useragent import UserAgent
from lxml import etree


def show_ip(url, headers):
    i = 1
    while i == 1:
        proxy = input('请输入ip及端口号\n: ')
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy
        }
        try:
            html = requests.get(url, headers=headers, proxies=proxies, timeout=2).text
            response = etree.HTML(html)
            ip = response.xpath('//span[@class="c-gap-right"]/text()')[0]
            # print(ip)
            address = response.xpath('//span[@class="c-gap-right"]/../text()')[1].strip()
            # print(address)
            ip_address = ip[2:] + '  ' + address
            print(ip_address)
            i = option(i)

        except requests.exceptions.ConnectTimeout:
            print('ip地址无效!')
            i = option(i)


def option(i):
    while i == 1:
        option_number = input('是否继续?\n1.继续\n2.退出\n: ')
        if option_number == '1':
            return 1
        elif option_number == '2':
            print('退出成功!')
            i = 0
        else:
            print('请输入正确信息!')
    if i == 0:
        return 0


def main():
    url = 'http://www.baidu.com/s?wd=ip'
    ua = UserAgent()
    headers = {'UserAgent': ua.random}
    show_ip(url, headers)


if __name__ == '__main__':
    main()
