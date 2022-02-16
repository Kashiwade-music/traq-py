# traq.ClipApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clip_message**](ClipApi.md#clip_message) | **POST** /clip-folders/{folderId}/messages | メッセージをクリップフォルダに追加
[**create_clip_folder**](ClipApi.md#create_clip_folder) | **POST** /clip-folders | クリップフォルダを作成
[**delete_clip_folder**](ClipApi.md#delete_clip_folder) | **DELETE** /clip-folders/{folderId} | クリップフォルダを削除
[**edit_clip_folder**](ClipApi.md#edit_clip_folder) | **PATCH** /clip-folders/{folderId} | クリップフォルダ情報を編集
[**get_clip_folder**](ClipApi.md#get_clip_folder) | **GET** /clip-folders/{folderId} | クリップフォルダ情報を取得
[**get_clip_folders**](ClipApi.md#get_clip_folders) | **GET** /clip-folders | クリップフォルダのリストを取得
[**get_clips**](ClipApi.md#get_clips) | **GET** /clip-folders/{folderId}/messages | フォルダ内のクリップのリストを取得
[**get_message_clips**](ClipApi.md#get_message_clips) | **GET** /messages/{messageId}/clips | 自分のクリップを取得
[**unclip_message**](ClipApi.md#unclip_message) | **DELETE** /clip-folders/{folderId}/messages/{messageId} | メッセージをクリップフォルダから除外


# **clip_message**
> ClippedMessage clip_message(folder_id)

メッセージをクリップフォルダに追加

指定したメッセージを指定したクリップフォルダに追加します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import clip_api
from traq.model.clipped_message import ClippedMessage
from traq.model.post_clip_folder_message_request import PostClipFolderMessageRequest
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
    api_instance = clip_api.ClipApi(api_client)
    folder_id = "folderId_example" # str | クリップフォルダUUID
    post_clip_folder_message_request = PostClipFolderMessageRequest(
        message_id="message_id_example",
    ) # PostClipFolderMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # メッセージをクリップフォルダに追加
        api_response = api_instance.clip_message(folder_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->clip_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # メッセージをクリップフォルダに追加
        api_response = api_instance.clip_message(folder_id, post_clip_folder_message_request=post_clip_folder_message_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->clip_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID |
 **post_clip_folder_message_request** | [**PostClipFolderMessageRequest**](PostClipFolderMessageRequest.md)|  | [optional]

### Return type

[**ClippedMessage**](ClippedMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found クリップフォルダが見つかりません。 |  -  |
**409** | Conflict 既に追加されています。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clip_folder**
> ClipFolder create_clip_folder()

クリップフォルダを作成

クリップフォルダを作成します。 既にあるフォルダと同名のフォルダを作成することは可能です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import clip_api
from traq.model.clip_folder import ClipFolder
from traq.model.post_clip_folder_request import PostClipFolderRequest
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
    api_instance = clip_api.ClipApi(api_client)
    post_clip_folder_request = PostClipFolderRequest(
        name="name_example",
        description="description_example",
    ) # PostClipFolderRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # クリップフォルダを作成
        api_response = api_instance.create_clip_folder(post_clip_folder_request=post_clip_folder_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->create_clip_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_clip_folder_request** | [**PostClipFolderRequest**](PostClipFolderRequest.md)|  | [optional]

### Return type

[**ClipFolder**](ClipFolder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clip_folder**
> delete_clip_folder(folder_id)

クリップフォルダを削除

指定したクリップフォルダを削除します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import clip_api
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
    api_instance = clip_api.ClipApi(api_client)
    folder_id = "folderId_example" # str | クリップフォルダUUID

    # example passing only required values which don't have defaults set
    try:
        # クリップフォルダを削除
        api_instance.delete_clip_folder(folder_id)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->delete_clip_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content 削除しました。 |  -  |
**404** | Not Found クリップフォルダが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_clip_folder**
> edit_clip_folder(folder_id)

クリップフォルダ情報を編集

指定したクリップフォルダの情報を編集します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import clip_api
from traq.model.patch_clip_folder_request import PatchClipFolderRequest
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
    api_instance = clip_api.ClipApi(api_client)
    folder_id = "folderId_example" # str | クリップフォルダUUID
    patch_clip_folder_request = PatchClipFolderRequest(
        name="name_example",
        description="description_example",
    ) # PatchClipFolderRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # クリップフォルダ情報を編集
        api_instance.edit_clip_folder(folder_id)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->edit_clip_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # クリップフォルダ情報を編集
        api_instance.edit_clip_folder(folder_id, patch_clip_folder_request=patch_clip_folder_request)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->edit_clip_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID |
 **patch_clip_folder_request** | [**PatchClipFolderRequest**](PatchClipFolderRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content 編集しました。 |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clip_folder**
> ClipFolder get_clip_folder(folder_id)

クリップフォルダ情報を取得

指定したクリップフォルダの情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import clip_api
from traq.model.clip_folder import ClipFolder
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
    api_instance = clip_api.ClipApi(api_client)
    folder_id = "folderId_example" # str | クリップフォルダUUID

    # example passing only required values which don't have defaults set
    try:
        # クリップフォルダ情報を取得
        api_response = api_instance.get_clip_folder(folder_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->get_clip_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID |

### Return type

[**ClipFolder**](ClipFolder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found クリップフォルダが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clip_folders**
> [ClipFolder] get_clip_folders()

クリップフォルダのリストを取得

自身が所有するクリップフォルダのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import clip_api
from traq.model.clip_folder import ClipFolder
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
    api_instance = clip_api.ClipApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # クリップフォルダのリストを取得
        api_response = api_instance.get_clip_folders()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->get_clip_folders: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ClipFolder]**](ClipFolder.md)

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

# **get_clips**
> [ClippedMessage] get_clips(folder_id)

フォルダ内のクリップのリストを取得

指定したフォルダ内のクリップのリストを取得します。 `order`を指定しない場合、クリップした日時の新しい順で返されます。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import clip_api
from traq.model.clipped_message import ClippedMessage
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
    api_instance = clip_api.ClipApi(api_client)
    folder_id = "folderId_example" # str | クリップフォルダUUID
    limit = 50 # int | 取得する件数 (optional)
    offset = 150 # int | 取得するオフセット (optional) if omitted the server will use the default value of 0
    order = "desc" # str | 昇順か降順か (optional) if omitted the server will use the default value of "desc"

    # example passing only required values which don't have defaults set
    try:
        # フォルダ内のクリップのリストを取得
        api_response = api_instance.get_clips(folder_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->get_clips: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # フォルダ内のクリップのリストを取得
        api_response = api_instance.get_clips(folder_id, limit=limit, offset=offset, order=order)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->get_clips: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID |
 **limit** | **int**| 取得する件数 | [optional]
 **offset** | **int**| 取得するオフセット | [optional] if omitted the server will use the default value of 0
 **order** | **str**| 昇順か降順か | [optional] if omitted the server will use the default value of "desc"

### Return type

[**[ClippedMessage]**](ClippedMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found クリップフォルダが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_clips**
> [MessageClip] get_message_clips(message_id)

自分のクリップを取得

対象のメッセージの自分のクリップの一覧を返します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import clip_api
from traq.model.message_clip import MessageClip
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
    api_instance = clip_api.ClipApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID

    # example passing only required values which don't have defaults set
    try:
        # 自分のクリップを取得
        api_response = api_instance.get_message_clips(message_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->get_message_clips: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID |

### Return type

[**[MessageClip]**](MessageClip.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unclip_message**
> unclip_message(folder_id, message_id)

メッセージをクリップフォルダから除外

指定したフォルダから指定したメッセージのクリップを除外します。 既に外されているメッセージを指定した場合は204を返します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import clip_api
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
    api_instance = clip_api.ClipApi(api_client)
    folder_id = "folderId_example" # str | クリップフォルダUUID
    message_id = "messageId_example" # str | メッセージUUID

    # example passing only required values which don't have defaults set
    try:
        # メッセージをクリップフォルダから除外
        api_instance.unclip_message(folder_id, message_id)
    except traq.ApiException as e:
        print("Exception when calling ClipApi->unclip_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID |
 **message_id** | **str**| メッセージUUID |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content 外しました。 |  -  |
**404** | Not Found クリップフォルダが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

