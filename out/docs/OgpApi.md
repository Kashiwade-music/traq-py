# traq.OgpApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ogp**](OgpApi.md#get_ogp) | **GET** /ogp | OGP情報を取得


# **get_ogp**
> Ogp get_ogp(url)

OGP情報を取得

OGP情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import ogp_api
from traq.model.ogp import Ogp
from pprint import pprint
# Defining the host is optional and defaults to https://q.trap.jp/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = traq.Configuration(
    host = "https://q.trap.jp/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = traq.Configuration(
    host = "https://q.trap.jp/api/v3"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with traq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ogp_api.OgpApi(api_client)
    url = "url_example" # str | OGPを取得したいURL

    # example passing only required values which don't have defaults set
    try:
        # OGP情報を取得
        api_response = api_instance.get_ogp(url)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling OgpApi->get_ogp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| OGPを取得したいURL |

### Return type

[**Ogp**](Ogp.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | 指定したURLが不正です。 |  -  |
**404** | 指定したURLに対するOGP情報が見つかりませんでした。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

