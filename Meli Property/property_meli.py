
import re
import scrapy
import logging
import requests
import unidecode
from datetime import datetime
from Property.items import RealstateItem
from scrapy.http import TextResponse
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class RealstateSpider(scrapy.Spider):

    name = 'realstateml'
    allowed_domains = ['mercadolibre.com.co']

    custom_settings = {
        'FEED_URI': 'inmuebles_' + str(datetime.today().strftime('%Y-%m-%d')) + '.csv',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORTERS': {
            'json': 'scrapy.exporters.CsvItemExporter',
        },
        'FEED_EXPORT_ENCODING': 'utf-8',
        'SPIDER_MIDDLEWARES': {
            'scrapy_deltafetch.DeltaFetch': 500,
            'scrapy_magicfields.MagicFieldsMiddleware': 400,
        },
        'MAGIC_FIELDS': {
            "link": "$response:url",
            "fecha_scraping": "$time",
        },
        'MAGICFIELDS_ENABLED': True,
        'DELTAFETCH_ENABLED': True,
        'DELTAFETCH_RESET': 1,
        'EXTENSIONS': {
            'scrapy.extensions.statsmailer.StatsMailer': 500,
        },
        'STATSMAILER_RCPTS': ['******@gmail.com'],
        'MAIL_HOST': 'smtp.gmail.com',
        'MAIL_PORT': 587,
        'MAIL_USER': '*****@gmail.com',
        'MAIL_PASS': '######'
    }

    def start_requests(self):

        yield scrapy.Request(
            'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/acacias/_DisplayType_LF',
            self.parse)

    def parse(self, response):

        reals_links = response.css('div[class="image-content"] a::attr(href)').extract()
        for i in reals_links:
            url = response.urljoin(i)
            yield response.follow(url, callback=self.get_details)

        next_page = response.xpath("//li[@class='andes-pagination__button andes-pagination__button--next ']/a/@href").extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)

    def get_details(self, response):

        # Functions

        def getInt(value):
            try:
                return int(value.replace('.', ''))
            except Exception:
                return int(value)

        # Seller
        def noaccent_seller(s):
            try:
                return str(unidecode.unidecode(s))
            except Exception:
                try:
                    items = response.xpath("//p[@class='disclaimer']/text()").extract_first()
                    return str(unidecode.unidecode(items))
                except Exception:
                    return None

        def noaccent(s):
            return str(unidecode.unidecode(s))

        def info(s):
            def tostr(s):
                return ' '.join(s)
            def accent(s):
                return str(unidecode.unidecode(s))
            return accent(tostr(s))

        # latitude y longitude
        def location(s):
            result = "".join(s)
            return (result)

        # Google Maps Link
        def gmap():

            data = re.findall("var dynamicMapProperties =(.+?);\n\t", response.body.decode("utf-8"), re.S)

            p = re.compile(r'[-+]?\d*\.\d+|\d+')
            a_list = [i for i in p.findall(location(data))]
            separador = ','
            coordenadas = separador.join(a_list[::-1][-2:])

            if data:
                return ('http://www.google.com/maps/place/' + coordenadas)

        items = RealstateItem()

        items['a_Tipo_Inmueble'] = noaccent(response.xpath("normalize-space(.//*[@id='root-app']/section[1]/nav/div[1]/ul/li[2]/a/text())").extract_first())
        items['b_Opcion'] = noaccent(response.xpath("normalize-space(.//*[@id='root-app']/section[1]/nav/div[1]/ul/li[3]/a/text())").extract_first())
        items['c_Ciudad'] = noaccent(response.xpath("normalize-space(.//*[@id='root-app']/section[1]/nav/div[1]/ul/li[4]/a/span/text())").extract_first())
        items['d_Localidad'] = noaccent(response.xpath("normalize-space(.//*[@id='root-app']/section[1]/nav/div[1]/ul/li[5]/a/span/text())").extract_first())
        items['e_Barrio'] = noaccent(response.xpath("normalize-space(.//*[@id='root-app']/section[1]/nav/div[1]/ul/li[6]/a/span/text())").extract_first())
        items['f_Precio'] = getInt(response.xpath("//span[@class='price-tag-fraction']/text()").extract_first())
        items['g_Metros_Cuadrados'] = response.css(".align-surface::text").re_first(r'\d+')
        items['h_Dormitorios'] = response.css(".align-room::text").re_first(r'\d+')
        items['i_Banos'] = response.css(".align-bathroom::text").re_first(r'\d+')
        items['j_Valor_Administracion'] = response.xpath("normalize-space(.//section[@class='ui-view-more vip-section-specs main-section'])").re_first(r'administración (\d+)')
        items['k_Parqueaderos'] = response.xpath("normalize-space(.//section[@class='ui-view-more vip-section-specs main-section'])").re_first(r'Parqueaderos (\d+)')
        items['l_Antiguedad'] = response.xpath("normalize-space(.//section[@class='ui-view-more vip-section-specs main-section'])").re_first(r'Antigüedad (\d+)')
        items['m_Vendedor'] = noaccent_seller(response.xpath("//p[@class='card-description card-description--bold']/span/text()").extract_first())
        items['n_Tel_Contacto'] = info(response.css(".profile-info-phone-value::text").extract())
        items['o_Info_adicional'] = noaccent(response.xpath("normalize-space(.//section[@class='ui-view-more vip-section-specs main-section'])").re_first(r'^\w+\s+(.*)'))
        items['p_Texto'] = info(response.xpath("//div[@class='item-description__text']/p/text()").extract())
        items['q_Google_Maps'] = gmap()
        items['yy_id_publicacion'] = response.css('.item-info__id-number::text').re_first(r'\d+')

        yield items


configure_logging()
runner = CrawlerRunner()
runner.crawl(RealstateSpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()
