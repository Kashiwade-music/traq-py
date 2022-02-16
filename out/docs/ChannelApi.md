# traq.ChannelApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel**](ChannelApi.md#create_channel) | **POST** /channels | チャンネルを作成
[**edit_channel**](ChannelApi.md#edit_channel) | **PATCH** /channels/{channelId} | チャンネル情報を変更
[**edit_channel_subscribers**](ChannelApi.md#edit_channel_subscribers) | **PATCH** /channels/{channelId}/subscribers | チャンネルの通知購読者を編集
[**edit_channel_topic**](ChannelApi.md#edit_channel_topic) | **PUT** /channels/{channelId}/topic | チャンネルトピックを編集
[**get_channel**](ChannelApi.md#get_channel) | **GET** /channels/{channelId} | チャンネル情報を取得
[**get_channel_bots**](ChannelApi.md#get_channel_bots) | **GET** /channels/{channelId}/bots | チャンネル参加中のBOTのリストを取得
[**get_channel_events**](ChannelApi.md#get_channel_events) | **GET** /channels/{channelId}/events | チャンネルイベントのリストを取得
[**get_channel_pins**](ChannelApi.md#get_channel_pins) | **GET** /channels/{channelId}/pins | チャンネルピンのリストを取得
[**get_channel_stats**](ChannelApi.md#get_channel_stats) | **GET** /channels/{channelId}/stats | チャンネル統計情報を取得
[**get_channel_subscribers**](ChannelApi.md#get_channel_subscribers) | **GET** /channels/{channelId}/subscribers | チャンネルの通知購読者のリストを取得
[**get_channel_topic**](ChannelApi.md#get_channel_topic) | **GET** /channels/{channelId}/topic | チャンネルトピックを取得
[**get_channel_viewers**](ChannelApi.md#get_channel_viewers) | **GET** /channels/{channelId}/viewers | チャンネル閲覧者リストを取得
[**get_channels**](ChannelApi.md#get_channels) | **GET** /channels | チャンネルリストを取得
[**get_messages**](ChannelApi.md#get_messages) | **GET** /channels/{channelId}/messages | チャンネルメッセージのリストを取得
[**get_user_dm_channel**](ChannelApi.md#get_user_dm_channel) | **GET** /users/{userId}/dm-channel | DMチャンネル情報を取得
[**post_message**](ChannelApi.md#post_message) | **POST** /channels/{channelId}/messages | チャンネルにメッセージを投稿
[**set_channel_subscribers**](ChannelApi.md#set_channel_subscribers) | **PUT** /channels/{channelId}/subscribers | チャンネルの通知購読者を設定


# **create_channel**
> Channel create_channel()

チャンネルを作成

チャンネルを作成します。 階層が6以上になるチャンネルは作成できません。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.channel import Channel
from traq.model.post_channel_request import PostChannelRequest
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
    api_instance = channel_api.ChannelApi(api_client)
    post_channel_request = PostChannelRequest(
        name="z",
        parent="parent_example",
    ) # PostChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルを作成
        api_response = api_instance.create_channel(post_channel_request=post_channel_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->create_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_channel_request** | [**PostChannelRequest**](PostChannelRequest.md)|  | [optional]

### Return type

[**Channel**](Channel.md)

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
**403** | Forbidden |  -  |
**409** | Conflict 指定した名前のチャンネルは既に存在しています。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_channel**
> edit_channel(channel_id)

チャンネル情報を変更

指定したチャンネルの情報を変更します。 変更には権限が必要です。 ルートチャンネルに移動させる場合は、`parent`に`00000000-0000-0000-0000-000000000000`を指定してください。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.patch_channel_request import PatchChannelRequest
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID
    patch_channel_request = PatchChannelRequest(
        name="z",
        archived=True,
        force=True,
        parent="parent_example",
    ) # PatchChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # チャンネル情報を変更
        api_instance.edit_channel(channel_id)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->edit_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネル情報を変更
        api_instance.edit_channel(channel_id, patch_channel_request=patch_channel_request)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->edit_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |
 **patch_channel_request** | [**PatchChannelRequest**](PatchChannelRequest.md)|  | [optional]

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict 変更後の名前のチャンネルが既に存在しています。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_channel_subscribers**
> edit_channel_subscribers(channel_id)

チャンネルの通知購読者を編集

指定したチャンネルの通知購読者を編集します。 リクエストに含めなかったユーザーの通知購読状態は変更しません。 また、存在しないユーザーを指定した場合は無視されます。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.patch_channel_subscribers_request import PatchChannelSubscribersRequest
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID
    patch_channel_subscribers_request = PatchChannelSubscribersRequest(
        on=[
            "on_example",
        ],
        off=[
            "off_example",
        ],
    ) # PatchChannelSubscribersRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # チャンネルの通知購読者を編集
        api_instance.edit_channel_subscribers(channel_id)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->edit_channel_subscribers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルの通知購読者を編集
        api_instance.edit_channel_subscribers(channel_id, patch_channel_subscribers_request=patch_channel_subscribers_request)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->edit_channel_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |
 **patch_channel_subscribers_request** | [**PatchChannelSubscribersRequest**](PatchChannelSubscribersRequest.md)|  | [optional]

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
**204** | No Content 変更できました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden 指定したチャンネルの通知購読者は変更できません。 |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_channel_topic**
> edit_channel_topic(channel_id)

チャンネルトピックを編集

指定したチャンネルのトピックを編集します。 アーカイブされているチャンネルのトピックは編集できません。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.put_channel_topic_request import PutChannelTopicRequest
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID
    put_channel_topic_request = PutChannelTopicRequest(
        topic="topic_example",
    ) # PutChannelTopicRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # チャンネルトピックを編集
        api_instance.edit_channel_topic(channel_id)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->edit_channel_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルトピックを編集
        api_instance.edit_channel_topic(channel_id, put_channel_topic_request=put_channel_topic_request)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->edit_channel_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |
 **put_channel_topic_request** | [**PutChannelTopicRequest**](PutChannelTopicRequest.md)|  | [optional]

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
**204** | No Content チャンネルトピックが編集されました |  -  |
**400** | Bad Request |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel**
> Channel get_channel(channel_id)

チャンネル情報を取得

指定したチャンネルの情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.channel import Channel
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID

    # example passing only required values which don't have defaults set
    try:
        # チャンネル情報を取得
        api_response = api_instance.get_channel(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |

### Return type

[**Channel**](Channel.md)

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

# **get_channel_bots**
> [BotUser] get_channel_bots(channel_id)

チャンネル参加中のBOTのリストを取得

指定したチャンネルに参加しているBOTのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.bot_user import BotUser
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID

    # example passing only required values which don't have defaults set
    try:
        # チャンネル参加中のBOTのリストを取得
        api_response = api_instance.get_channel_bots(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_channel_bots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |

### Return type

[**[BotUser]**](BotUser.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_events**
> [ChannelEvent] get_channel_events(channel_id)

チャンネルイベントのリストを取得

指定したチャンネルのイベントリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.channel_event import ChannelEvent
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID
    limit = 50 # int | 取得する件数 (optional)
    offset = 150 # int | 取得するオフセット (optional) if omitted the server will use the default value of 0
    since = dateutil_parser('2016-10-12T11:00:00.000000Z') # datetime | 取得する時間範囲の開始日時 (optional) if omitted the server will use the default value of dateutil_parser('0000-01-01T00:00:00Z')
    until = dateutil_parser('2016-10-12T11:00:00.0000000Z') # datetime | 取得する時間範囲の終了日時 (optional)
    inclusive = False # bool | 範囲の端を含めるかどうか (optional) if omitted the server will use the default value of False
    order = "desc" # str | 昇順か降順か (optional) if omitted the server will use the default value of "desc"

    # example passing only required values which don't have defaults set
    try:
        # チャンネルイベントのリストを取得
        api_response = api_instance.get_channel_events(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_channel_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルイベントのリストを取得
        api_response = api_instance.get_channel_events(channel_id, limit=limit, offset=offset, since=since, until=until, inclusive=inclusive, order=order)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_channel_events: %s\n" % e)
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

[**[ChannelEvent]**](ChannelEvent.md)

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

# **get_channel_pins**
> [Pin] get_channel_pins(channel_id)

チャンネルピンのリストを取得

指定したチャンネルにピン留めされているピンメッセージのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.pin import Pin
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID

    # example passing only required values which don't have defaults set
    try:
        # チャンネルピンのリストを取得
        api_response = api_instance.get_channel_pins(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_channel_pins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |

### Return type

[**[Pin]**](Pin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_stats**
> ChannelStats get_channel_stats(channel_id)

チャンネル統計情報を取得

指定したチャンネルの統計情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.channel_stats import ChannelStats
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID

    # example passing only required values which don't have defaults set
    try:
        # チャンネル統計情報を取得
        api_response = api_instance.get_channel_stats(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_channel_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |

### Return type

[**ChannelStats**](ChannelStats.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_subscribers**
> [str] get_channel_subscribers(channel_id)

チャンネルの通知購読者のリストを取得

指定したチャンネルを通知購読しているユーザーのUUIDのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID

    # example passing only required values which don't have defaults set
    try:
        # チャンネルの通知購読者のリストを取得
        api_response = api_instance.get_channel_subscribers(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_channel_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |

### Return type

**[str]**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden プライベートチャンネル・強制通知チャンネルの設定は取得できません。 |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_topic**
> ChannelTopic get_channel_topic(channel_id)

チャンネルトピックを取得

指定したチャンネルのトピックを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.channel_topic import ChannelTopic
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID

    # example passing only required values which don't have defaults set
    try:
        # チャンネルトピックを取得
        api_response = api_instance.get_channel_topic(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_channel_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |

### Return type

[**ChannelTopic**](ChannelTopic.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_viewers**
> [ChannelViewer] get_channel_viewers(channel_id)

チャンネル閲覧者リストを取得

指定したチャンネルの閲覧者のリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.channel_viewer import ChannelViewer
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID

    # example passing only required values which don't have defaults set
    try:
        # チャンネル閲覧者リストを取得
        api_response = api_instance.get_channel_viewers(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_channel_viewers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |

### Return type

[**[ChannelViewer]**](ChannelViewer.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channels**
> ChannelList get_channels()

チャンネルリストを取得

チャンネルのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.channel_list import ChannelList
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
    api_instance = channel_api.ChannelApi(api_client)
    include_dm = False # bool | ダイレクトメッセージチャンネルをレスポンスに含めるかどうか (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルリストを取得
        api_response = api_instance.get_channels(include_dm=include_dm)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_dm** | **bool**| ダイレクトメッセージチャンネルをレスポンスに含めるかどうか | [optional] if omitted the server will use the default value of False

### Return type

[**ChannelList**](ChannelList.md)

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

# **get_messages**
> [Message] get_messages(channel_id)

チャンネルメッセージのリストを取得

指定したチャンネルのメッセージのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
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
    api_instance = channel_api.ChannelApi(api_client)
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
        print("Exception when calling ChannelApi->get_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルメッセージのリストを取得
        api_response = api_instance.get_messages(channel_id, limit=limit, offset=offset, since=since, until=until, inclusive=inclusive, order=order)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_messages: %s\n" % e)
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

# **get_user_dm_channel**
> DMChannel get_user_dm_channel(user_id)

DMチャンネル情報を取得

指定したユーザーとのダイレクトメッセージチャンネルの情報を返します。 ダイレクトメッセージチャンネルが存在しなかった場合、自動的に作成されます。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.dm_channel import DMChannel
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
    api_instance = channel_api.ChannelApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # DMチャンネル情報を取得
        api_response = api_instance.get_user_dm_channel(user_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->get_user_dm_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

[**DMChannel**](DMChannel.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found ユーザーが見つかりません。  |  -  |

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
from traq.api import channel_api
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
    api_instance = channel_api.ChannelApi(api_client)
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
        print("Exception when calling ChannelApi->post_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルにメッセージを投稿
        api_response = api_instance.post_message(channel_id, post_message_request=post_message_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->post_message: %s\n" % e)
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

# **set_channel_subscribers**
> set_channel_subscribers(channel_id)

チャンネルの通知購読者を設定

指定したチャンネルの通知購読者を設定します。 リクエストに含めなかったユーザーの通知購読状態はオフになります。 また、存在しないユーザーを指定した場合は無視されます。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import channel_api
from traq.model.put_channel_subscribers_request import PutChannelSubscribersRequest
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
    api_instance = channel_api.ChannelApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID
    put_channel_subscribers_request = PutChannelSubscribersRequest(
        on=[
            "on_example",
        ],
    ) # PutChannelSubscribersRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # チャンネルの通知購読者を設定
        api_instance.set_channel_subscribers(channel_id)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->set_channel_subscribers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルの通知購読者を設定
        api_instance.set_channel_subscribers(channel_id, put_channel_subscribers_request=put_channel_subscribers_request)
    except traq.ApiException as e:
        print("Exception when calling ChannelApi->set_channel_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |
 **put_channel_subscribers_request** | [**PutChannelSubscribersRequest**](PutChannelSubscribersRequest.md)|  | [optional]

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
**204** | No Content 変更されました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden 指定したチャンネルの通知購読者は変更できません。 |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

