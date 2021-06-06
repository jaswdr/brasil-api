
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.banks_api import BanksApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from brasil_api.banks_api import BanksApi
from brasil_api.cep_api import CEPApi
from brasil_api.cep_v2_api import CEPV2Api
from brasil_api.cnpj_api import CNPJApi
from brasil_api.ddd_api import DDDApi
from brasil_api.feriados_nacionais_api import FeriadosNacionaisApi
from brasil_api.ibge_api import IBGEApi
