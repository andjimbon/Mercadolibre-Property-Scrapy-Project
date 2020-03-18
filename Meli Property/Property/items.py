# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# Extract data -> temporary containers (items) -> storing in db

from scrapy.item import Item, Field

class RealstateItem(Item):

    a_Tipo_Inmueble = Field()
    b_Opcion = Field()
    c_Ciudad = Field()
    d_Localidad = Field()
    e_Barrio = Field()
    f_Precio = Field()
    g_Metros_Cuadrados = Field()
    h_Dormitorios = Field()
    i_Banos = Field()
    j_Valor_Administracion = Field()
    k_Parqueaderos = Field()
    l_Antiguedad = Field()
    m_Vendedor = Field()
    n_Tel_Contacto = Field()
    o_Info_adicional = Field()
    p_Texto = Field()
    q_Google_Maps = Field()
    link = Field()
    yy_id_publicacion = Field()
    fecha_scraping = Field()
