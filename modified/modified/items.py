from scrapy.item import Item, Field

class StarbucksItem(Item):
    sublocality = Field()
    locality = Field()
    city = Field()
    pincode = Field()
    lat = Field()
    lng = Field()
