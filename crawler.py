from lxml import html
import requests


class AppCrawler:
    def __init__(self, starting_url, depth):
      self.starting_url = starting_url
      self.depth = depth
      self.apps = []
    
    def crawl(self):
        self.get_app_from_url(self.starting_url)
        return 
    
    def get_app_from_url(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)
        name = tree.xpath('//div[@class="code-block code-block-3"]/ul[@class="bs-shortcode-list list-style-star"]/li/text()')[0]
        country = tree.xpath('//div[@class="code-block code-block-2"]/ul[@class="bs-shortcode-list list-style-edit"]/li/text()')[1]
        level = tree.xpath('//div[@class="code-block code-block-2"]/ul[@class="bs-shortcode-list list-style-edit"]/li/text()')[3]
        advantage = tree.xpath('//div[@class="code-block code-block-2"]/ul[@class="bs-shortcode-list list-style-edit"]/li/text()')[5]
        deadline = tree.xpath('//div[@class="code-block code-block-2"]/ul[@class="bs-shortcode-list list-style-edit"]/li/text()')[6]
        description = tree.xpath('//div[@class="code-block code-block-4"]/p/text()')
        link_apply = tree.xpath('//a[@class="button"]/@href')[0]
        link_official = tree.xpath('//a[@class="button"]/@href')[1]
        descrip = ''
        for li in range(0, len(description)):
            descrip = descrip + description[li]
        print(link_apply)
        print(link_official)
        return
    
    
class App:
    
    def __init__(self, name, description, level, advantage, links):
        self.name = name
        self.description = description
        self.level = level
        self.advantage = advantage
        
    def __str__(self):
        return ("name: " + self.name + "developper: " + self.developper + "price : " + self.price)
    
crawler = AppCrawler('https://bourses-etudes.net/bourses-university-of-hertfordshire-royaume-uni-2021/', 0) 

crawler.crawl()   

for app in crawler.apps:
    print("her we are")