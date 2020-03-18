# -*- coding: utf-8 -*-

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import pymongo
# import mysql.connector


# class CarrosPipeline(object):

# def process_item(self, item, spider):
#     return item


## MYSQL

    # def __init__(self):
    #     self.create_connection()
    #     self.create_table()
    #
    # def create_connection(self):
    #     self.conn = mysql.connector.connect(
    #         host='localhost',
    #         user='root',
    #         password='andy0827',
    #         database='celularesml')
    #
    #     self.curr = self.conn.cursor()
    #
    # def create_table(self):
    #     self.curr.execute("""create table listado_celulares(
    #         a_Id int,
    #         aa_Link text,
    #         ab_Producto text,
    #         b_Marca text,
    #         c_Modelo text,
    #         d_Estado text,
    #         e_Precio int,
    #         f_Memo_Interna text,
    #         g_RAM text,
    #         h_Pixel_camara text,
    #         j_Cia_telefonica text,
    #         k_Vendidos text,
    #         l_Descuento text,
    #         n_Opiniones text,
    #         o_Rate_Vendedor float,
    #         p_Stock int,
    #         q_Ventas_per int,
    #         qa_Num_per int,
    #         qb_Denom_per text,
    #         r_Clase_Vendedor text,
    #         s_Descripcion text,
    #         sa_Ubicacion text,
    #         z_Fecha_info date,
    #         )""")

# def process_item(self, item, spider):
    # self.store_db(items)
#     return item

    # def store_db(self, items):
    #     self.curr.execute("""insert into listado_celulares values (
    #         %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
    #
    #         items['a_Id'][0],
    #         items['aa_Link'][0],
    #         items['ab_Producto'][0],
    #         items['b_Marca'][0],
    #         items['c_Modelo'][0],
    #         items['d_Estado'][0],
    #         items['e_Precio'][0],
    #         items['f_Memo_interna'][0],
    #         items['g_RAM'][0],
    #         items['h_Pixel_camara'][0],
    #         items['j_Cia_telefonica'][0],
    #         items['k_Vendidos'][0],
    #         items['l_Descuento'][0],
    #         items['n_Opiniones'][0],
    #         items['o_Rate_Vendedor'][0],
    #         items['p_Stock'][0],
    #         items['q_Ventas_per'][0],
    #         items['qa_Num_per'][0],
    #         items['qb_Denom_per'][0],
    #         items['r_Clase_Vendedor'][0],
    #         items['s_Descripcion'][0],
    #         items['sa_Ubicacion'][0],
    #         items['z_Fecha_Info'][0]
    #     ))
    #
    #     self.conn.commit()



# Mongo DB
    # def __init__(self):
    #     self.conn = pymongo.MongoClient(
    #         'localhost',
    #         27017
    #     )
    #     db = self.conn['carrosml']
    #     self.collection = db['mlibre_tb']
    #
    # def process_item(self, item, spider):
    #     self.collection.insert(dict(item))
    #     return item
#
#
#
# POSTGRESQL
#
# import psycopg2
# import functools
# import logging
#
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import pprint
# import datetime
#
# # def check_spider_pipeline(process_item_method):
# #
# #     @functools.wraps(process_item_method)
# #     def wrapper(self, item, spider):
# #
# #         msg = '%%s %s pipeline step' % (self.__class__.__name__,)
# #
# #         # if class is in the spider's pipeline, then use the
# #         # process_item method normally.
# #         if self.__class__ in spider.pipeline:
# #             spider.log(msg % 'executing', level=logging.DEBUG)
# #             return process_item_method(self, item, spider)
# #
# #         # otherwise, just return the untouched item (skip this step in
# #         # the pipeline)
# #         else:
# #             spider.log(msg % 'skipping', level=logging.DEBUG)
# #             return item
# #
# #     return wrapper
#
#
# class CelularesPipeline(object):
#
#     def close_spider(self, spider):
#
#         from_email = "ajimenezbonilla@gmail.com"
#         to_email = "ajimenezbonilla@gmail.com"
#         msg = MIMEMultipart()
#         msg['From'] = from_email
#         msg['To'] = to_email
#         msg['Subject'] = 'Scraper Report for ' + datetime.date.today().strftime("%m/%d/%y")
#         intro = "Summary stats from Scrapy spider: \n\n"
#         body = spider.crawler.stats.get_stats()
#         body = pprint.pformat(body)
#         body = intro + body
#         msg.attach(MIMEText(body, 'plain'))
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         password = 'Afjb*0827/'
#         server.login(from_email, password)
#         server.ehlo()
#         text = msg.as_string()
#         server.sendmail(from_email, to_email, text)
#         server.quit()
#
#     # def open_spider(self, spider):
#     #     hostname = 'localhost'
#     #     username = 'postgres'
#     #     password = 'andy0827'
#     #     database = 'scrapy_celulares'
#     #     self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
#     #     self.cur = self.connection.cursor()
#     #
#     # def close_spider(self, spider):
#     #     self.cur.close()
#     #     self.connection.close()
#
#     # @check_spider_pipeline
#     def process_item(self, item, spider):
#
#         # if 'pipelines.CelularesPipeline' in getattr(spider, 'pipeline'):
#
#             # msg = '%%s %s ' % (self.__class__.__name__,)
#             # spider.log(msg % 'pipeline elegido 1', level=logging.DEBUG)
#         #
#         # self.cur.execute("INSERT INTO celularesml ("
#         #                  "a_id,"
#         #                  "b_link,"
#         #                  "c_producto,"
#         #                  "d_marca,"
#         #                  "e_modelo,"
#         #                  "f_estado,"
#         #                  "g_precio,"
#         #                  "h_vendidos,"
#         #                  "i_descuento,"
#         #                  "j_opiniones,"
#         #                  "k_rate_vendedor,"
#         #                  "l_ventas_per,"
#         #                  "m_num_per,"
#         #                  "n_denom_per,"
#         #                  "o_clase_vendedor,"
#         #                  "p_descripcion,"
#         #                  "q_ubicacion,"
#         #                  "r_fecha_info"
#         #                  # "memo_interna,"
#         #                  # "RAM,"
#         #                  # "pixel_camara,"
#         #                  # "cia_telefonica,"
#         #                  # "stock,"
#         #                  # "tamano_pantalla,"
#         #                  # "vendedor,"
#         #                  # "categoria,"
#         #                  # "subcategoria,"
#         #                  ")"
#         #
#         #                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#         #
#         #                  (
#         #                      item['a_id'],
#         #                      item['b_link'],
#         #                      item['c_producto'],
#         #                      item['d_marca'],
#         #                      item['e_modelo'],
#         #                      item['f_estado'],
#         #                      item['g_precio'],
#         #                      item['h_vendidos'],
#         #                      item['i_descuento'],
#         #                      item['j_opiniones'],
#         #                      item['k_rate_vendedor'],
#         #                      item['l_ventas_per'],
#         #                      item['m_num_per'],
#         #                      item['n_denom_per'],
#         #                      item['o_clase_vendedor'],
#         #                      item['p_descripcion'],
#         #                      item['q_ubicacion'],
#         #                      item['r_fecha_info']
#         #                      # item['memo_interna'],
#         #                      # item['RAM'],
#         #                      # item['pixel_camara'],
#         #                      # item['cia_telefonica'],
#         #                      # item['stock'],
#         #                      # item['tamano_pantalla'],
#         #                      # item['vendedor'],
#         #                      # item['categoria'],
#         #                      # item['subcategoria'],
#         #                  ))
#         #
#         # self.connection.commit()
#         return item
#
#
# class CarrosPipeline(object):
#
#     def close_spider(self, spider):
#         from_email = "ajimenezbonilla@gmail.com"
#         to_email = "ajimenezbonilla@gmail.com"
#         msg = MIMEMultipart()
#         msg['From'] = from_email
#         msg['To'] = to_email
#         msg['Subject'] = 'Scraper Report for ' + datetime.date.today().strftime("%m/%d/%y")
#         intro = "Summary stats from Scrapy spider: \n\n"
#         body = spider.crawler.stats.get_stats()
#         body = pprint.pformat(body)
#         body = intro + body
#         msg.attach(MIMEText(body, 'plain'))
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.ehlo()
#         password = 'Afjb*0827/'
#         server.login(from_email, password)
#         text = msg.as_string()
#         server.sendmail(from_email, to_email, text)
#         server.quit()
#
#     # def open_spider(self, spider):
#     #     hostname = 'localhost'
#     #     username = 'postgres'
#     #     password = 'andy0827'
#     #     database = 'scrapy_carros'
#     #     self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
#     #     self.cur = self.connection.cursor()
#     #
#     # def close_spider(self, spider):
#     #     self.cur.close()
#     #     self.connection.close()
#
#     # @check_spider_pipeline
#     def process_item(self, item, spider):
#
#         # if 'pipelines.CelularesPipeline' not in getattr(spider, 'pipeline'):
#
#             # msg = '%%s %s ' % (self.__class__.__name__,)
#             # spider.log(msg % 'pipeline elegido 2', level=logging.DEBUG)
#         # self.cur.execute("INSERT INTO carros ("
#         #                  "a_id"
#         #                  # "b_link,"
#         #                  # "c_producto,"
#         #                  # "d_marca,"
#         #                  # "e_modelo,"
#         #                  # "f_version,"
#         #                  # "g_precio,"
#         #                  # "h_KM,"
#         #                  # "i_year,"
#         #                  # "j_puertas,"
#         #                  # "k_transmision,"
#         #                  # "l_direccion,"
#         #                  # "m_placa,"
#         #                  # "n_color,"
#         #                  # "o_vendedor,"
#         #                  # "p_tel_contacto,"
#         #                  # "q_ubicacion,"
#         #                  # "qa_info_adicional,"
#         #                  # "qb_descripcion,"
#         #                  # "r_fecha_info"
#         #                  ")"
#         #
#         #                  "VALUES (%s)",
#         #
#         #                 (
#         #                     item['a_id']
#         #                     # item['b_link'],
#         #                     # item['c_producto'],
#         #                     # item['d_marca'],
#         #                     # item['e_modelo'],
#         #                     # item['f_version'],
#         #                     # item['g_precio'],
#         #                     # item['h_KM'],
#         #                     # item['i_year'],
#         #                     # item['j_puertas'],
#         #                     # item['k_transmision'],
#         #                     # item['l_direccion'],
#         #                     # item['m_placa'],
#         #                     # item['n_color'],
#         #                     # item['o_vendedor'],
#         #                     # item['p_tel_contacto'],
#         #                     # item['q_ubicacion'],
#         #                     # item['qa_info_adicional'],
#         #                     # item['qb_descripcion'],
#         #                     # item['r_fecha_info']
#         #                 ))
#         #
#         # self.connection.commit()
#         return item
