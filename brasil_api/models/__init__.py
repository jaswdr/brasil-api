# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from brasil_api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from brasil_api.model.bank_v1 import BankV1
from brasil_api.model.cepv1 import CEPV1
from brasil_api.model.cepv2 import CEPV2
from brasil_api.model.dddv1 import DDDV1
from brasil_api.model.empresa_v1 import EmpresaV1
from brasil_api.model.feriado_v1 import FeriadoV1
from brasil_api.model.ibgev1 import IBGEV1
from brasil_api.model.ibgev1_regiao import IBGEV1Regiao
