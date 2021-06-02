# brasil_api.BANKSApi

All URIs are relative to *https://brasilapi.com.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**banks_v1_code_get**](BANKSApi.md#banks_v1_code_get) | **GET** /banks/v1/{code} | Busca as informações de um banco a partir de um código
[**banks_v1_get**](BANKSApi.md#banks_v1_get) | **GET** /banks/v1 | Retorna informações de todos os bancos do Brasil


# **banks_v1_code_get**
> BankV1 banks_v1_code_get(code)

Busca as informações de um banco a partir de um código

### Example

```python
import time
import brasil_api
from brasil-api import banks_api
from brasil_api.model.bank_v1 import BankV1
from pprint import pprint
# Defining the host is optional and defaults to https://brasilapi.com.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = brasil_api.Configuration(
    host = "https://brasilapi.com.br/api"
)


# Enter a context with an instance of the API client
with brasil_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = banks_api.BANKSApi(api_client)
    code = "code_example" # str | Código do banco

    # example passing only required values which don't have defaults set
    try:
        # Busca as informações de um banco a partir de um código
        api_response = api_instance.banks_v1_code_get(code)
        pprint(api_response)
    except brasil_api.ApiException as e:
        print("Exception when calling BANKSApi->banks_v1_code_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Código do banco |

### Return type

[**BankV1**](BankV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | O código do banco não foi encontrado |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **banks_v1_get**
> [BankV1] banks_v1_get()

Retorna informações de todos os bancos do Brasil

### Example

```python
import time
import brasil_api
from brasil-api import banks_api
from brasil_api.model.bank_v1 import BankV1
from pprint import pprint
# Defining the host is optional and defaults to https://brasilapi.com.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = brasil_api.Configuration(
    host = "https://brasilapi.com.br/api"
)


# Enter a context with an instance of the API client
with brasil_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = banks_api.BANKSApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retorna informações de todos os bancos do Brasil
        api_response = api_instance.banks_v1_get()
        pprint(api_response)
    except brasil_api.ApiException as e:
        print("Exception when calling BANKSApi->banks_v1_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[BankV1]**](BankV1.md)

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

