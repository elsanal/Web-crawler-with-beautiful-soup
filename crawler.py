from lxml import html
import requests
import time

class AppCrawler:
    def __init__(self, starting_url, depth):
      self.starting_url = starting_url
      self.depth = depth
      self.current_depth = 0
      self.depth_links = []
      self.apps = []
    
    def crawl(self):
        app = self.get_app_from_url(self.starting_url)
        self.apps.append(app)
        self.depth_links.append(app.links)
        
        while self.current_depth < self.depth:
            current_links = []
            for link in self.depth_links[self.current_depth]:
                current_app = self.get_app_from_url(link)
                current_links.extend(current_app.links)
                self.apps.append(current_app)
                time.sleep(5)
            self.current_depth +=1
            self.depth_links.append(current_links)
    
    def get_app_from_url(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)
        name = tree.xpath('//div[@class="code-block code-block-3"]/ul[@class="bs-shortcode-list list-style-star"]/li/text()')[0]
        year = tree.xpath('//div[@class="code-block code-block-2"]/ul[@class="bs-shortcode-list list-style-edit"]/li/text()')[0]
        country = tree.xpath('//div[@class="code-block code-block-2"]/ul[@class="bs-shortcode-list list-style-edit"]/li/text()')[1]
        level = tree.xpath('//div[@class="code-block code-block-2"]/ul[@class="bs-shortcode-list list-style-edit"]/li/text()')[3]
        advantage = tree.xpath('//div[@class="code-block code-block-2"]/ul[@class="bs-shortcode-list list-style-edit"]/li/text()')[5]
        deadline = tree.xpath('//div[@class="code-block code-block-2"]/ul[@class="bs-shortcode-list list-style-edit"]/li/text()')[6]
        description = tree.xpath('//div[@class="code-block code-block-4"]/p/text()')
        link_apply = tree.xpath('//a[@class="button"]/@href')[0]
        link_official = tree.xpath('//a[@class="button"]/@href')[1]
        links = tree.xpath('//a[@class="post-url"]/@href')
        descrip = ''
        for li in range(0, len(description)):
            descrip = descrip + description[li]
        index = 0
        # for link in links:
        #     print("index : $index" + " link = " +link)
        #     index +=1
        app = App(name,country,year,descrip,level,advantage,link_official,link_apply,deadline,links)
        
        return app
    
    
class App:
    
    def __init__(self, name,country,year, description, level, 
                 advantage,link_official, link_apply, deadline, links):
        self.name = name
        self.country = country
        self.level = level
        self.year = year
        self.description = description
        self.advantage = advantage
        self.deadline = deadline
        self.link_official = link_official
        self.link_apply = link_apply
        self.links = links
        
    def __str__(self):
        return ("\n\nname: " + self.name + "\ncountry : " + self.country + "\nyear : " + self.year +"\nlevel : " + self.level + "deadline : " + 
                self.deadline + "\nadvantage : " + self.advantage + "\nofficial link : " + self.link_official 
                + "\napply link : " + self.link_apply + "\ndescription: " + self.description + "\n")
    
crawler = AppCrawler('https://bourses-etudes.net/bourse-africa-leadership-fund-scholarship-france-2021/', 1) 

crawler.crawl()   

newScho = open("scholarship_list.docx","w")

for app in crawler.apps:
    newScho.write(str(app))
newScho.close()    