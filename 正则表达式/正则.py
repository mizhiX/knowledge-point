import re

# TODO 1.输出
'''
guoup() 方法可以输出匹配的内容
span()  方法可以输出匹配的范围
'''
print('=' * 100)
# TODO 2.match()
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)

print(result)
print(result.group())		# guoup() 方法可以输出匹配的内容
print(result.span())		# span()  方法可以输出匹配的范围
print('=' * 100)

# TODO 匹配目标
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())		# 索引为空或0输出完整的匹配结果
print(result.group(1))		# 索引从1开始 , 假如正则表达式后面还有()括上的内容, name可以依次用group(2)、group(3)等来获取, 但不能超过索引, 否则报错.
print(result.span())
print('=' * 100)

# TODO 通用匹配
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())		# 输出的是整个字符串的长度
print('=' * 100)

# TODO 贪婪与非贪婪
content= 'Hello 1234567 World_This is a Regex Demo'
"""贪婪"""
result = re.match('^He.*(\d+).*Demo$', content)
print(result.group())
"""非贪婪"""
result = re.match('^He.*?(\d+).*Demo$', content)
print(result.group(1))
print('=' * 100)

# TODO 修饰符
content = '''Hello 1234567 World_This
is a Regex Demo'''
try:
    result = re.match('^He.*?(\d+).*?Demo$', content)
    print('修饰前: ' + result.group(1))
except:
    result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
    print('修饰后: ' + result.group(1))
print('=' * 100)

# TODO 转义匹配
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result.group())
print('=' * 100)

# TODO 3.search()
html = '''
<div id="songs-list">
<h2 class="title">网络热歌</h2>
<p class="introduction">
网络热歌
</p>
<ul id="list" class="list-group">
<li data-view="2">童话镇</li>
<li data-view="7">
<a href="/2.mp3" singer="郑晓填">如果寂寞了</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="麦小兜">9420</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">文爱</a></li>
<li data-view="5"><a href="/5.mp3" singer="阿涵">过客</a></li>
<li data-view="5">
<a href="/6.mp3" singer="刘心">凭什么说</a>
</li>
</ul>
</div>
'''

result = re.search('<li.*?active.*?singer="(.*?)>(.*?)</a>', html, re.S)
print(result.group(1) + ':' + result.group(2))
print('=' * 100)

# TODO 4.findall()
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
print('=' * 100)

# TODO 5.sub()
content = '65as1dfa5e1f65ew1f613'
result = re.sub('\d+', '', content)
print(result)

html = re.sub('<a.*?>|</a>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for result in results:
    print(result.strip())
print('=' * 100)

# TODO compile()
content1 = '2018-11-11 11:11'
content2 = '2018-11-16 12:00'
content3 = '2018-11-19 00:00'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
print('=' * 100)