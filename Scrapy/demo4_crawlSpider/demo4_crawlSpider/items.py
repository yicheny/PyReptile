from scrapy import Field,Item

class IMGItem(Item):
    title = Field()
    url = Field()
    datetime = Field()
    source = Field()
    website = Field()
