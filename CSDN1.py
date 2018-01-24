from lxml import etree
import requests
import MySQLdb

db = MySQLdb.Connection(
    host = '127.0.0.1',
    database = 'blog',
    user = 'root',
    password = 'qw13198321328',
    charset = 'utf8'
)


article_category = '前端'
url = 'https://www.csdn.net/'
html = requests.get(url)
content = html.text
selector = etree.HTML(content)
html_href = selector.xpath('//h2[@class="csdn-tracking-statistics"]/a/@href')
for url in html_href:
    html1 = requests.get(url)
    content1 = html1.text
    selector = etree.HTML(content1)
    title = selector.xpath('//h1[@class="csdn_top"]')
    if title:
        title = title[0].xpath('string(.)')
        content_selector = selector.xpath('//div[@id="article_content"]')
        content = content_selector[0].xpath('string(.)').strip()
        #content = '萨摩耶乘地铁出走'
        cur = db.cursor()
        sql = "insert into articles(article_category,article_title,article_content) VALUES ('%s','%s','%s')" %(article_category,str(title),str(content))
        cur.execute(sql)
        db.commit()
cur.close()
db.close()
        #print(content)
        #print(
        # str(title))
        #print(url,content)
