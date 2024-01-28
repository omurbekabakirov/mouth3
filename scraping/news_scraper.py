import requests
from parsel.selector import Selector


class NewsScraper:
    START_URL = "https://knews.kg"
    URL = "https://knews.kg/wp-includes/js/jquery/jquery.js?ver=3.7.1"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    LINK_XPATH = '//div[@class="td-module-thumb"]/a/@href'


    def parse_data(self):
        text = requests.get(url=self.URL, headers=self.HEADERS).text
        tree = Selector(text=text)
        links = tree.xpath(self.LINK_XPATH).extract()
        for link in links:
            print(self.START_URL + link)
        return links


if __name__ == '__main__':
    scraper = NewsScraper()
    scraper.parse_data()

