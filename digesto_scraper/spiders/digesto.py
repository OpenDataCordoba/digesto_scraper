# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response


class DigestoSpider(scrapy.Spider):
    name = "digesto"
    allowed_domains = ["servicios.cordoba.gov.ar"]
    start_urls = ['http://servicios.cordoba.gov.ar/DigestoWeb/Page/BuscarDocumento.aspx']

    def parse(self, response):
        yield scrapy.FormRequest(
            'http://servicios.cordoba.gov.ar/DigestoWeb/Page/BuscarDocumento.aspx',
            formdata={
                'ctl00$tsm': 'ctl00$tsm|ctl00$ContentPlaceHolder1$btnBuscar',
                'ctl00$ContentPlaceHolder1$txtNro': '',
                'ctl00$ContentPlaceHolder1$txtAno': '0',
                'ctl00$ContentPlaceHolder1$ddlLegislacion': '0',
                'ctl00$ContentPlaceHolder1$txtExpediente': '',
                'ctl00$ContentPlaceHolder1$cboVocesGenerales$TextBox': 'Bienes',
                'ctl00$ContentPlaceHolder1$cboVocesGenerales$HiddenField': '0',
                'ctl00$ContentPlaceHolder1$cboVocesEspeciales$TextBox': '107',
                'ctl00$ContentPlaceHolder1$cboVocesEspeciales$HiddenField': '0',
                'ctl00$ContentPlaceHolder1$txtVocesG': '',
                'ctl00$ContentPlaceHolder1$txtVocesP': '',
                'ctl00$ContentPlaceHolder1$btnBuscar.x': '52',
                'ctl00$ContentPlaceHolder1$btnBuscar.y': '18',
                'tsm_HiddenField': '',
                '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                '__VIEWSTATEGENERATOR': response.css('input#__VIEWSTATEGENERATOR::attr(value)').extract_first(),
                '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                '__ASYNCPOST': 'true',
                '__LASTFOCUS': '',
                '__EVENTTARGET': '',
                '__EVENTARGUMENT': '',

            },
            callback=self.parse_result_page
        )
    def parse_result_page(self, response):
        print(response.body)
        inspect_response(response, self)