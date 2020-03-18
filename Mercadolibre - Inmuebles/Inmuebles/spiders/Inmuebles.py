# -*- coding: utf-8 -*-
import scrapy
import re
import unidecode
from ..items import RealstateItem



# REAL STATE BOGOTA
class RealstateSpider(scrapy.Spider):

    name = 'realstateml'
    allowed_domains = ['mercadolibre.com.co']

    def start_requests(self):

        yield scrapy.Request(
            'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/acacias/_DisplayType_LF',
            self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/agrupacion-de-vivienda-los-pinos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/alcala/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/alcaparros/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/alcazar-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/alhambra/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/almendros-de-suba-suba-linda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/almendros-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/almeria-de-san-luis/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/altos-de-chozica/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/altos-del-rincon/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/andes-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/antonio-granados/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/arrayanes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/atabanza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/aticos-del-norte--colina-campestre-/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/aures/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/balcones-del-alcudia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/balcon-de-lindaraja/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/batan/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/bilbao-/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/bochalema/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/bosque-de-gratamira/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/bosque-de-la-colina/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/bosque-de-los-lagartos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/bosque-de-san-jorge/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/bosques-de-san-jorge/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/britalia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/calatayud/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/calatrava/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/calima-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/camino-verde--predio-el-cerezo--pl.-2/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/campanela/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/campania/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/cantagallo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/cantalejo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/cantalejo-sec.-alejandria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/canodromo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/casa-blanca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/casa-blanca-sec-el-plan/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/casa-blanca-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/casablanca-sector-la-gruta/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/cerros-170-s.a.-bolga/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/cerros-de-niza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/cerros-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/ciudad-hunza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/ciudad-jardin/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/ciudad-jardin-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/ciudadela-cafam/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/club-de-los-lagartos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/colina-campestre-i-y-ii-etapa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/colina-campestre-iii,-iv,-v,-vi-sector/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/colina-linda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/colina-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/colinas-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/colpatria-santa-helena/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/compartir/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/compartir--rincon-de-santa-ines-/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/conjunto-residencial-cerros-del-tabor/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/conjunto-residencial-del-monte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/costa-azul/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/covadonga/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/cordoba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/del-monte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-aguinaldo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-batan-ii-sector/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-bosque-reservado/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-carmen/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-cedro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-condado-de-iberia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-escorial-hoy-villanova/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-pinar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-pino/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-poa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-portal-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-recreo-de-los-frailes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-refugio/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-refugio-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-rincon-de-las-villas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-salitre/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/el-solar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/estoril/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/gibraltar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/gilmar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/granada-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/gratamira/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/guaymaral/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/hacienda-cordoba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/hacienda-san-sebastian-pl.-2-de-3/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/iberia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/ilarco/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/imperial/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/julio-florez/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-alameda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-britalia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-campina/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-candelaria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-colina-campestre/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-flora/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-floresta-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-floresta-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-fontana/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-hacienda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-victoria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/la-victoria-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/lagos-de-cordoba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/las-flores/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/las-mercedes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/las-orquideas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/las-terrazas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/las-villas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/libertadores/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/lindaraja/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/lisboa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/lombardia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/los-andes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/los-arrayanes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/los-naranjos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/los-nogales/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/los-nogales-de-tibabuyes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/los-portales-del-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/malibu/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/mazuren/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/mirador-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/miraflores/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/miramar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/mirandela/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/monaco/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/montealto/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/morato/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/naranjos-altos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/niza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/niza-ix/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/niza-norte-/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/niza-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/niza-sur-/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/nueva-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/nueva-tibabuyes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/nueva-zelandia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/nuevo-corinto/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/parque-los-lagartos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/parques-de-la-colina/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/pasadena/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/pinar-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/pinos-de-lombardia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/pontevedra/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/portal-de-las-mercedes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/portales-del-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/potosi/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/pradera-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/prado-jardin/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/prado-pinzon/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/prado-veraniego/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/prado-veraniego-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/prados-de-santa-barbara/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/prados-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/prados-del-salitre/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/provenza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/puente-largo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/puerta-del-sol/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/quintas-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/qumran/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/rincon-de-santa-ines/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/rincon-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/rincon-el-condor/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/rincon-escuela/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/sabana-de-tibabuyes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/salitre-/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/salitre-alto/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/san-antonio-noroccidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/san-carlos-de-tibabuyes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/san-cipriano/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/san-felipe/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/san-francisco/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/san-jorge/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/san-jose-de-bavaria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/san-jose-de-spring/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/san-jose-del-prado/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/san-nicolas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/santa-barbara-ii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/santa-carolina/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/santa-helena/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/santa-helena-de-baviera-iv-sector/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/santa-rosa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/sotileza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/spring-prado-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/suba-centro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/subata/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/tarragona/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/tejares-del-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/teusaca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/teusaquillo-de-suba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/tibabuyes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/tibabuyes-universal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/tierra-linda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/torreladera-casa-blanca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/toscana/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/tuna-alta/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/tuna-alta-el-pedregal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/turingia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/urbanizacion-torres-de-suba--san-carlos-/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/valle-refous-/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/victoria-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/villa-campestre/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/villa-cindy/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/villa-del-prado/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/villa-delia-britalia-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/villa-elisa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/villa-lucy/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/villa-maria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/suba/villa-paulina--prado-veraniego-/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/acacias-usaquen/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/alameda-170/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/altablanca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/antigua/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/balmoral-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/barrancas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/bella-suiza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/belmira/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/bosque-de-pinos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/bosque-medina/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/canaima/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/caobos-salazar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/capri/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/cedritos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/cedro-bolivar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/cedro-golf/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/cedro-narvaez/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/cedro-salazar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/chico-navarra/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/country-club/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/danubio/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/el-codito/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/el-contador/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/el-panuelito/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/el-redil/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/el-refugio-de-san-antonio/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/el-rincon-de-las-margaritas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/el-toberin/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/el-verbenal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/estrella-del-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/francisco-miranda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/ginebra/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/horizontes-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/jardin-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/la-alameda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/la-calleja/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/la-carolina/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/la-cita/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/la-esperanza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/la-floresta-de-la-sabana/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/la-liberia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/la-pradera-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/la-uribe/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/las-margaritas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/las-orquideas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/lijaca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/lisboa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/los-cedros/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/los-cedros-oriental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/maranta/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/molinos-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/montearroyo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/multicentro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/nueva-autopista/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/nuevo-country/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/nuevo-horizonte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/prados-del-country/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/recodo-del-country/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/rincon-del-chico/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/sagrado-corazon/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/san-antonio-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/san-cristobal-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/san-gabriel/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/san-patricio/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-ana/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-ana-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-ana-oriental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-barbara-oriental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-bibiana/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-barbara/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-barbara-alta/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-barbara-central/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-barbara-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-coloma/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-monica/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-paula/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/santa-teresa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/sierras-del-moral/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/tibabita/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/torcoroma/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/unicerros/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/usaquen/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/villa-magdala/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/villas-de-aranjuez/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usaquen/villas-del-mediterraneo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/antiguo-country/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/bellavista/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/bosque-calderon/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/bosque-calderon-tejada/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/cataluna/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/chapinero-alto/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/chapinero-central/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/chapinero-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/chico-alto/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/chico-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/chico-norte-ii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/chico-norte-iii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/chico-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/chico-reservado/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/el-castillo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/el-chico/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/el-nogal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/el-refugio/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/el-retiro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/emaus/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/granada/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/ingemar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/la-cabrera/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/la-salle/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/lago-gaitan/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/las-acacias/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/los-rosales/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/mariscal-sucre/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/marly/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/maria-cristina/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/nueva-granada/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/pardo-rubio/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/porciuncula/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/quinta-camacho/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/san-isidro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/san-luis-altos-del-cabo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/san-martin-de-porres/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/chapinero/sucre/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/12-de-octubre/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/baquero/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/benjamin-herrera/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/chapinero-noroccidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/colombia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/concepcion-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/el-rosario/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/entrerrios/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/jose-joaquin-vargas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/la-castellana/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/la-patria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/los-alcazares/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/los-andes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/metropolis/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/muequeta/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/polo-club/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/popular-modelo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/quinta-mutis/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/rincon-del-salitre/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/san-felipe/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/san-fernando/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/san-fernando-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/san-miguel/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/siete-de-agosto/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/barrios-unidos/simon-bolivar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/amaruc/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/andalucia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/betania/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/bosa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/bosa-centro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/brasil-ii-sector/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/chicala/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/chico-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/el-corzo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/el-porvenir/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/el-recreo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/industrial/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/la-esperanza-i/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/la-estacion/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/la-fontana-de-bosa-la-libertad/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/la-libertad/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/la-paz/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/las-margaritas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/metro-vivienda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/miraflores-iisector/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/olarte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/parcela-el-porvenir/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/piamonte-i-etapa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/porvenir-par.33/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/san-bernardino/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/san-bernardino-xxii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/san-javier/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/santa-barbara/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bosa/villa-carolina/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/bellavista/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/bogota-sector-tequendama/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/candelaria-la-nueva/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/cedritos-del-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/cooperativa-ismael-perdomo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/el-ensueno/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/el-mochuelo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/el-penon-del-cortijo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/galicia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/ismael-perdomo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/la-alameda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/la-estancia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/madelena/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/perdomo-alto/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/potosi/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/primavera-sur-occ./_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/santa-helena/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/sotavento/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/tierra-linda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/urb.-galicia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/urb.-madelena-/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/urb.-tunal-central/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/ciudad-bolivar/vista-hermosa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/acapulco/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/alameda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/alamos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/alamos-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/bellavista-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/bochica/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/bochica-ii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/bolivia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/bonanza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/bosque-popular/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/boyaca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/ciudad-bachue/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/ciudadela-colsubsidio/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/el-cedro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/el-cortijo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/el-dorado/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/el-encanto/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/el-laurel/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/el-mirador/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/el-real/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/el-refugio/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/engativa-centro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/estrada/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/florencia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/florida-blanca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/garces-navas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/gran-granada/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/granjas-el-dorado/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/la-almeria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/la-cabana/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/la-espanola/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/la-granja/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/la-serena/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/la-soledad-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/las-ferias/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/los-cerezos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/los-monjes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/los-pinos-florencia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/marandu/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/metropolis/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/minuto-de-dios/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/molinos-de-viento/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/normandia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/normandia-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/palo-blanco/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/paris/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/paris-gaitan/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/plazuelas-del-virrey/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/quirigua/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/san-antonio-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/san-joaquin/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/santa-cecilia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/santa-helenita/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/santa-maria-del-lago/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/santa-rosita/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/tabora/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/villa-gladys/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/villa-luz/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/villa-teresita/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/villas-de-granada/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/villas-de-madrigal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/villas-del-dorado/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/engativa/zarzamora/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/ambalema/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/arabia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/atahualpa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/bahia-solano/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/bohios/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/bosque-de-modelia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/capellania/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/carlos-lleras/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/centenario/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/cofradia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/el-carmen/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/el-cuco-la-estancia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/el-recodo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/el-rubi/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/el-tintal-central/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/ferrocaja/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/fontibon-centro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/hayuelos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/la-cabana/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/la-esperanza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/la-esperanza-norte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/la-felicidad/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/la-giralda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/la-laguna/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/mallorca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/modelia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/modelia-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/rincon-santo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/salamanca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/salitre-nor---occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/san-jose/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/san-pablo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/santa-cecilia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/sauzalito/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/tarragona/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/torcoroma/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/versalles/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/villemar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/fontibon/zona-franca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/abraham-lincoln/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/acip/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/agrupacion-de-vivienda-pio-xii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/agrupacion-francisco-jose-de-caldas./_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/aloha/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/alsacia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/americas-central/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/americas-occidental-i,-ii-y-iii-etapa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/andalucia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/antiguo-hipodromo-de-techo-ii-etapa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/bavaria-techo-ii-sector-,i-y-ii-etapa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/bellavista/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/boita/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/boita-ii-sector/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/bosques-de-castilla/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/britalita/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/carimagua-i-sector/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/carvajal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/casa-blanca-i-etapa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/casa-blanca-ii-etapa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/casa-blanca-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/castilla/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/catalina-ii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/ciudad-favidi/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/ciudad-kennedy/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/ciudad-kennedy-central/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/ciudad-kennedy-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/ciudad-techo-1/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/class/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/delicias/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/el-condado-de-la-paz/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/el-portal-de-las-americas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/el-rincon-de-los-angeles/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/el-tintal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/floralia-i-y-ii-sector/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/fundadores/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/gerona/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/glorieta-de-las-americas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/hipotecho/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/kennedy-norte-super-mz.11/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/la-chucua/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/la-igualdad/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/lago-timiza-i-y-ii-etapa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/las-americas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/las-margaritas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/los-almendros/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/mandalay-i-sector/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/marsella/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/multifamiliares-el-ferrol/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/nueva-marsella-i,-ii-y-iii-sector/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/nuevo-kennedy/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/parques-del-tintal-campo-alegre-londono/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/pio-xii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/roma/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/san-andres/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/santa-fe-del-tintal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/techo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/tierra-buena/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/timiza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/tintalito/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/tintalito-ii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/tintala/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/tundama/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/urbanizacion-castilla-reservado/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/urbanizacion-banderas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/urbanizacion-castilla/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/urbanizacion-castilla-la-nueva/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/urbanizacion-experimental-kennedy/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/urbanizacion-pio-xii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/valladolid/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/vereda-el-tintal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/villa-alsacia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/kennedy/villa-claudia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/alcala/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/autopista-muzu/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/bochica/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/carabelas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/ciudad-montes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/galan/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/jazmin/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/la-asuncion/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/la-guaca/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/la-pradera/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/los-sauces/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/milenta/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/muzu/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/primavera/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/puente-aranda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/san-gabriel/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/santa-isabel-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/santa-matilde/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/santa-rita/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/tejar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/puente-aranda/tibana/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/bravo-paez/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/centenario/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/cerros-de-oriente/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/claret/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/diana-turbay/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/govaroba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/guiparma/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/gustavo-restrepo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/hospital-san-carlos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/ingles/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/libertador/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/los-arrayanes-ii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/los-molinos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/marruecos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/molinos-del-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/olaya/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/palermo-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/principe-de-bochica/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/quiroga/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/san-agustin/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/san-jorge-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/san-jose-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/santa-lucia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/rafael-uribe-uribe/villa-mayor/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/20-de-julio/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/altos-del-virrey/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/buenos-aires/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/calvo-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/camino-viejo-de-san-cristobal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/cordoba/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/el-ramajal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/granada-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/la-serafina/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/la-victoria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/las-brisas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/los-alpes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/los-libertadores/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/primero-de-mayo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/quinta-ramos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/san-blas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/san-cristobal-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/san-isidro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/san-javier/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/santa-ana-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/santa-rita-i,-ii-y-iii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/santa-rita-sur-oriental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/sociego/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/velodromo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/san-cristobal-sur/villa-del-cerro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/acevedo-tejada/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/alfonso-lopez/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/armenia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/banco-central/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/belalcazar/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/campin/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/centro-narino/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/chapinero-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/ciudad-salitre-nor-oriental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/ciudad-salitre-sur-oriental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/el-recuerdo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/el-salitre/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/galerias/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/gran-america/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/la-esmeralda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/la-magdalena/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/la-soledad/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/las-americas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/nicolas-de-federman/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/nuevo-campin/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/pablo-vi/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/palermo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/quesada/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/quinta-paredes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/rafael-nunez/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/san-luis/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/santa-teresita/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/teusaquillo/teusaquillo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bogota/directo//_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/bogota/inmobiliaria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/colseguros/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/eduardo-santos/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/el-liston/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/el-progreso/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/el-vergel/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/la-estanzuela/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/la-sabana/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/paloquemao/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/ricaurte/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/samper-mendoza/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/santa-fe/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/santa-isabel/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/usatama/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/martires/veraguas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/bosque-izquierdo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/el-mirador/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/germania/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/la-alameda/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/la-capuchina/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/la-macarena/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/la-merced/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/la-paz-centro/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/las-cruces/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/las-nieves/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/lourdes/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/parque-central-bavaria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/sagrado-corazon/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/samper/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/san-bernardo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/san-diego/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/santa-fe/san-martin/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/tunjuelito/tunjuelito/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/tunjuelito/ciudad-tunal/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/tunjuelito/villa-ximena/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/tunjuelito/nuevo-muzu/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/tunjuelito/ontario/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/tunjuelito/fatima/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/tunjuelito/santa-lucia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/tunjuelito/venecia-occidental/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usme/el-porvenir/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usme/el-cortijo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usme/centro-usme/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usme/el-virrey-ultima-etapa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usme/el-portal-ii-etapa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usme/el-porvenir-ii/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usme/usminia/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usme/marichuela-ii-sector-cafam-ii-s./_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/usme/arizona/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/antonio-narino/caracas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/antonio-narino/ciudad-jardin-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/antonio-narino/san-antonio/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/antonio-narino/ciudad-berna/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/antonio-narino/restrepo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/antonio-narino/la-fraguita/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/antonio-narino/luna-park/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/antonio-narino/policarpa/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/antonio-narino/santander-sur/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/la-candelaria/las-aguas/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/la-candelaria/centro-administrativo/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/la-candelaria/candelaria/_DisplayType_LF',
        #     self.parse)
        # yield scrapy.Request(
        #     'https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/bogota-dc/la-candelaria/belen/_DisplayType_LF',
        #     self.parse)



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

        # FUNCIONES

        def getInt(value):
            try:
                return int(value.replace('.', ''))
            except Exception:
                return int(value)

        # Texto
        # Nombre vendedor
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

        # latitud y longitud
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



#     # para Barrio Bogota = response.xpath("//*[@id='id_seller_type']/dd[1]/a/@href").extract_first()
#     # response.xpath("//*[@id='id_seller_type']/dd[2]/a/@href").extract_first()
#
#     # a_list = response.css('.neighborhood_filter_name::text').extract()
#     # b_list = [i.replace(" ", "-") for i in a_list]
#     # [unidecode.unidecode(i.lower()) for i in b_list]
#
#
#     # scrapy crawl samsung --logfile spider.log
#     # scrapy crawl realstateml -s LOG_LEVEL=ERROR --logfile spider.log

