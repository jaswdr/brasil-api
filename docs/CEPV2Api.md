# brasil_api.CEPV2Api

All URIs are relative to *https://brasilapi.com.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cep_v2_cep_get**](CEPV2Api.md#cep_v2_cep_get) | **GET** /cep/v2/{cep} | Busca por CEP com múltiplos providers de fallback v2.


# **cep_v2_cep_get**
> CEPV2 cep_v2_cep_get(cep)

Busca por CEP com múltiplos providers de fallback v2.

### Example

```python
import time
import brasil_api
from brasil_api.api import cep_v2_api
from brasil_api.model.cepv2 import CEPV2
from pprint import pprint
# Defining the host is optional and defaults to https://brasilapi.com.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = brasil_api.Configuration(
    host = "https://brasilapi.com.br/api"
)


# Enter a context with an instance of the API client
with brasil_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cep_v2_api.CEPV2Api(api_client)
    cep = 1 # int | O CEP (Código de Endereçamento Postal) é um sistema de códigos que visa racionalizar o processo de encaminhamento e entrega de correspondências através da divisão do país em regiões postais. ... Atualmente, o CEP é composto por oito dígitos, cinco de um lado e três de outro. Cada algarismo do CEP possui um significado. 

    # example passing only required values which don't have defaults set
    try:
        # Busca por CEP com múltiplos providers de fallback v2.
        api_response = api_instance.cep_v2_cep_get(cep)
        pprint(api_response)
    except brasil_api.ApiException as e:
        print("Exception when calling CEPV2Api->cep_v2_cep_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cep** | **int**| O CEP (Código de Endereçamento Postal) é um sistema de códigos que visa racionalizar o processo de encaminhamento e entrega de correspondências através da divisão do país em regiões postais. ... Atualmente, o CEP é composto por oito dígitos, cinco de um lado e três de outro. Cada algarismo do CEP possui um significado.  |

### Return type

[**CEPV2**](CEPV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Todos os serviços de CEP retornaram erro. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

