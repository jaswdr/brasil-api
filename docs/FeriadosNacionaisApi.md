# brasil_api.FeriadosNacionaisApi

All URIs are relative to *https://brasilapi.com.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feriados_v1_ano_get**](FeriadosNacionaisApi.md#feriados_v1_ano_get) | **GET** /feriados/v1/{ano} | Lista os feriados nacionais de determinado ano.


# **feriados_v1_ano_get**
> [FeriadoV1] feriados_v1_ano_get(ano)

Lista os feriados nacionais de determinado ano.

Calcula os feriados móveis baseados na Páscoa e adiciona os feriados fixos

### Example

```python
import time
import brasil_api
from brasil-api import feriados_nacionais_api
from brasil_api.model.feriado_v1 import FeriadoV1
from pprint import pprint
# Defining the host is optional and defaults to https://brasilapi.com.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = brasil_api.Configuration(
    host = "https://brasilapi.com.br/api"
)


# Enter a context with an instance of the API client
with brasil_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = feriados_nacionais_api.FeriadosNacionaisApi(api_client)
    ano = 1 # int | Ano para calcular os feriados. 

    # example passing only required values which don't have defaults set
    try:
        # Lista os feriados nacionais de determinado ano.
        api_response = api_instance.feriados_v1_ano_get(ano)
        pprint(api_response)
    except brasil_api.ApiException as e:
        print("Exception when calling FeriadosNacionaisApi->feriados_v1_ano_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ano** | **int**| Ano para calcular os feriados.  |

### Return type

[**[FeriadoV1]**](FeriadoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Ano fora do intervalo suportado. |  -  |
**500** | Erro inesperado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

