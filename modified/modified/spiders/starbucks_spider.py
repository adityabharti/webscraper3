import scrapy
from pygeocoder import Geocoder
from pygeocoder import GeocoderError
from modified.items import StarbucksItem

class StarbucksSpider(scrapy.Spider):
    name = "starbucks"
    allowed_domains = ["starbucks.in"]
    start_urls = ["http://www.starbucks.in/coffeehouse/store-locations/"]
    
    def parse(self, response):
	for sel in response.xpath('//div[@class = "region size2of3"]/*[self::strong]'):
		item = StarbucksItem()
		
    		item['sublocality'] = sel.xpath('following-sibling::div[position() = 1  and not(starts-with(., "Timings"))]/text()').extract()
		item['locality'] = sel.xpath('following-sibling::div[position() = 2 and not(starts-with(., "Timings"))]/text()').extract()
		item['city'] = sel.xpath('following-sibling::div[position() = 3]/text()').extract()
		item['pincode'] = sel.xpath('following-sibling::div[position() = 3]/text()').re('\d{6}')
		add =  "  ".join(item.strip() for item in sel.xpath('following-sibling::div[position() < 3 and not(starts-with(., "Timings"))]/text()').extract())
		try:		
		    coord = Geocoder.geocode(add)
		    item['lat'] = coord.latitude
		    item['lng'] = coord.longitude
		except GeocoderError:
		    item['lat'] = 0.0
		    item['lng'] = 0.0
		yield item

#.re(r'([A-Z])\w+|\d{6}')
