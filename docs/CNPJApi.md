# brasil_api.CNPJApi

All URIs are relative to *https://brasilapi.com.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cnpj_v1_cnpj_get**](CNPJApi.md#cnpj_v1_cnpj_get) | **GET** /cnpj/v1/{cnpj} | Busca por CNPJ na API Minha Receita.


# **cnpj_v1_cnpj_get**
> EmpresaV1 cnpj_v1_cnpj_get(cnpj)

Busca por CNPJ na API Minha Receita.

### Example

```python
import time
import brasil_api
from brasil_api.api import cnpj_api
from brasil_api.model.empresa_v1 import EmpresaV1
from pprint import pprint
# Defining the host is optional and defaults to https://brasilapi.com.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = brasil_api.Configuration(
    host = "https://brasilapi.com.br/api"
)


# Enter a context with an instance of the API client
with brasil_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cnpj_api.CNPJApi(api_client)
    cnpj = "cnpj_example" # str | O Cadastro Nacional da Pessoa Jurídica é um número único que identifica uma pessoa jurídica e outros tipos de arranjo jurídico sem personalidade jurídica junto à Receita Federal. 

    # example passing only required values which don't have defaults set
    try:
        # Busca por CNPJ na API Minha Receita.
        api_response = api_instance.cnpj_v1_cnpj_get(cnpj)
        pprint(api_response)
    except brasil_api.ApiException as e:
        print("Exception when calling CNPJApi->cnpj_v1_cnpj_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cnpj** | **str**| O Cadastro Nacional da Pessoa Jurídica é um número único que identifica uma pessoa jurídica e outros tipos de arranjo jurídico sem personalidade jurídica junto à Receita Federal.  |

### Return type

[**EmpresaV1**](EmpresaV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | CNPJ não encontrado na API Minha Receita. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

