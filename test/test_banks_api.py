"""
    Brasil API

    Acesso programático de informações é algo fundamental na comunicação entre sistemas mas, para nossa surpresa, uma informação tão útil e pública quanto um CEP não consegue ser acessada diretamente por um navegador por conta da API dos Correios não possuir CORS habilitado. Dado a isso, este projeto experimental tem como objetivo centralizar e disponibilizar endpoints modernos com baixíssima latência utilizando tecnologias como Vercel Smart CDN responsável por fazer o cache das informações em atualmente 23 regiões distribuídas ao longo do mundo (incluindo Brasil). Então não importa o quão devagar for a fonte dos dados, nós queremos disponibilizá-la da forma mais rápida e moderna possível.  Recursos disponíveis   - CEP   - DDD   - Banks   - CNPJ   - IBGE   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import brasil_api
from brasil-api.banks_api import BANKSApi  # noqa: E501


class TestBANKSApi(unittest.TestCase):
    """BANKSApi unit test stubs"""

    def setUp(self):
        self.api = BANKSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_banks_v1_code_get(self):
        """Test case for banks_v1_code_get

        Busca as informações de um banco a partir de um código  # noqa: E501
        """
        pass

    def test_banks_v1_get(self):
        """Test case for banks_v1_get

        Retorna informações de todos os bancos do Brasil  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
