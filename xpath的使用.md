# XPath解析库的使用

XPath, 全称XML Path Language, 即XML路径语言, 它是一门在XML文档中查找信息的语言, 它最初是用来搜寻XML文档的, 但它同样适用于HTML文档的搜索

## 1.XPath概览

XPath的选择功能十分强大, 它提供了非常简洁明了的路径选择表达式, 另外, 它还提供了超过100个内建函数, 用于字符串、数值、时间的匹配以及节点、序列的处理等, 几乎所有我们想要定位的节点, 都可以用XPath来选择

## 2.XPath常规规则

```python
================================================================================================
										  XPath常用规则
================================================================================================
  表 达 式										描    		述
================================================================================================
nodename					选取此节点的所有子节点
/							从当前节点选取直接子节点
//							从当前节点选取子孙节点
.							选取当前节点
..							选取当前节点的父节点
@							选取属性
================================================================================================
```

##3.准备工作

使用前确保安装好lxml:

```python
pip install lxml
```

## 4.实例

```python
from lxml import etree		#导入lxml库的etree模块
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item </a></li>
<li class="item-1"><a href="link2.html">second item </a></li>
<li class="item-inactive"><a href="link3.html">third item </a></li>
<li class="item-1"><a href="link4.html">fourth item </a></li>
<li class="item-0"><a href="link5.html">first item </a>
</ul>
</div>
'''
html = etree.HTML(text)		# 调用HTML类将文本初始化, 就构造 了一个XPath解析对象; 这里注意HTML文本中最后一个li节点是没有闭合的, 但etree模块可以自动修正HTML文本
result = etree.tostring(html)	# 调用tostring()方法即可输出修正后的HTML代码, 但结果是bytes类型, 利用decode()方法将其转成str类型
print(result.decode('utf8'))

运行结果如下:
<html><body><div>
<ul>
<li class="item-0"><a href="link1.html">first item </a></li>
<li class="item-1"><a href="link2.html">second item </a></li>
<li class="item-inactive"><a href="link3.html">third item </a></li>
<li class="item-1"><a href="link4.html">fourth item </a></li>
<li class="item-0"><a href="link5.html">first item </a>
</li></ul>
</div>
</body></html>

$ 另外, 也可以直接读取文本文件进行解析:
form lxml import etree

html = etree.parse('./text.html', etree.HTMLParser())
result = etree.tostring(html).decode('utf8')
print(result)
```

## 5.所有节点 //

```python
from lxml import etree

html = etree.HTML(text)
result = html.xpath('//*')	# 这里的*代表匹配所有节点
print(result)
li_result = html.xpath('//li') #获取所有li节点
print(li_result)
print(li_result[0])	#因为输入的是列表, 所以可以用索引取出想要的对象

运行结果如下:
[<Element html at 0x28c9bc8>, <Element body at 0x28c9b08>, <Element div at 0x28c9c08>, <Element ul at 0x28c9c48>, <Element li at 0x28c9c88>, <Element a at 0x28c9d08>, <Element li at 0x28c9d48>, <Element a at 0x28c9d88>, <Element li at 0x28c9dc8>, <Element a at 0x28c9cc8>, <Element li at 0x28c9e08>, <Element a at 0x28c9e48>, <Element li at 0x28c9e88>, <Element a at 0x28c9ec8>]
[<Element li at 0x28b9cc8>, <Element li at 0x28b9d88>, <Element li at 0x28b9e08>, <Element li at 0x28b9e48>, <Element li at 0x28b9ec8>]
<Element li at 0x28b9cc8>
```

## 6.子节点 /

```python
from lxml import etree
# 选择所有li节点的所有直接a子节点
html = etree.HTML(text)
li_result = html.xpath('//li/a')
print(li_result)
# 选择所有ul节点下的所有子孙a节点
ul_result = html.xpath('//ul//a')
print(ul_result)

运行结果如下:
[<Element a at 0x2889b08>, <Element a at 0x2889c08>, <Element a at 0x2889c48>, <Element a at 0x2889c88>, <Element a at 0x2889cc8>]
[<Element a at 0x288bb48>, <Element a at 0x288bc48>, <Element a at 0x288bc88>, <Element a at 0x288bcc8>, <Element a at 0x288bd08>]
```



##7.属性匹配 @

```python
from lxml import etree
#限制节点
html = etree.HTML(text)
result = html.xpath('//li[@class="item-0"]')
print(result)

运行结果如下:
[<Element li at 0x28c9b08>, <Element li at 0x28c9c08>]
```



## 8.父节点 ..

```python
from lxml import etree
# 首先选中href属性为link4.html的a节点, 然后再获取其父节点, 然后再获取其class属性
html = etree.HTML(text)
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

运行结果如下:
['item-1']
```



## 9.文本获取 text()

获取节点中的文本

```python
from lxml import etree

html = etree.HTML(text)
# 先选取a节点再获取文本
a_result = html.xpath('//li[@class="item-0"]/a/text()')
# 获取li节点下的所有文本信息
li_result = html.xpath('//li[@class="item-0"]//text()')
print(a_result)
print(li_result)

运行结果如下:
['first item ', 'first item ']
['first item ', 'first item ', '\n']
```



## 10.属性获取 @

获取节点的属性

```python
from lxml import etree

html = etree.HTML(text)
# 获取li节点下a节点的href属性, 并以列表形式返回
result = html.xpath('//li/a/@href')
print(result)

运行结果如下:
['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
```



## 11.属性多值匹配 contains()

contains(): 第一个参数传入@属性名称, 第二个参数传入属性值, 只要此属性包含所传入的属性值, 就可以完成匹配.

```python
from lxml import etree

text = """
<li class="li li-first"><a href="link.html">first item</a></li>
<li class="li-second"><a href="link.html">second item</a></li>
<li class="li li-third"><a href="link.html">third item</a></li>
"""
html = etree.HTML(text)
# 获取所有li节点中class属性里包含li属性值的文本
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

运行结果如下:
['first item', 'second item', 'third item']
```



## 12.多属性匹配 and

使用运算符and连接

```python
from lxml import etree

text = """
<li class="li li-first"><a href="link.html">first item</a></li>
<li class="li-second"><a href="link.html">second item</a></li>
<li class="li li-third"><a href="link.html">third item</a></li>
"""
html = etree.HTML(text)
# 获取所有li节点中class属性里包含li属性值的文本 并且 name属性值为item, 二者需要同时满足
and_result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(and_result)
# 获取所有li节点中class属性里包含li属性值的文本 name属性值为item, 二者最少满足一个
or_result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(or_result)

运行结果如下:
['first item', 'third item']
['first item', 'second item', 'third item']
```

##13.按序选择 position(), last()

```python
from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item </a></li>
<li class="item-1"><a href="link2.html">second item </a></li>
<li class="item-inactive"><a href="link3.html">third item </a></li>
<li class="item-1"><a href="link4.html">fourth item </a></li>
<li class="item-0"><a href="link5.html">first item </a>
</ul>
</div>
'''
html = etree.HTML(text)
# 选取了第一个li节点
result = html.xpath('//li[1]/a/text()')
print(result)
# 选取了最后一个li节点
result = html.xpath('//li[last()]/a/text()')
print(result)
# 选取了位置小于3的li节点
result = html.xpath('//li[position()<3]/a/text()')
print(result)
# 选取了倒数第3个li节点
result = html.xpath('//li[last()-2]/a/text()')
print(result)

运行结果如下:
['first item ']
['first item ']
['first item ', 'second item ']
['third item ']
```

