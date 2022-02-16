# traq.BotApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_bot**](BotApi.md#activate_bot) | **POST** /bots/{botId}/actions/activate | BOTをアクティベート
[**change_bot_icon**](BotApi.md#change_bot_icon) | **PUT** /bots/{botId}/icon | BOTのアイコン画像を変更
[**connect_bot_ws**](BotApi.md#connect_bot_ws) | **GET** /bots/ws | WebSocket Mode BOT用通知ストリームに接続します
[**create_bot**](BotApi.md#create_bot) | **POST** /bots | BOTを作成
[**delete_bot**](BotApi.md#delete_bot) | **DELETE** /bots/{botId} | BOTを削除
[**edit_bot**](BotApi.md#edit_bot) | **PATCH** /bots/{botId} | BOT情報を変更
[**get_bot**](BotApi.md#get_bot) | **GET** /bots/{botId} | BOT情報を取得
[**get_bot_icon**](BotApi.md#get_bot_icon) | **GET** /bots/{botId}/icon | BOTのアイコン画像を取得
[**get_bot_logs**](BotApi.md#get_bot_logs) | **GET** /bots/{botId}/logs | BOTのイベントログを取得
[**get_bots**](BotApi.md#get_bots) | **GET** /bots | BOTリストを取得
[**get_channel_bots**](BotApi.md#get_channel_bots) | **GET** /channels/{channelId}/bots | チャンネル参加中のBOTのリストを取得
[**inactivate_bot**](BotApi.md#inactivate_bot) | **POST** /bots/{botId}/actions/inactivate | BOTをインアクティベート
[**let_bot_join_channel**](BotApi.md#let_bot_join_channel) | **POST** /bots/{botId}/actions/join | BOTをチャンネルに参加させる
[**let_bot_leave_channel**](BotApi.md#let_bot_leave_channel) | **POST** /bots/{botId}/actions/leave | BOTをチャンネルから退出させる
[**reissue_bot**](BotApi.md#reissue_bot) | **POST** /bots/{botId}/actions/reissue | BOTのトークンを再発行


# **activate_bot**
> activate_bot(bot_id)

BOTをアクティベート

指定したBOTを有効化します。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID

    # example passing only required values which don't have defaults set
    try:
        # BOTをアクティベート
        api_instance.activate_bot(bot_id)
    except traq.ApiException as e:
        print("Exception when calling BotApi->activate_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |

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
**202** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_bot_icon**
> change_bot_icon(bot_id, file)

BOTのアイコン画像を変更

指定したBOTのアイコン画像を変更を変更します。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID
    file = open('/path/to/file', 'rb') # file_type | アイコン画像(1MBまでのpng, jpeg, gif)

    # example passing only required values which don't have defaults set
    try:
        # BOTのアイコン画像を変更
        api_instance.change_bot_icon(bot_id, file)
    except traq.ApiException as e:
        print("Exception when calling BotApi->change_bot_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |
 **file** | **file_type**| アイコン画像(1MBまでのpng, jpeg, gif) |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content 変更されました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |
**413** | Request Entity Too Large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_bot_ws**
> connect_bot_ws()

WebSocket Mode BOT用通知ストリームに接続します

# BOT WebSocketプロトコル  ## 送信  `コマンド:引数1:引数2:...` のような形式のTextMessageをサーバーに送信することで、このWebSocketセッションに対する設定が実行できます。  ### `rtcstate`コマンド 自分のWebRTC状態を変更します。 他のコネクションが既に状態を保持している場合、変更することができません。  `rtcstate:{チャンネルID}:({状態}:{セッションID})*`  チャンネルIDにnullもしくは空文字を指定するか、状態にnullもしくは空文字を指定した場合、WebRTC状態はリセットされます。  `rtcstate:null`, `rtcstate:`, `rtcstate:channelId:null`, `rtcstate:channelId:`  コネクションが切断された場合、自分のWebRTC状態はリセットされます。  ## 受信  TextMessageとして各種イベントが`type`、`reqId`、`body`を持つJSONとして非同期に送られます。 `body`の内容はHTTP Modeの場合のRequest Bodyと同様です。 例外として`ERROR`イベントは`reqId`を持ちません。  例: PINGイベント `{\"type\":\"PING\",\"reqId\":\"requestId\",\"body\":{\"eventTime\":\"2019-05-07T04:50:48.582586882Z\"}}`  ### `ERROR`  コマンドの引数が不正などの理由でコマンドが受理されなかった場合に送られます。 非同期に送られるため、必ずしもコマンドとの対応関係を確定できないことに注意してください。 本番環境ではERRORが送られないようにすることが望ましいです。  `{\"type\":\"ERROR\",\"body\":\"message\"}`

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
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
    api_instance = bot_api.BotApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # WebSocket Mode BOT用通知ストリームに接続します
        api_instance.connect_bot_ws()
    except traq.ApiException as e:
        print("Exception when calling BotApi->connect_bot_ws: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**101** | Switching Protocols |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bot**
> BotDetail create_bot()

BOTを作成

BOTを作成します。 作成後に購読イベントの設定を行う必要があります。 さらにHTTP Modeの場合はアクティベーションを行う必要があります。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
from traq.model.bot_detail import BotDetail
from traq.model.post_bot_request import PostBotRequest
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
    api_instance = bot_api.BotApi(api_client)
    post_bot_request = PostBotRequest(
        name="zBAMDTMv2D2y",
        display_name="display_name_example",
        description="description_example",
        mode=BotMode("HTTP"),
        endpoint="endpoint_example",
    ) # PostBotRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # BOTを作成
        api_response = api_instance.create_bot(post_bot_request=post_bot_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling BotApi->create_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_bot_request** | [**PostBotRequest**](PostBotRequest.md)|  | [optional]

### Return type

[**BotDetail**](BotDetail.md)

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
**409** | Conflict 既に使われている名前です。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bot**
> delete_bot(bot_id)

BOTを削除

指定したBOTを削除します。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID

    # example passing only required values which don't have defaults set
    try:
        # BOTを削除
        api_instance.delete_bot(bot_id)
    except traq.ApiException as e:
        print("Exception when calling BotApi->delete_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_bot**
> edit_bot(bot_id)

BOT情報を変更

指定したBOTの情報を変更します。 対象のBOTの管理権限が必要です。 BOT開発者UUIDを変更した場合は、変更先ユーザーにBOT管理権限が移譲され、自分自身は権限を失います。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
from traq.model.patch_bot_request import PatchBotRequest
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID
    patch_bot_request = PatchBotRequest(
        display_name="display_name_example",
        description="description_example",
        privileged=True,
        mode=BotMode("HTTP"),
        endpoint="endpoint_example",
        developer_id="developer_id_example",
        subscribe_events=[
            "subscribe_events_example",
        ],
    ) # PatchBotRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # BOT情報を変更
        api_instance.edit_bot(bot_id)
    except traq.ApiException as e:
        print("Exception when calling BotApi->edit_bot: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # BOT情報を変更
        api_instance.edit_bot(bot_id, patch_bot_request=patch_bot_request)
    except traq.ApiException as e:
        print("Exception when calling BotApi->edit_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |
 **patch_bot_request** | [**PatchBotRequest**](PatchBotRequest.md)|  | [optional]

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
**204** | No Content 変更しました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot**
> bool, date, datetime, dict, float, int, list, str, none_type get_bot(bot_id)

BOT情報を取得

指定したBOTのBOT情報を取得します。 BOT詳細情報を取得する場合は、対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
from traq.model.bot import Bot
from traq.model.bot_detail import BotDetail
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID
    detail = False # bool | 詳細情報を含めるかどうか (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # BOT情報を取得
        api_response = api_instance.get_bot(bot_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling BotApi->get_bot: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # BOT情報を取得
        api_response = api_instance.get_bot(bot_id, detail=detail)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling BotApi->get_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |
 **detail** | **bool**| 詳細情報を含めるかどうか | [optional] if omitted the server will use the default value of False

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_icon**
> file_type get_bot_icon(bot_id)

BOTのアイコン画像を取得

指定したBOTのアイコン画像を取得を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID

    # example passing only required values which don't have defaults set
    try:
        # BOTのアイコン画像を取得
        api_response = api_instance.get_bot_icon(bot_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling BotApi->get_bot_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |

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
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_logs**
> [BotEventLog] get_bot_logs(bot_id)

BOTのイベントログを取得

指定したBOTのイベントログを取得します。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
from traq.model.bot_event_log import BotEventLog
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID
    limit = 50 # int | 取得する件数 (optional)
    offset = 150 # int | 取得するオフセット (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # BOTのイベントログを取得
        api_response = api_instance.get_bot_logs(bot_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling BotApi->get_bot_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # BOTのイベントログを取得
        api_response = api_instance.get_bot_logs(bot_id, limit=limit, offset=offset)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling BotApi->get_bot_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |
 **limit** | **int**| 取得する件数 | [optional]
 **offset** | **int**| 取得するオフセット | [optional] if omitted the server will use the default value of 0

### Return type

[**[BotEventLog]**](BotEventLog.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bots**
> [Bot] get_bots()

BOTリストを取得

BOT情報のリストを取得します。 allを指定しない場合、自分が開発者のBOTのみを返します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
from traq.model.bot import Bot
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
    api_instance = bot_api.BotApi(api_client)
    all = False # bool | 全てのBOTを取得するかどうか (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # BOTリストを取得
        api_response = api_instance.get_bots(all=all)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling BotApi->get_bots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| 全てのBOTを取得するかどうか | [optional] if omitted the server will use the default value of False

### Return type

[**[Bot]**](Bot.md)

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

# **get_channel_bots**
> [BotUser] get_channel_bots(channel_id)

チャンネル参加中のBOTのリストを取得

指定したチャンネルに参加しているBOTのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
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
    api_instance = bot_api.BotApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID

    # example passing only required values which don't have defaults set
    try:
        # チャンネル参加中のBOTのリストを取得
        api_response = api_instance.get_channel_bots(channel_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling BotApi->get_channel_bots: %s\n" % e)
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

# **inactivate_bot**
> inactivate_bot(bot_id)

BOTをインアクティベート

指定したBOTを無効化します。対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID

    # example passing only required values which don't have defaults set
    try:
        # BOTをインアクティベート
        api_instance.inactivate_bot(bot_id)
    except traq.ApiException as e:
        print("Exception when calling BotApi->inactivate_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |

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
**204** | No Content BOTがインアクティベートされました。 |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **let_bot_join_channel**
> let_bot_join_channel(bot_id)

BOTをチャンネルに参加させる

指定したBOTを指定したチャンネルに参加させます。 チャンネルに参加したBOTは、そのチャンネルの各種イベントを受け取るようになります。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
from traq.model.post_bot_action_join_request import PostBotActionJoinRequest
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID
    post_bot_action_join_request = PostBotActionJoinRequest(
        channel_id="channel_id_example",
    ) # PostBotActionJoinRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # BOTをチャンネルに参加させる
        api_instance.let_bot_join_channel(bot_id)
    except traq.ApiException as e:
        print("Exception when calling BotApi->let_bot_join_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # BOTをチャンネルに参加させる
        api_instance.let_bot_join_channel(bot_id, post_bot_action_join_request=post_bot_action_join_request)
    except traq.ApiException as e:
        print("Exception when calling BotApi->let_bot_join_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |
 **post_bot_action_join_request** | [**PostBotActionJoinRequest**](PostBotActionJoinRequest.md)|  | [optional]

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
**204** | No Content BOTを参加させました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **let_bot_leave_channel**
> let_bot_leave_channel(bot_id)

BOTをチャンネルから退出させる

指定したBOTを指定したチャンネルから退出させます。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
from traq.model.post_bot_action_leave_request import PostBotActionLeaveRequest
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID
    post_bot_action_leave_request = PostBotActionLeaveRequest(
        channel_id="channel_id_example",
    ) # PostBotActionLeaveRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # BOTをチャンネルから退出させる
        api_instance.let_bot_leave_channel(bot_id)
    except traq.ApiException as e:
        print("Exception when calling BotApi->let_bot_leave_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # BOTをチャンネルから退出させる
        api_instance.let_bot_leave_channel(bot_id, post_bot_action_leave_request=post_bot_action_leave_request)
    except traq.ApiException as e:
        print("Exception when calling BotApi->let_bot_leave_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |
 **post_bot_action_leave_request** | [**PostBotActionLeaveRequest**](PostBotActionLeaveRequest.md)|  | [optional]

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
**204** | No Content BOTを退出させました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reissue_bot**
> BotTokens reissue_bot(bot_id)

BOTのトークンを再発行

指定したBOTの現在の各種トークンを無効化し、再発行を行います。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import bot_api
from traq.model.bot_tokens import BotTokens
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
    api_instance = bot_api.BotApi(api_client)
    bot_id = "botId_example" # str | BOTUUID

    # example passing only required values which don't have defaults set
    try:
        # BOTのトークンを再発行
        api_response = api_instance.reissue_bot(bot_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling BotApi->reissue_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID |

### Return type

[**BotTokens**](BotTokens.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

