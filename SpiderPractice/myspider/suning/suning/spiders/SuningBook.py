import scrapy


class SuningbookSpider(scrapy.Spider):
    name = 'SuningBook'
    allowed_domains = ['book.suning.com']
    start_urls = ['https://list.suning.com/1-502687-0.html']

    def parse(self, response):  # 数据起始方法，接收下载中间件传过来的response
        # 处理start_urls地址对应的响应
        # res = response.xpath("//div[@id='filter-results']/ul/li[1]/div/div/div/div[2]/p[2]/a/text()").extract()
        # res = response.xpath("//*[@id='filter-results']//p[2]//a/text()").extract()
        # print(res)

        # 分组
        li_list = response.xpath("//div[@id='filter-results']/ul/li")
        for li in li_list:
            item = {"store": li.xpath(".//p[@class='seller oh no-more ']/a/text()").extract_first(),
                    "title": li.xpath(".//p[@class='sell-point']/a/text()").extract_first().strip()}
            yield item  # 循环内yield，减少内存占用
