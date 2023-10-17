# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class TutoCnrsItem(Item):
    # define the fields for your item here like:
    title = Field()
    kind = Field()
    body = Field()
    section_number = Field()
    page_number = Field()
    url_rel = Field()
    url_full = Field()
