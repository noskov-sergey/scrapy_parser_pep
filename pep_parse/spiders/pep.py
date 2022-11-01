import scrapy
import re

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Парсит ссылки на каждый PEP отдельно."""
        
        index = response.xpath('//*[@id="numerical-index"]').css("tbody")
        all_hrefs = index.css("a::attr(href)").getall()
        for href in all_hrefs:
            yield response.follow(href, callback=self.parse_pep)
        

    def parse_pep(self, response):
        """Парсит каждый PEP на его странице, собирает статус и имя."""

        pep = response.css("section[id='pep-content']")
        pattern = re.compile(r"^PEP\s(?P<number>\d+)[\s–]+(?P<name>.*)")
        h1_tag = pattern.search(pep.css("h1::text").get())
        if h1_tag:
            number, name = h1_tag.group("number", "name")
        context = {
            'number': number,
            'name': name,
            'status': pep.css("dt:contains('Status') + dd::text").get()
        }
        yield PepParseItem(context)
