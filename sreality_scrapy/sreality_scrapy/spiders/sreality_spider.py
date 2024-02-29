import scrapy
import json
import re
import psycopg2

class SrealitySpider(scrapy.Spider):
    """
    Spider for scraping data from the Sreality website.
    """

    name = "sreality"
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500']

    def parse(self, response, **kwargs):
        """
        Parse the response and extract the required data.

        Args:
            response (scrapy.http.Response): The response object.

        Yields:
            dict: A dictionary containing the extracted data.
        """
        response_json = json.loads(response.body)
        for flat in response_json.get('_embedded').get('estates'):
            imgs = flat.get('_links').get('images')
            yield (
                {
                    # I am getting the whole list (just in case)
                    # but I am only interested in the first element
                    'title': re.sub(r'\s', ' ', flat.get('name')),
                    'image_urls': [img.get('href') for img in imgs][0],
                }
            )