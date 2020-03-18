# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# Extract data -> temporary containers (items) -> storing in db

from scrapy.item import Item, Field


# CARROS
class MlibreItem(Item):

    id = Field()
    link = Field()
    producto = Field()
    marca = Field()
    modelo = Field()
    version = Field()
    precio = Field()
    km = Field()
    year = Field()
    puertas = Field()
    transmision = Field()
    direccion = Field()
    placa = Field()
    color = Field()
    vendedor = Field()
    tel_contacto = Field()
    ubicacion = Field()
    info_adicional = Field()
    descripcion = Field()
    fecha_scraping = Field()


# CELULARES
class MlibreItems(Item):

    id = Field()
    link = Field()
    producto = Field()
    marca = Field()
    modelo = Field()
    estado = Field()
    precio = Field()
    vendidos = Field()
    descuento = Field()
    opiniones = Field()
    rating_vendedor = Field()
    ventas_per = Field()
    num_per = Field()
    denom_per = Field()
    clase_vendedor = Field()
    descripcion = Field()
    ubicacion = Field()
    memo_interna = Field()
    ram = Field()
    pixel_camara = Field()
    tam_pantalla = Field()
    fecha_scraping = Field()
    # cia_telefonica = Field()
    # stock = Field()
    # vendedor = Field()
    # categoria = Field()
    # subcategoria = Field()


# INMUEBLES
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


# COMPUTRABAJO
class JobItem(Item):
    link = Field()
    empresa = Field()
    puesto = Field()
    salario = Field()
    z_descripcion = Field()
    categoria = Field()


# LIBROS
class LibroItem(Item):

    a_id = Field()
    aa_link = Field()
    b_producto = Field()
    c_precio = Field()
    d_ISBN = Field()
    editorial = Field()
    formato = Field()
    g_categoria = Field()
    gg_libreria = Field()
    h_vendidos = Field()
    i_descuento = Field()
    j_opiniones = Field()
    k_rating_vendedor = Field()
    l_ventas_per = Field()
    num_per = Field()
    o_denom_per = Field()
    p_clase_vendedor = Field()
    q_ubicacion = Field()
    z_fecha_scraping = Field()
