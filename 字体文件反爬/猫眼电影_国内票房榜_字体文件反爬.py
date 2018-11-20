import json
import requests
from fake_useragent import UserAgent
from lxml import etree
from fontTools.ttLib import TTFont
import re

ua = UserAgent()
url = 'http://maoyan.com/board/1'
headers = {
    'User-Agent': ua.random
}


def get_top(response):
    dl_list = response.xpath('//dl[@class="board-wrapper"]/dd')
    # print(len(dl))
    for dl in dl_list:
        # 排名
        top = dl.xpath('./i/text()')[0]
        # print(top)
        # 名称
        name = dl.xpath('.//p[@class="name"]/a/text()')[0]
        # print(name)
        # 主演
        starring = dl.xpath('.//p[@class="star"]/text()')[0]
        # print(starring)
        # 上映时间
        show_time = dl.xpath('.//p[@class="releasetime"]/text()')[0]
        # print(show_time)

        # 实时票房
        real_time_head = dl.xpath('.//p[@class="realtime"]/text()')[0].strip()
        real_time_tail = dl.xpath('.//p[@class="realtime"]/text()')[1].strip()
        real_time_number = dl.xpath('.//p[@class="realtime"]/span/span/text()')[0]
        real_time = real_time_head + real_time_number + real_time_tail
        # print(real_time)
        # 总票房
        overall_ticket_head = dl.xpath('.//p[@class="total-boxoffice"]/text()')[0].strip()
        overall_ticket_tail = dl.xpath('.//p[@class="total-boxoffice"]/text()')[1].strip()
        overall_ticket_number = dl.xpath('.//p[@class="total-boxoffice"]/span/span/text()')[0]
        overall_ticket = overall_ticket_head + overall_ticket_number + overall_ticket_tail
        # print(overall_ticket)
        yield top, name, starring, show_time, real_time, overall_ticket


# TODO 需要将所要爬取页面的字体文件保存到本地为basefonts.woff
def fonts(response_index):
    try:
        # 获取字体文件的url
        woff_ = re.search(r"url\('(.*\.woff)'\)", response_index).group(1)
        # print(woff_)
        woff_url = 'http:' + woff_
        response_woff = requests.get(woff_url, headers=headers).content
        # 将字体文件保存到本地, 每次爬取都需要保存
        with open('fonts.woff', 'wb') as f:
            f.write(response_woff)

        # baseFonts: 从网站的源代码的font-face中的url下载woff文件  并改名为basefonts.woff
        baseFonts = TTFont('basefonts.woff')
        # 用http://fontstore.baidu.com/static/editor/index.html#解析basefonts.woff文件
        # base_nums， base_fonts 需要自己手动解析映射关系， 要和basefonts.woff一致
        base_nums = ['9', '5', '6', '7', '3', '8', '4', '2', '1', '0']
        base_fonts = ['uniF59C', 'uniF65B', 'uniE3C2', 'uniECD9', 'uniE676', 'uniF7AD', 'uniF4B7', 'uniF7F7', 'uniE683', 'uniF044']
        # onlineFonts: 从get中解析出font-face的url, 并以二进制写入fonts.woff文件中
        onlineFonts = TTFont('fonts.woff')

        # onlineFonts.saveXML('test.xml')

        # 获取数字的编码
        uni_list = onlineFonts.getGlyphNames()[1:-1]
        temp = {}
        # 解析字体库
        for i in range(10):
            # 获取fonts.woff中的第i个信息
            onlineGlyph = onlineFonts['glyf'][uni_list[i]]
            for j in range(10):
                # 获取basefonts.woff中的第j个信息
                baseGlyph = baseFonts['glyf'][base_fonts[j]]
                # 如果fonts.woff的第i个信息与basefonts.woff的第j个信息相同, 就保存在temp中
                if onlineGlyph == baseGlyph:
                    # 键为f&@x加onts.woff的第i个小写信息, 值为basefonts.woff的第j个信息
                    temp["&#x" + uni_list[i][3:].lower() + ';'] = base_nums[j]
        # print(temp)
        # 字符替换
        pat = '(' + '|'.join(temp.keys()) + ')'
        response_index = re.sub(pat, lambda x: temp[x.group()], response_index)
        response = etree.HTML(response_index)
        return response
    except:
        print('解析失败!')


def with_to_file(item):
    # 注意编码
    with open('content.txt', 'a', encoding='utf8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main():
    response_index = requests.get(url, headers=headers).text
    # print(re.text)
    # 将页面的字体替换
    response = fonts(response_index)
    # 爬取页面信息
    for item in get_top(response):
        print(item)
        # 写入文件
        with_to_file(item)


if __name__ == '__main__':
    main()