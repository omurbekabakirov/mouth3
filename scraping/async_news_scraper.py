import httpx
import asyncio
from parsel import Selector


class AsyncNewsScraper:
     START_URL = "https://knews.kg"
     URL = "https://knews.kg/"
     HEADERS = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
          'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
          'Accept-Encoding': 'gzip, deflate, br',
     }
     LINK_XPATH = '//div[@class="td-module-thumb"]/a/@href'

     async def async_generator(self, limit):
         for page in range(1, limit + 1):
             yield page

     async def get_pages(self):
         async with httpx.AsyncClient(headers=self.HEADERS) as client:
             async for page in self.async_generator(limit=3):
                 data = await self.get_url(
                     client=client,
                     url=self.URL.format(
                         page=page
                     )
                 )
                 return data

     async def get_url(self, client, url):
         response = await client.get(url=url)
         print('response-url: ', response.url)

         await self.scrape_url(response=response)

     async def scrape_url(self, response):
         tree = Selector(text=response.text)
         links = tree.xpath(self.LINK_XPATH).extract()
         for link in links:
             print(link)


if __name__ == "__main__":
     scraper = AsyncNewsScraper()
     asyncio.run(scraper.get_pages())