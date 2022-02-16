# traq.UserApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_tag**](UserApi.md#add_user_tag) | **POST** /users/{userId}/tags | ユーザーにタグを追加
[**change_user_icon**](UserApi.md#change_user_icon) | **PUT** /users/{userId}/icon | ユーザーのアイコン画像を変更します
[**change_user_password**](UserApi.md#change_user_password) | **PUT** /users/{userId}/password | ユーザーのパスワードを変更
[**create_user**](UserApi.md#create_user) | **POST** /users | ユーザーを登録
[**edit_user**](UserApi.md#edit_user) | **PATCH** /users/{userId} | ユーザー情報を変更
[**edit_user_tag**](UserApi.md#edit_user_tag) | **PATCH** /users/{userId}/tags/{tagId} | ユーザーのタグを編集
[**get_direct_messages**](UserApi.md#get_direct_messages) | **GET** /users/{userId}/messages | ダイレクトメッセージのリストを取得
[**get_user**](UserApi.md#get_user) | **GET** /users/{userId} | ユーザー詳細情報を取得
[**get_user_dm_channel**](UserApi.md#get_user_dm_channel) | **GET** /users/{userId}/dm-channel | DMチャンネル情報を取得
[**get_user_icon**](UserApi.md#get_user_icon) | **GET** /users/{userId}/icon | ユーザーのアイコン画像を取得
[**get_user_stats**](UserApi.md#get_user_stats) | **GET** /users/{userId}/stats | ユーザー統計情報を取得
[**get_user_tags**](UserApi.md#get_user_tags) | **GET** /users/{userId}/tags | ユーザーのタグリストを取得
[**get_users**](UserApi.md#get_users) | **GET** /users | ユーザーのリストを取得
[**post_direct_message**](UserApi.md#post_direct_message) | **POST** /users/{userId}/messages | ダイレクトメッセージを送信
[**remove_user_tag**](UserApi.md#remove_user_tag) | **DELETE** /users/{userId}/tags/{tagId} | ユーザーからタグを削除します


# **add_user_tag**
> UserTag add_user_tag(user_id)

ユーザーにタグを追加

指定したユーザーに指定したタグを追加します。 Webhookユーザーにタグを追加することは出来ません。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID
    post_user_tag_request = PostUserTagRequest(
        tag="tag_example",
    ) # PostUserTagRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ユーザーにタグを追加
        api_response = api_instance.add_user_tag(user_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->add_user_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ユーザーにタグを追加
        api_response = api_instance.add_user_tag(user_id, post_user_tag_request=post_user_tag_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->add_user_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |
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
**403** | Forbidden |  -  |
**404** | Not Found ユーザーが見つかりません。 |  -  |
**409** | Conflict 既に追加されています。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_icon**
> change_user_icon(user_id, file)

ユーザーのアイコン画像を変更します

指定したユーザーのアイコン画像を変更します。 管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID
    file = open('/path/to/file', 'rb') # file_type | アイコン画像(1MBまでのpng, jpeg, gif)

    # example passing only required values which don't have defaults set
    try:
        # ユーザーのアイコン画像を変更します
        api_instance.change_user_icon(user_id, file)
    except traq.ApiException as e:
        print("Exception when calling UserApi->change_user_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |
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
**404** | Not Found ユーザーが見つかりません。 |  -  |
**413** | Request Entity Too Large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_password**
> change_user_password(user_id)

ユーザーのパスワードを変更

指定したユーザーのパスワードを変更します。 管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
from traq.model.put_user_password_request import PutUserPasswordRequest
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID
    put_user_password_request = PutUserPasswordRequest(
        new_password="jUR,rZ#UM/?R,Fp^",
    ) # PutUserPasswordRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ユーザーのパスワードを変更
        api_instance.change_user_password(user_id)
    except traq.ApiException as e:
        print("Exception when calling UserApi->change_user_password: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ユーザーのパスワードを変更
        api_instance.change_user_password(user_id, put_user_password_request=put_user_password_request)
    except traq.ApiException as e:
        print("Exception when calling UserApi->change_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |
 **put_user_password_request** | [**PutUserPasswordRequest**](PutUserPasswordRequest.md)|  | [optional]

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
**403** | Forbidden |  -  |
**404** | Not Found ユーザーが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserDetail create_user()

ユーザーを登録

ユーザーを登録します。 管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
from traq.model.post_user_request import PostUserRequest
from traq.model.user_detail import UserDetail
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
    api_instance = user_api.UserApi(api_client)
    post_user_request = PostUserRequest(
        name="zBAMDTMv2D2ylmgd10Z3UB6U",
        password="66:ILDLDNVAIP\4\",
    ) # PostUserRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ユーザーを登録
        api_response = api_instance.create_user(post_user_request=post_user_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_user_request** | [**PostUserRequest**](PostUserRequest.md)|  | [optional]

### Return type

[**UserDetail**](UserDetail.md)

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
**409** | Conflict nameが重複しています。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user**
> edit_user(user_id)

ユーザー情報を変更

指定したユーザーの情報を変更します。 管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
from traq.model.patch_user_request import PatchUserRequest
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID
    patch_user_request = PatchUserRequest(
        display_name="display_name_example",
        twitter_id="HqXzyC",
        state=UserAccountState(0),
        role="role_example",
    ) # PatchUserRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ユーザー情報を変更
        api_instance.edit_user(user_id)
    except traq.ApiException as e:
        print("Exception when calling UserApi->edit_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ユーザー情報を変更
        api_instance.edit_user(user_id, patch_user_request=patch_user_request)
    except traq.ApiException as e:
        print("Exception when calling UserApi->edit_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |
 **patch_user_request** | [**PatchUserRequest**](PatchUserRequest.md)|  | [optional]

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user_tag**
> edit_user_tag(user_id, tag_id)

ユーザーのタグを編集

指定したユーザーの指定したタグの状態を変更します。 他人の状態は変更できません。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID
    tag_id = "tagId_example" # str | タグUUID
    patch_user_tag_request = PatchUserTagRequest(
        is_locked=True,
    ) # PatchUserTagRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ユーザーのタグを編集
        api_instance.edit_user_tag(user_id, tag_id)
    except traq.ApiException as e:
        print("Exception when calling UserApi->edit_user_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ユーザーのタグを編集
        api_instance.edit_user_tag(user_id, tag_id, patch_user_tag_request=patch_user_tag_request)
    except traq.ApiException as e:
        print("Exception when calling UserApi->edit_user_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |
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
**404** | Not Found ユーザーか、タグが見つかりません。 |  -  |

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
from traq.api import user_api
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
    api_instance = user_api.UserApi(api_client)
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
        print("Exception when calling UserApi->get_direct_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ダイレクトメッセージのリストを取得
        api_response = api_instance.get_direct_messages(user_id, limit=limit, offset=offset, since=since, until=until, inclusive=inclusive, order=order)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->get_direct_messages: %s\n" % e)
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

# **get_user**
> UserDetail get_user(user_id)

ユーザー詳細情報を取得

指定したユーザーの詳細情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
from traq.model.user_detail import UserDetail
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID

    # example passing only required values which don't have defaults set
    try:
        # ユーザー詳細情報を取得
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |

### Return type

[**UserDetail**](UserDetail.md)

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

# **get_user_dm_channel**
> DMChannel get_user_dm_channel(user_id)

DMチャンネル情報を取得

指定したユーザーとのダイレクトメッセージチャンネルの情報を返します。 ダイレクトメッセージチャンネルが存在しなかった場合、自動的に作成されます。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # DMチャンネル情報を取得
        api_response = api_instance.get_user_dm_channel(user_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->get_user_dm_channel: %s\n" % e)
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

# **get_user_icon**
> file_type get_user_icon(user_id)

ユーザーのアイコン画像を取得

指定したユーザーのアイコン画像を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID

    # example passing only required values which don't have defaults set
    try:
        # ユーザーのアイコン画像を取得
        api_response = api_instance.get_user_icon(user_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->get_user_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |

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

# **get_user_stats**
> UserStats get_user_stats(user_id)

ユーザー統計情報を取得

指定したユーザーの統計情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
from traq.model.user_stats import UserStats
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID

    # example passing only required values which don't have defaults set
    try:
        # ユーザー統計情報を取得
        api_response = api_instance.get_user_stats(user_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->get_user_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |

### Return type

[**UserStats**](UserStats.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found ユーザーが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_tags**
> [UserTag] get_user_tags(user_id)

ユーザーのタグリストを取得

指定したユーザーのタグリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID

    # example passing only required values which don't have defaults set
    try:
        # ユーザーのタグリストを取得
        api_response = api_instance.get_user_tags(user_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->get_user_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |

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
**404** | Not Found ユーザーが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> [User] get_users()

ユーザーのリストを取得

ユーザーのリストを取得します。 `include-suspended`を指定しない場合、レスポンスにはユーザーアカウント状態が\"1: 有効\"であるユーザーのみが含まれます。 `include-suspended`と`name`を同時に指定することはできません。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
from traq.model.user import User
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
    api_instance = user_api.UserApi(api_client)
    include_suspended = False # bool | アカウントがアクティブでないユーザーを含め、全てのユーザーを取得するかどうか (optional) if omitted the server will use the default value of False
    name = "name_example" # str | 名前が一致するアカウントのみを取得する (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ユーザーのリストを取得
        api_response = api_instance.get_users(include_suspended=include_suspended, name=name)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_suspended** | **bool**| アカウントがアクティブでないユーザーを含め、全てのユーザーを取得するかどうか | [optional] if omitted the server will use the default value of False
 **name** | **str**| 名前が一致するアカウントのみを取得する | [optional]

### Return type

[**[User]**](User.md)

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
from traq.api import user_api
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
    api_instance = user_api.UserApi(api_client)
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
        print("Exception when calling UserApi->post_direct_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ダイレクトメッセージを送信
        api_response = api_instance.post_direct_message(user_id, post_message_request=post_message_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling UserApi->post_direct_message: %s\n" % e)
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

# **remove_user_tag**
> remove_user_tag(user_id, tag_id)

ユーザーからタグを削除します

既に存在しないタグを削除しようとした場合は204を返します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | ユーザーUUID
    tag_id = "tagId_example" # str | タグUUID

    # example passing only required values which don't have defaults set
    try:
        # ユーザーからタグを削除します
        api_instance.remove_user_tag(user_id, tag_id)
    except traq.ApiException as e:
        print("Exception when calling UserApi->remove_user_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーUUID |
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
**403** | Forbidden |  -  |
**404** | Not Found ユーザーが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

