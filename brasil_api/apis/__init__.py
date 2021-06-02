
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
from brasil-api.banks_api import BanksApi
from brasil-api.cep_api import CEPApi
from brasil-api.cep_v2_api import CEPV2Api
from brasil-api.cnpj_api import CNPJApi
from brasil-api.ddd_api import DDDApi
from brasil-api.feriados_nacionais_api import FeriadosNacionaisApi
from brasil-api.ibge_api import IBGEApi
