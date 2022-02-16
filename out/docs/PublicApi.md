# traq.PublicApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_user_icon**](PublicApi.md#get_public_user_icon) | **GET** /public/icon/{username} | ユーザーのアイコン画像を取得
[**get_server_version**](PublicApi.md#get_server_version) | **GET** /version | バージョンを取得


# **get_public_user_icon**
> file_type get_public_user_icon(username)

ユーザーのアイコン画像を取得

ユーザーのアイコン画像を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import public_api
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
    api_instance = public_api.PublicApi(api_client)
    username = "zBAMDTMv2D2ylmgd10Z3UB6U" # str | ユーザー名

    # example passing only required values which don't have defaults set
    try:
        # ユーザーのアイコン画像を取得
        api_response = api_instance.get_public_user_icon(username)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling PublicApi->get_public_user_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| ユーザー名 |

### Return type

**file_type**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, image/gif, image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_version**
> Version get_server_version()

バージョンを取得

サーバーバージョン及びサーバーフラグ情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import public_api
from traq.model.version import Version
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
    api_instance = public_api.PublicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # バージョンを取得
        api_response = api_instance.get_server_version()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling PublicApi->get_server_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

