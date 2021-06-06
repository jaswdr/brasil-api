# brasil_api.IBGEApi

All URIs are relative to *https://brasilapi.com.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ibge_uf_v1_code_get**](IBGEApi.md#ibge_uf_v1_code_get) | **GET** /ibge/uf/v1/{code} | Busca as informações de um um estado a partir da sigla ou código
[**ibge_uf_v1_get**](IBGEApi.md#ibge_uf_v1_get) | **GET** /ibge/uf/v1 | Retorna informações de todos estados do Brasil


# **ibge_uf_v1_code_get**
> IBGEV1 ibge_uf_v1_code_get(code)

Busca as informações de um um estado a partir da sigla ou código

### Example

```python
import time
import brasil_api
from brasil_api.api import ibge_api
from brasil_api.model.ibgev1 import IBGEV1
from pprint import pprint
# Defining the host is optional and defaults to https://brasilapi.com.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = brasil_api.Configuration(
    host = "https://brasilapi.com.br/api"
)


# Enter a context with an instance of the API client
with brasil_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ibge_api.IBGEApi(api_client)
    code = "code_example" # str | Código do IBGE

    # example passing only required values which don't have defaults set
    try:
        # Busca as informações de um um estado a partir da sigla ou código
        api_response = api_instance.ibge_uf_v1_code_get(code)
        pprint(api_response)
    except brasil_api.ApiException as e:
        print("Exception when calling IBGEApi->ibge_uf_v1_code_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Código do IBGE |

### Return type

[**IBGEV1**](IBGEV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | O código / sigla do estado não foi encontrado |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibge_uf_v1_get**
> [IBGEV1] ibge_uf_v1_get()

Retorna informações de todos estados do Brasil

### Example

```python
import time
import brasil_api
from brasil_api.api import ibge_api
from brasil_api.model.ibgev1 import IBGEV1
from pprint import pprint
# Defining the host is optional and defaults to https://brasilapi.com.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = brasil_api.Configuration(
    host = "https://brasilapi.com.br/api"
)


# Enter a context with an instance of the API client
with brasil_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ibge_api.IBGEApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retorna informações de todos estados do Brasil
        api_response = api_instance.ibge_uf_v1_get()
        pprint(api_response)
    except brasil_api.ApiException as e:
        print("Exception when calling IBGEApi->ibge_uf_v1_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[IBGEV1]**](IBGEV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

