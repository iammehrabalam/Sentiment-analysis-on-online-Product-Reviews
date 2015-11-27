import bottlenose
import requests
from bs4 import BeautifulSoup
from lxml import etree
import config as ke

'''
About This Amazon Api
---------------------

In search you must have to specify Search Index  eg: search_index = "Books"
and in query you type Keywords

Maximum Number of results you get is 100 or 10 page of size 10 products.
When Search Index is all than you get is 50 or 5 page of size 10 products
 ( This restriction is provided by Amazon )


'''


class Amazon(object):
    def __init__(self):
        self._api = bottlenose.Amazon(ke.AMAZON_ACCESS_KEY_ID,
                                      ke.AMAZON_ACCESS_SECRET_KEY,
                                      ke.AMAZON_ASSOCIATE_TAG, Region="US",
                                      Version='2013-08-01')
        self.results = []
        self.reviews = []
        self.count = 0

    def _scrap_reviews(self, soup):
        '''
        soup: BeautifulSoup object
        '''
        css = ["a-section review", "a-row", "a-icon-alt",
               "a-size-base review-text"]
        reviews = []
        try:
            for review in soup.findAll('div',
                                       attrs={"class": css[0]}):
                rows = review.findAll('div', attrs={"class": css[1]})
                temp = []
                rating = rows[1].findAll('span', attrs={"class": css[2]})
                temp.append(rating[0].text)
                single_review = rows[4].findAll('span',
                                                attrs={"class": css[3]})
                temp.append(single_review[0].text)
                reviews.append(temp)
                self.count = self.count + 1
                if self.total_reviews <= self.count:
                    break
        except:
            pass
        return reviews

    def _handle_review_urls(self):
        for product in self.results:
            try:
                next_url = product["reviews_url"]
                print next_url
                while True:
                    try:
                        response = requests.get(next_url)
                        soup = BeautifulSoup(response.text)
                        self.reviews = self.reviews + self._scrap_reviews(soup)
                        self.count = self.count + 1
                        if self.total_reviews <= self.count:
                            break
                        next_url = soup.findAll('li',
                                                attrs={"class": "a-last"})[0]
                        next_url = next_url.find('a').get('href')
                        next_url = "http://www.amazon.com/" + next_url
                    except:
                        break
            except:
                pass
            if self.total_reviews <= self.count:
                break

    def _get_items(self, response):

        '''
        Input:
        -----
        response: object of etree.fromstring

        '''
        xp = ke.AMAZON_XPATH
        for item in response.xpath(xp["_items"]):
            try:
                data = {}
                data['id'] = item.find(xp["id"]).text
                data["image_url"] = item.find(xp["image_url"]).text
                data["name"] = item.find(xp["product_name"]).text
                for itemlink in item.xpath(xp["reviews_url"]):
                    if itemlink.find("Description").text == \
                            "All Customer Reviews":
                        data['reviews_url'] = itemlink.find("URL").text
                        break
                self.results.append(data)
            except:
                pass
        self._handle_review_urls()

    def search(self, query='Mobile', search_index="All",
               res_group="Images,ItemAttributes", total_reviews=5):
        '''
        input:
        -----
        query: Query string like iphone mobile, python books
        search_index: Amazon search index name  (see config.py)
        total_reviews: No. of reviews to get

        Output:
        ------
        return two list first one contain reviews and other contain
               corresponding ratings
        '''

        self.total_reviews = total_reviews
        for page in xrange(0, 10):
            if search_index == "All":
                response = self._api.ItemSearch(Keywords=query,
                                                SearchIndex=search_index,
                                                ResponseGroup=res_group,
                                                ItemPage=page + 1)
            else:
                response = self._api.ItemSearch(Keywords=query,
                                                SearchIndex=search_index,
                                                ResponseGroup=res_group,
                                                ItemPage=page + 1,
                                                MaximumPrice=1000000,
                                                MinimumPrice=0)
            response = response.replace(' xmlns="http://webservices.'
                                        'amazon.com/AWSECommerce'
                                        'Service/2013-08-01"', '')
            response = etree.fromstring(response)
            if response.xpath("Items/Request/Errors"):
                pass
            if self.total_reviews <= self.count:
                break
            print response
            self._get_items(response)
        rate = []
        rev = []
        for i in self.reviews:
            rating = float(i[0].split()[0])
            rate.append(rating)
            rev.append(i[1])
        return rev, rate
