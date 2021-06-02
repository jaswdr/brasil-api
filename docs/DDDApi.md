# brasil_api.DDDApi

All URIs are relative to *https://brasilapi.com.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ddd_v1_ddd_get**](DDDApi.md#ddd_v1_ddd_get) | **GET** /ddd/v1/{ddd} | Retorna estado e lista de cidades por DDD


# **ddd_v1_ddd_get**
> DDDV1 ddd_v1_ddd_get(ddd)

Retorna estado e lista de cidades por DDD

### Example

```python
import time
import brasil_api
from brasil-api import ddd_api
from brasil_api.model.dddv1 import DDDV1
from pprint import pprint
# Defining the host is optional and defaults to https://brasilapi.com.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = brasil_api.Configuration(
    host = "https://brasilapi.com.br/api"
)


# Enter a context with an instance of the API client
with brasil_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ddd_api.DDDApi(api_client)
    ddd = 1 # int | DDD significa Discagem Direta à Distância. É um sistema de ligação telefônica automática entre diferentes áreas urbanas nacionais. O DDD é um código constituído por 2 dígitos que identificam as principais cidades do país e devem ser adicionados ao nº de telefone, juntamente com o código da operadora. 

    # example passing only required values which don't have defaults set
    try:
        # Retorna estado e lista de cidades por DDD
        api_response = api_instance.ddd_v1_ddd_get(ddd)
        pprint(api_response)
    except brasil_api.ApiException as e:
        print("Exception when calling DDDApi->ddd_v1_ddd_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ddd** | **int**| DDD significa Discagem Direta à Distância. É um sistema de ligação telefônica automática entre diferentes áreas urbanas nacionais. O DDD é um código constituído por 2 dígitos que identificam as principais cidades do país e devem ser adicionados ao nº de telefone, juntamente com o código da operadora.  |

### Return type

[**DDDV1**](DDDV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | DDD não encontrado |  -  |
**500** | Todos os serviços de DDD retornaram erro. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

