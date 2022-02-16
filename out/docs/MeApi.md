# traq.MeApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_my_star**](MeApi.md#add_my_star) | **POST** /users/me/stars | チャンネルをスターに追加
[**add_my_user_tag**](MeApi.md#add_my_user_tag) | **POST** /users/me/tags | 自分にタグを追加
[**change_my_icon**](MeApi.md#change_my_icon) | **PUT** /users/me/icon | 自分のアイコン画像を変更
[**change_my_notify_citation**](MeApi.md#change_my_notify_citation) | **PUT** /users/me/settings/notify-citation | メッセージ引用通知の設定情報を変更
[**change_my_password**](MeApi.md#change_my_password) | **PUT** /users/me/password | 自分のパスワードを変更
[**edit_me**](MeApi.md#edit_me) | **PATCH** /users/me | 自分のユーザー情報を変更
[**edit_my_user_tag**](MeApi.md#edit_my_user_tag) | **PATCH** /users/me/tags/{tagId} | 自分のタグを編集
[**get_me**](MeApi.md#get_me) | **GET** /users/me | 自分のユーザー詳細を取得
[**get_my_channel_subscriptions**](MeApi.md#get_my_channel_subscriptions) | **GET** /users/me/subscriptions | 自分のチャンネル購読状態を取得
[**get_my_external_accounts**](MeApi.md#get_my_external_accounts) | **GET** /users/me/ex-accounts | 外部ログインアカウント一覧を取得
[**get_my_icon**](MeApi.md#get_my_icon) | **GET** /users/me/icon | 自分のアイコン画像を取得
[**get_my_notify_citation**](MeApi.md#get_my_notify_citation) | **GET** /users/me/settings/notify-citation | メッセージ引用通知の設定情報を取得
[**get_my_qr_code**](MeApi.md#get_my_qr_code) | **GET** /users/me/qr-code | QRコードを取得
[**get_my_sessions**](MeApi.md#get_my_sessions) | **GET** /users/me/sessions | 自分のログインセッションリストを取得
[**get_my_stamp_history**](MeApi.md#get_my_stamp_history) | **GET** /users/me/stamp-history | スタンプ履歴を取得
[**get_my_stars**](MeApi.md#get_my_stars) | **GET** /users/me/stars | スターチャンネルリストを取得
[**get_my_tokens**](MeApi.md#get_my_tokens) | **GET** /users/me/tokens | 有効トークンのリストを取得
[**get_my_unread_channels**](MeApi.md#get_my_unread_channels) | **GET** /users/me/unread | 未読チャンネルを取得
[**get_my_user_tags**](MeApi.md#get_my_user_tags) | **GET** /users/me/tags | 自分のタグリストを取得
[**get_my_view_states**](MeApi.md#get_my_view_states) | **GET** /users/me/view-states | 自身のチャンネル閲覧状態一覧を取得
[**get_user_settings**](MeApi.md#get_user_settings) | **GET** /users/me/settings | ユーザー設定を取得
[**link_external_account**](MeApi.md#link_external_account) | **POST** /users/me/ex-accounts/link | 外部ログインアカウントを紐付ける
[**read_channel**](MeApi.md#read_channel) | **DELETE** /users/me/unread/{channelId} | チャンネルを既読にする
[**register_fcm_device**](MeApi.md#register_fcm_device) | **POST** /users/me/fcm-device | FCMデバイスを登録
[**remove_my_star**](MeApi.md#remove_my_star) | **DELETE** /users/me/stars/{channelId} | チャンネルをスターから削除します
[**remove_my_user_tag**](MeApi.md#remove_my_user_tag) | **DELETE** /users/me/tags/{tagId} | 自分からタグを削除します
[**revoke_my_session**](MeApi.md#revoke_my_session) | **DELETE** /users/me/sessions/{sessionId} | セッションを無効化
[**revoke_my_token**](MeApi.md#revoke_my_token) | **DELETE** /users/me/tokens/{tokenId} | トークンの認可を取り消す
[**set_channel_subscribe_level**](MeApi.md#set_channel_subscribe_level) | **PUT** /users/me/subscriptions/{channelId} | チャンネル購読レベルを設定
[**unlink_external_account**](MeApi.md#unlink_external_account) | **POST** /users/me/ex-accounts/unlink | 外部ログインアカウントの紐付けを解除


# **add_my_star**
> add_my_star()

チャンネルをスターに追加

指定したチャンネルをスターチャンネルに追加します。 不正なチャンネルIDを指定した場合、400を返します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.post_star_request import PostStarRequest
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
    api_instance = me_api.MeApi(api_client)
    post_star_request = PostStarRequest(
        channel_id="channel_id_example",
    ) # PostStarRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネルをスターに追加
        api_instance.add_my_star(post_star_request=post_star_request)
    except traq.ApiException as e:
        print("Exception when calling MeApi->add_my_star: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_star_request** | [**PostStarRequest**](PostStarRequest.md)|  | [optional]

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
**204** | No Content スターしました。 |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_my_user_tag**
> UserTag add_my_user_tag()

自分にタグを追加

自分に新しくタグを追加します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.user_tag import UserTag
from traq.model.post_user_tag_request import PostUserTagRequest
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
    api_instance = me_api.MeApi(api_client)
    post_user_tag_request = PostUserTagRequest(
        tag="tag_example",
    ) # PostUserTagRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 自分にタグを追加
        api_response = api_instance.add_my_user_tag(post_user_tag_request=post_user_tag_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->add_my_user_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_user_tag_request** | [**PostUserTagRequest**](PostUserTagRequest.md)|  | [optional]

### Return type

[**UserTag**](UserTag.md)

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
**409** | Conflict 既に追加されています。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_my_icon**
> change_my_icon(file)

自分のアイコン画像を変更

自分のアイコン画像を変更します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
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
    api_instance = me_api.MeApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | アイコン画像(1MBまでのpng, jpeg, gif)

    # example passing only required values which don't have defaults set
    try:
        # 自分のアイコン画像を変更
        api_instance.change_my_icon(file)
    except traq.ApiException as e:
        print("Exception when calling MeApi->change_my_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**413** | Request Entity Too Large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_my_notify_citation**
> change_my_notify_citation()

メッセージ引用通知の設定情報を変更

メッセージ引用通知の設定情報を変更します

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.put_notify_citation_request import PutNotifyCitationRequest
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
    api_instance = me_api.MeApi(api_client)
    put_notify_citation_request = PutNotifyCitationRequest(
        notify_citation=True,
    ) # PutNotifyCitationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # メッセージ引用通知の設定情報を変更
        api_instance.change_my_notify_citation(put_notify_citation_request=put_notify_citation_request)
    except traq.ApiException as e:
        print("Exception when calling MeApi->change_my_notify_citation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_notify_citation_request** | [**PutNotifyCitationRequest**](PutNotifyCitationRequest.md)|  | [optional]

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
**204** | 変更できました。 |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_my_password**
> change_my_password()

自分のパスワードを変更

自身のパスワードを変更します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.put_my_password_request import PutMyPasswordRequest
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
    api_instance = me_api.MeApi(api_client)
    put_my_password_request = PutMyPasswordRequest(
        password="jUR,rZ#UM/?R,Fp^",
        new_password="jUR,rZ#UM/?R,Fp^",
    ) # PutMyPasswordRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 自分のパスワードを変更
        api_instance.change_my_password(put_my_password_request=put_my_password_request)
    except traq.ApiException as e:
        print("Exception when calling MeApi->change_my_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_my_password_request** | [**PutMyPasswordRequest**](PutMyPasswordRequest.md)|  | [optional]

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
**401** | Unauthorized 現在のパスワードが違います。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_me**
> edit_me()

自分のユーザー情報を変更

自身のユーザー情報を変更します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.patch_me_request import PatchMeRequest
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
    api_instance = me_api.MeApi(api_client)
    patch_me_request = PatchMeRequest(
        display_name="display_name_example",
        twitter_id="HqXzyC",
        bio="bio_example",
        home_channel="home_channel_example",
    ) # PatchMeRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 自分のユーザー情報を変更
        api_instance.edit_me(patch_me_request=patch_me_request)
    except traq.ApiException as e:
        print("Exception when calling MeApi->edit_me: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_me_request** | [**PatchMeRequest**](PatchMeRequest.md)|  | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_my_user_tag**
> edit_my_user_tag(tag_id)

自分のタグを編集

自分の指定したタグの状態を変更します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.patch_user_tag_request import PatchUserTagRequest
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
    api_instance = me_api.MeApi(api_client)
    tag_id = "tagId_example" # str | タグUUID
    patch_user_tag_request = PatchUserTagRequest(
        is_locked=True,
    ) # PatchUserTagRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 自分のタグを編集
        api_instance.edit_my_user_tag(tag_id)
    except traq.ApiException as e:
        print("Exception when calling MeApi->edit_my_user_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 自分のタグを編集
        api_instance.edit_my_user_tag(tag_id, patch_user_tag_request=patch_user_tag_request)
    except traq.ApiException as e:
        print("Exception when calling MeApi->edit_my_user_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| タグUUID |
 **patch_user_tag_request** | [**PatchUserTagRequest**](PatchUserTagRequest.md)|  | [optional]

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
**404** | Not Found タグが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_me**
> MyUserDetail get_me()

自分のユーザー詳細を取得

自身のユーザー詳細情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.my_user_detail import MyUserDetail
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 自分のユーザー詳細を取得
        api_response = api_instance.get_me()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_me: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MyUserDetail**](MyUserDetail.md)

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

# **get_my_channel_subscriptions**
> [UserSubscribeState] get_my_channel_subscriptions()

自分のチャンネル購読状態を取得

自身のチャンネル購読状態を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.user_subscribe_state import UserSubscribeState
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 自分のチャンネル購読状態を取得
        api_response = api_instance.get_my_channel_subscriptions()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_channel_subscriptions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[UserSubscribeState]**](UserSubscribeState.md)

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

# **get_my_external_accounts**
> [ExternalProviderUser] get_my_external_accounts()

外部ログインアカウント一覧を取得

自分に紐付けられている外部ログインアカウント一覧を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.external_provider_user import ExternalProviderUser
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 外部ログインアカウント一覧を取得
        api_response = api_instance.get_my_external_accounts()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_external_accounts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ExternalProviderUser]**](ExternalProviderUser.md)

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

# **get_my_icon**
> file_type get_my_icon()

自分のアイコン画像を取得

自分のアイコン画像を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 自分のアイコン画像を取得
        api_response = api_instance.get_my_icon()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_icon: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**404** | Not Found ユーザーが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_notify_citation**
> GetNotifyCitation get_my_notify_citation()

メッセージ引用通知の設定情報を取得

メッセージ引用通知の設定情報を変更します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.get_notify_citation import GetNotifyCitation
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # メッセージ引用通知の設定情報を取得
        api_response = api_instance.get_my_notify_citation()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_notify_citation: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNotifyCitation**](GetNotifyCitation.md)

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

# **get_my_qr_code**
> file_type get_my_qr_code()

QRコードを取得

自身のQRコードを取得します。 返されたQRコードまたはトークンは、発行後の5分間のみ有効です

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
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
    api_instance = me_api.MeApi(api_client)
    token = False # bool | 画像でなくトークン文字列で返すかどうか (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # QRコードを取得
        api_response = api_instance.get_my_qr_code(token=token)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_qr_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **bool**| 画像でなくトークン文字列で返すかどうか | [optional] if omitted the server will use the default value of False

### Return type

**file_type**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_sessions**
> [LoginSession] get_my_sessions()

自分のログインセッションリストを取得

自分のログインセッションのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.login_session import LoginSession
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 自分のログインセッションリストを取得
        api_response = api_instance.get_my_sessions()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_sessions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[LoginSession]**](LoginSession.md)

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

# **get_my_stamp_history**
> [StampHistoryEntry] get_my_stamp_history()

スタンプ履歴を取得

自分のスタンプ履歴を最大100件まで取得します。 結果は降順で返されます。  このAPIが返すスタンプ履歴は厳密な履歴ではありません。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.stamp_history_entry import StampHistoryEntry
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
    api_instance = me_api.MeApi(api_client)
    limit = 100 # int | 件数 (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # スタンプ履歴を取得
        api_response = api_instance.get_my_stamp_history(limit=limit)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_stamp_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 件数 | [optional] if omitted the server will use the default value of 100

### Return type

[**[StampHistoryEntry]**](StampHistoryEntry.md)

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

# **get_my_stars**
> [str] get_my_stars()

スターチャンネルリストを取得

自分がスターしているチャンネルのUUIDの配列を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # スターチャンネルリストを取得
        api_response = api_instance.get_my_stars()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_stars: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_tokens**
> [ActiveOAuth2Token] get_my_tokens()

有効トークンのリストを取得

有効な自分に発行されたOAuth2トークンのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.active_o_auth2_token import ActiveOAuth2Token
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 有効トークンのリストを取得
        api_response = api_instance.get_my_tokens()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_tokens: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ActiveOAuth2Token]**](ActiveOAuth2Token.md)

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

# **get_my_unread_channels**
> [UnreadChannel] get_my_unread_channels()

未読チャンネルを取得

自分が現在未読のチャンネルの未読情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.unread_channel import UnreadChannel
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 未読チャンネルを取得
        api_response = api_instance.get_my_unread_channels()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_unread_channels: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[UnreadChannel]**](UnreadChannel.md)

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

# **get_my_user_tags**
> [UserTag] get_my_user_tags()

自分のタグリストを取得

自分に付けられているタグの配列を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.user_tag import UserTag
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 自分のタグリストを取得
        api_response = api_instance.get_my_user_tags()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_user_tags: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[UserTag]**](UserTag.md)

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

# **get_my_view_states**
> [MyChannelViewState] get_my_view_states()

自身のチャンネル閲覧状態一覧を取得

自身のチャンネル閲覧状態一覧を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.my_channel_view_state import MyChannelViewState
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 自身のチャンネル閲覧状態一覧を取得
        api_response = api_instance.get_my_view_states()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_my_view_states: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[MyChannelViewState]**](MyChannelViewState.md)

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

# **get_user_settings**
> UserSettings get_user_settings()

ユーザー設定を取得

ユーザー設定を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.user_settings import UserSettings
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
    api_instance = me_api.MeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ユーザー設定を取得
        api_response = api_instance.get_user_settings()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling MeApi->get_user_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserSettings**](UserSettings.md)

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

# **link_external_account**
> link_external_account()

外部ログインアカウントを紐付ける

自分に外部ログインアカウントを紐付けます。 指定した`providerName`がサーバー側で有効である必要があります。 リクエストが受理された場合、外部サービスの認証画面にリダイレクトされ、認証される必要があります。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.post_link_external_account import PostLinkExternalAccount
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
    api_instance = me_api.MeApi(api_client)
    post_link_external_account = PostLinkExternalAccount(
        provider_name="provider_name_example",
    ) # PostLinkExternalAccount |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 外部ログインアカウントを紐付ける
        api_instance.link_external_account(post_link_external_account=post_link_external_account)
    except traq.ApiException as e:
        print("Exception when calling MeApi->link_external_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_link_external_account** | [**PostLinkExternalAccount**](PostLinkExternalAccount.md)|  | [optional]

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
**302** | Found 外部サービスの認証画面に遷移します。 |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_channel**
> read_channel(channel_id)

チャンネルを既読にする

自分が未読のチャンネルを既読にします。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
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
    api_instance = me_api.MeApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID

    # example passing only required values which don't have defaults set
    try:
        # チャンネルを既読にする
        api_instance.read_channel(channel_id)
    except traq.ApiException as e:
        print("Exception when calling MeApi->read_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |

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
**204** | No Content 既読にしました。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_fcm_device**
> register_fcm_device()

FCMデバイスを登録

自身のFCMデバイスを登録します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.post_my_fcm_device_request import PostMyFCMDeviceRequest
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
    api_instance = me_api.MeApi(api_client)
    post_my_fcm_device_request = PostMyFCMDeviceRequest(
        token="bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1",
    ) # PostMyFCMDeviceRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # FCMデバイスを登録
        api_instance.register_fcm_device(post_my_fcm_device_request=post_my_fcm_device_request)
    except traq.ApiException as e:
        print("Exception when calling MeApi->register_fcm_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_my_fcm_device_request** | [**PostMyFCMDeviceRequest**](PostMyFCMDeviceRequest.md)|  | [optional]

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
**204** | No Content 登録できました。 |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_my_star**
> remove_my_star(channel_id)

チャンネルをスターから削除します

既にスターから削除されているチャンネルを指定した場合は204を返します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
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
    api_instance = me_api.MeApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID

    # example passing only required values which don't have defaults set
    try:
        # チャンネルをスターから削除します
        api_instance.remove_my_star(channel_id)
    except traq.ApiException as e:
        print("Exception when calling MeApi->remove_my_star: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |

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
**204** | No Content 削除されました。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_my_user_tag**
> remove_my_user_tag(tag_id)

自分からタグを削除します

既に存在しないタグを削除しようとした場合は204を返します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
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
    api_instance = me_api.MeApi(api_client)
    tag_id = "tagId_example" # str | タグUUID

    # example passing only required values which don't have defaults set
    try:
        # 自分からタグを削除します
        api_instance.remove_my_user_tag(tag_id)
    except traq.ApiException as e:
        print("Exception when calling MeApi->remove_my_user_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| タグUUID |

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
**204** | No Content 削除されました。 |  -  |
**403** | Forbidden タグがロックされています。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_my_session**
> revoke_my_session(session_id)

セッションを無効化

指定した自分のセッションを無効化(ログアウト)します。 既に存在しない・無効化されているセッションを指定した場合も`204`を返します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
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
    api_instance = me_api.MeApi(api_client)
    session_id = "sessionId_example" # str | セッションUUID

    # example passing only required values which don't have defaults set
    try:
        # セッションを無効化
        api_instance.revoke_my_session(session_id)
    except traq.ApiException as e:
        print("Exception when calling MeApi->revoke_my_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| セッションUUID |

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
**204** | No Content 無効化しました。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_my_token**
> revoke_my_token(token_id)

トークンの認可を取り消す

自分の指定したトークンの認可を取り消します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
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
    api_instance = me_api.MeApi(api_client)
    token_id = "tokenId_example" # str | OAuth2トークンUUID

    # example passing only required values which don't have defaults set
    try:
        # トークンの認可を取り消す
        api_instance.revoke_my_token(token_id)
    except traq.ApiException as e:
        print("Exception when calling MeApi->revoke_my_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| OAuth2トークンUUID |

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
**204** | No Content 取り消しました。 |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_channel_subscribe_level**
> set_channel_subscribe_level(channel_id)

チャンネル購読レベルを設定

自身の指定したチャンネルの購読レベルを設定します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.put_channel_subscribe_level_request import PutChannelSubscribeLevelRequest
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
    api_instance = me_api.MeApi(api_client)
    channel_id = "channelId_example" # str | チャンネルUUID
    put_channel_subscribe_level_request = PutChannelSubscribeLevelRequest(
        level=ChannelSubscribeLevel(0),
    ) # PutChannelSubscribeLevelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # チャンネル購読レベルを設定
        api_instance.set_channel_subscribe_level(channel_id)
    except traq.ApiException as e:
        print("Exception when calling MeApi->set_channel_subscribe_level: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # チャンネル購読レベルを設定
        api_instance.set_channel_subscribe_level(channel_id, put_channel_subscribe_level_request=put_channel_subscribe_level_request)
    except traq.ApiException as e:
        print("Exception when calling MeApi->set_channel_subscribe_level: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID |
 **put_channel_subscribe_level_request** | [**PutChannelSubscribeLevelRequest**](PutChannelSubscribeLevelRequest.md)|  | [optional]

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
**403** | Forbidden 指定したチャンネルの通知購読レベルは変更できません。 |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_external_account**
> unlink_external_account()

外部ログインアカウントの紐付けを解除

自分に紐付けられている外部ログインアカウントの紐付けを解除します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import me_api
from traq.model.post_unlink_external_account import PostUnlinkExternalAccount
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
    api_instance = me_api.MeApi(api_client)
    post_unlink_external_account = PostUnlinkExternalAccount(
        provider_name="provider_name_example",
    ) # PostUnlinkExternalAccount |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 外部ログインアカウントの紐付けを解除
        api_instance.unlink_external_account(post_unlink_external_account=post_unlink_external_account)
    except traq.ApiException as e:
        print("Exception when calling MeApi->unlink_external_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_unlink_external_account** | [**PostUnlinkExternalAccount**](PostUnlinkExternalAccount.md)|  | [optional]

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
**204** | No Content 紐付けを解除しました。 |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

