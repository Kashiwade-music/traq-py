# traq.MessageApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_message_stamp**](MessageApi.md#add_message_stamp) | **POST** /messages/{messageId}/stamps/{stampId} | スタンプを押す
[**create_pin**](MessageApi.md#create_pin) | **POST** /messages/{messageId}/pin | ピン留めする
[**delete_message**](MessageApi.md#delete_message) | **DELETE** /messages/{messageId} | メッセージを削除
[**edit_message**](MessageApi.md#edit_message) | **PUT** /messages/{messageId} | メッセージを編集
[**get_direct_messages**](MessageApi.md#get_direct_messages) | **GET** /users/{userId}/messages | ダイレクトメッセージのリストを取得
[**get_message**](MessageApi.md#get_message) | **GET** /messages/{messageId} | メッセージを取得
[**get_message_clips**](MessageApi.md#get_message_clips) | **GET** /messages/{messageId}/clips | 自分のクリップを取得
[**get_message_stamps**](MessageApi.md#get_message_stamps) | **GET** /messages/{messageId}/stamps | メッセージのスタンプリストを取得
[**get_messages**](MessageApi.md#get_messages) | **GET** /channels/{channelId}/messages | チャンネルメッセージのリストを取得
[**get_pin**](MessageApi.md#get_pin) | **GET** /messages/{messageId}/pin | ピン留めを取得
[**post_direct_message**](MessageApi.md#post_direct_message) | **POST** /users/{userId}/messages | ダイレクトメッセージを送信
[**post_message**](MessageApi.md#post_message) | **POST** /channels/{channelId}/messages | チャンネルにメッセージを投稿
[**remove_message_stamp**](MessageApi.md#remove_message_stamp) | **DELETE** /messages/{messageId}/stamps/{stampId} | スタンプを消す
[**remove_pin**](MessageApi.md#remove_pin) | **DELETE** /messages/{messageId}/pin | ピン留めを外す
[**search_messages**](MessageApi.md#search_messages) | **GET** /messages | メッセージを検索


# **add_message_stamp**
> add_message_stamp(message_id, stamp_id)

スタンプを押す

指定したメッセージに指定したスタンプを押します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.post_message_stamp_request import PostMessageStampRequest
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
    api_instance = message_api.MessageApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID
    stamp_id = "stampId_example" # str | スタンプUUID
    post_message_stamp_request = PostMessageStampRequest(
        count=1,
    ) # PostMessageStampRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # スタンプを押す
        api_instance.add_message_stamp(message_id, stamp_id)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->add_message_stamp: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # スタンプを押す
        api_instance.add_message_stamp(message_id, stamp_id, post_message_stamp_request=post_message_stamp_request)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->add_message_stamp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID |
 **stamp_id** | **str**| スタンプUUID |
 **post_message_stamp_request** | [**PostMessageStampRequest**](PostMessageStampRequest.md)|  | [optional]

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
**204** | No Content スタンプを押すことができました。 |  -  |
**400** | Bad Request |  -  |
**404** | Not Found メッセージ、またはスタンプが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pin**
> MessagePin create_pin(message_id)

ピン留めする

指定したメッセージをピン留めします。 アーカイブされているチャンネルのメッセージ・存在しないメッセージ・チャンネル当たりの上限数を超えたメッセージのピン留めはできません。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.message_pin import MessagePin
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
    api_instance = message_api.MessageApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID

    # example passing only required values which don't have defaults set
    try:
        # ピン留めする
        api_response = api_instance.create_pin(message_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->create_pin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID |

### Return type

[**MessagePin**](MessagePin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created 指定したメッセージがピン留めされました。 |  -  |
**400** | Bad Request |  -  |
**404** | Not Found メッセージが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message**
> delete_message(message_id)

メッセージを削除

指定したメッセージを削除します。 自身が投稿したメッセージと自身が管理権限を持つWebhookとBOTが投稿したメッセージのみ削除することができます。 アーカイブされているチャンネルのメッセージを編集することは出来ません。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
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
    api_instance = message_api.MessageApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID

    # example passing only required values which don't have defaults set
    try:
        # メッセージを削除
        api_instance.delete_message(message_id)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->delete_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | No Content 正常に削除できました。 |  -  |
**403** | Forbidden 指定されたメッセージを削除する権限がありません。 |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_message**
> edit_message(message_id)

メッセージを編集

指定したメッセージを編集します。 自身が投稿したメッセージのみ編集することができます。 アーカイブされているチャンネルのメッセージを編集することは出来ません。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.post_message_request import PostMessageRequest
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
    api_instance = message_api.MessageApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID
    post_message_request = PostMessageRequest(
        content="content_example",
        embed=False,
    ) # PostMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # メッセージを編集
        api_instance.edit_message(message_id)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->edit_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # メッセージを編集
        api_instance.edit_message(message_id, post_message_request=post_message_request)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->edit_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID |
 **post_message_request** | [**PostMessageRequest**](PostMessageRequest.md)|  | [optional]

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
**204** | No Content メッセージを編集できました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden 指定されたメッセージを編集する権限がありません。 |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_direct_messages**
> [Message] get_direct_messages(user_id)

ダイレクトメッセージのリストを取得

指定したユーザーとのダイレクトメッセージのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.message import Message
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
    api_instance = message_api.MessageApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID
    limit = 50 # int | 取得する件数 (optional)
    offset = 150 # int | 取得するオフセット (optional) if omitted the server will use the default value of 0
    since = dateutil_parser('2016-10-12T11:00:00.000000Z') # datetime | 取得する時間範囲の開始日時 (optional) if omitted the server will use the default value of dateutil_parser('0000-01-01T00:00:00Z')
    until = dateutil_parser('2016-10-12T11:00:00.0000000Z') # datetime | 取得する時間範囲の終了日時 (optional)
    inclusive = False # bool | 範囲の端を含めるかどうか (optional) if omitted the server will use the default value of False
    order = "desc" # str | 昇順か降順か (optional) if omitted the server will use the default value of "desc"

    # example passing only required values which don't have defaults set
    try:
        # ダイレクトメッセージのリストを取得
        api_response = api_instance.get_direct_messages(user_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->get_direct_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ダイレクトメッセージのリストを取得
        api_response = api_instance.get_direct_messages(user_id, limit=limit, offset=offset, since=since, until=until, inclusive=inclusive, order=order)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->get_direct_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |
 **limit** | **int**| 取得する件数 | [optional]
 **offset** | **int**| 取得するオフセット | [optional] if omitted the server will use the default value of 0
 **since** | **datetime**| 取得する時間範囲の開始日時 | [optional] if omitted the server will use the default value of dateutil_parser('0000-01-01T00:00:00Z')
 **until** | **datetime**| 取得する時間範囲の終了日時 | [optional]
 **inclusive** | **bool**| 範囲の端を含めるかどうか | [optional] if omitted the server will use the default value of False
 **order** | **str**| 昇順か降順か | [optional] if omitted the server will use the default value of "desc"

### Return type

[**[Message]**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-TRAQ-MORE -  <br>  |
**400** | Bad Request |  -  |
**404** | Not Found ユーザーが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message**
> Message get_message(message_id)

メッセージを取得

指定したメッセージを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.message import Message
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
    api_instance = message_api.MessageApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID

    # example passing only required values which don't have defaults set
    try:
        # メッセージを取得
        api_response = api_instance.get_message(message_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->get_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID |

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

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
from traq.api import message_api
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
    api_instance = message_api.MessageApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID

    # example passing only required values which don't have defaults set
    try:
        # 自分のクリップを取得
        api_response = api_instance.get_message_clips(message_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->get_message_clips: %s\n" % e)
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

# **get_message_stamps**
> [MessageStamp] get_message_stamps(message_id)

メッセージのスタンプリストを取得

指定したメッセージに押されているスタンプのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.message_stamp import MessageStamp
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
    api_instance = message_api.MessageApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID

    # example passing only required values which don't have defaults set
    try:
        # メッセージのスタンプリストを取得
        api_response = api_instance.get_message_stamps(message_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->get_message_stamps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID |

### Return type

[**[MessageStamp]**](MessageStamp.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> [Message] get_messages(channel_id)

チャンネルメッセージのリストを取得

指定したチャンネルのメッセージのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.message import Message
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
    api_instance = message_api.MessageApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID
    limit = 50 # int | 取得する件数 (optional)
    offset = 150 # int | 取得するオフセット (optional) if omitted the server will use the default value of 0
    since = dateutil_parser('2016-10-12T11:00:00.000000Z') # datetime | 取得する時間範囲の開始日時 (optional) if omitted the server will use the default value of dateutil_parser('0000-01-01T00:00:00Z')
    until = dateutil_parser('2016-10-12T11:00:00.0000000Z') # datetime | 取得する時間範囲の終了日時 (optional)
    inclusive = False # bool | 範囲の端を含めるかどうか (optional) if omitted the server will use the default value of False
    order = "desc" # str | 昇順か降順か (optional) if omitted the server will use the default value of "desc"

    # example passing only required values which don't have defaults set
    try:
        # チャンネルメッセージのリストを取得
        api_response = api_instance.get_messages(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->get_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルメッセージのリストを取得
        api_response = api_instance.get_messages(channel_id, limit=limit, offset=offset, since=since, until=until, inclusive=inclusive, order=order)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->get_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |
 **limit** | **int**| 取得する件数 | [optional]
 **offset** | **int**| 取得するオフセット | [optional] if omitted the server will use the default value of 0
 **since** | **datetime**| 取得する時間範囲の開始日時 | [optional] if omitted the server will use the default value of dateutil_parser('0000-01-01T00:00:00Z')
 **until** | **datetime**| 取得する時間範囲の終了日時 | [optional]
 **inclusive** | **bool**| 範囲の端を含めるかどうか | [optional] if omitted the server will use the default value of False
 **order** | **str**| 昇順か降順か | [optional] if omitted the server will use the default value of "desc"

### Return type

[**[Message]**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-TRAQ-MORE -  <br>  |
**400** | Bad Request |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pin**
> MessagePin get_pin(message_id)

ピン留めを取得

指定したメッセージのピン留め情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.message_pin import MessagePin
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
    api_instance = message_api.MessageApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID

    # example passing only required values which don't have defaults set
    try:
        # ピン留めを取得
        api_response = api_instance.get_pin(message_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->get_pin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID |

### Return type

[**MessagePin**](MessagePin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found 指定したメッセージ、またはピン留めが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_direct_message**
> Message post_direct_message(user_id)

ダイレクトメッセージを送信

指定したユーザーにダイレクトメッセージを送信します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.message import Message
from traq.model.post_message_request import PostMessageRequest
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
    api_instance = message_api.MessageApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID
    post_message_request = PostMessageRequest(
        content="content_example",
        embed=False,
    ) # PostMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ダイレクトメッセージを送信
        api_response = api_instance.post_direct_message(user_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->post_direct_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ダイレクトメッセージを送信
        api_response = api_instance.post_direct_message(user_id, post_message_request=post_message_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->post_direct_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |
 **post_message_request** | [**PostMessageRequest**](PostMessageRequest.md)|  | [optional]

### Return type

[**Message**](Message.md)

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
**404** | Not Found ユーザーが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_message**
> Message post_message(channel_id)

チャンネルにメッセージを投稿

指定したチャンネルにメッセージを投稿します。 embedをtrueに指定すると、メッセージ埋め込みが自動で行われます。 アーカイブされているチャンネルに投稿することはできません。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.message import Message
from traq.model.post_message_request import PostMessageRequest
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
    api_instance = message_api.MessageApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID
    post_message_request = PostMessageRequest(
        content="content_example",
        embed=False,
    ) # PostMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # チャンネルにメッセージを投稿
        api_response = api_instance.post_message(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->post_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルにメッセージを投稿
        api_response = api_instance.post_message(channel_id, post_message_request=post_message_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->post_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |
 **post_message_request** | [**PostMessageRequest**](PostMessageRequest.md)|  | [optional]

### Return type

[**Message**](Message.md)

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
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_message_stamp**
> remove_message_stamp(message_id, stamp_id)

スタンプを消す

指定したメッセージから指定した自身が押したスタンプを削除します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
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
    api_instance = message_api.MessageApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID
    stamp_id = "stampId_example" # str | スタンプUUID

    # example passing only required values which don't have defaults set
    try:
        # スタンプを消す
        api_instance.remove_message_stamp(message_id, stamp_id)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->remove_message_stamp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID |
 **stamp_id** | **str**| スタンプUUID |

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
**204** | No Content スタンプを消すことができました。 |  -  |
**404** | Not Found メッセージ、またはスタンプが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_pin**
> remove_pin(message_id)

ピン留めを外す

指定したメッセージのピン留めを外します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
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
    api_instance = message_api.MessageApi(api_client)
    message_id = "messageId_example" # str | メッセージUUID

    # example passing only required values which don't have defaults set
    try:
        # ピン留めを外す
        api_instance.remove_pin(message_id)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->remove_pin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | No Content 指定したメッセージのピン留めが外されました。 |  -  |
**400** | Bad Request |  -  |
**404** | Not Found 指定したメッセージ、またはピン留めが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_messages**
> MessageSearchResult search_messages()

メッセージを検索

メッセージを検索します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import message_api
from traq.model.message_search_result import MessageSearchResult
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
    api_instance = message_api.MessageApi(api_client)
    word = ""phrase match" +(foo | bar) -baz" # str | 検索ワード Simple-Query-String-Syntaxをパースして検索します  (optional)
    after = dateutil_parser('2006-01-02T15:04:05Z') # datetime | 投稿日時が指定日時より後 (optional)
    before = dateutil_parser('2006-01-02T15:04:05Z') # datetime | 投稿日時が指定日時より前 (optional)
    _in = "in_example" # str | メッセージが投稿されたチャンネル (optional)
    to = "to_example" # str | メンションされたユーザー (optional)
    _from = "from_example" # str | メッセージを投稿したユーザー (optional)
    citation = "citation_example" # str | 引用しているメッセージ (optional)
    bot = True # bool | メッセージを投稿したユーザーがBotかどうか (optional)
    has_url = True # bool | メッセージがURLを含むか (optional)
    has_attachments = True # bool | メッセージが添付ファイルを含むか (optional)
    has_image = True # bool | メッセージが画像を含むか (optional)
    has_video = True # bool | メッセージが動画を含むか (optional)
    has_audio = True # bool | メッセージが音声ファイルを含むか (optional)
    limit = 1 # int | 検索結果から取得するメッセージの最大件数 (optional)
    offset = 0 # int | 検索結果から取得するメッセージのオフセット (optional)
    sort = "-createdAt" # str | ソート順 (作成日時が新しい `createdAt`, 作成日時が古い `-createdAt`, 更新日時が新しい `updatedAt`, 更新日時が古い `-updatedAt`) (optional) if omitted the server will use the default value of "-createdAt"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # メッセージを検索
        api_response = api_instance.search_messages(word=word, after=after, before=before, _in=_in, to=to, _from=_from, citation=citation, bot=bot, has_url=has_url, has_attachments=has_attachments, has_image=has_image, has_video=has_video, has_audio=has_audio, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MessageApi->search_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **word** | **str**| 検索ワード Simple-Query-String-Syntaxをパースして検索します  | [optional]
 **after** | **datetime**| 投稿日時が指定日時より後 | [optional]
 **before** | **datetime**| 投稿日時が指定日時より前 | [optional]
 **_in** | **str**| メッセージが投稿されたチャンネル | [optional]
 **to** | **str**| メンションされたユーザー | [optional]
 **_from** | **str**| メッセージを投稿したユーザー | [optional]
 **citation** | **str**| 引用しているメッセージ | [optional]
 **bot** | **bool**| メッセージを投稿したユーザーがBotかどうか | [optional]
 **has_url** | **bool**| メッセージがURLを含むか | [optional]
 **has_attachments** | **bool**| メッセージが添付ファイルを含むか | [optional]
 **has_image** | **bool**| メッセージが画像を含むか | [optional]
 **has_video** | **bool**| メッセージが動画を含むか | [optional]
 **has_audio** | **bool**| メッセージが音声ファイルを含むか | [optional]
 **limit** | **int**| 検索結果から取得するメッセージの最大件数 | [optional]
 **offset** | **int**| 検索結果から取得するメッセージのオフセット | [optional]
 **sort** | **str**| ソート順 (作成日時が新しい &#x60;createdAt&#x60;, 作成日時が古い &#x60;-createdAt&#x60;, 更新日時が新しい &#x60;updatedAt&#x60;, 更新日時が古い &#x60;-updatedAt&#x60;) | [optional] if omitted the server will use the default value of "-createdAt"

### Return type

[**MessageSearchResult**](MessageSearchResult.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**503** | search service is currently unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

