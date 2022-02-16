# traq.AuthenticationApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_external_accounts**](AuthenticationApi.md#get_my_external_accounts) | **GET** /users/me/ex-accounts | 外部ログインアカウント一覧を取得
[**get_my_sessions**](AuthenticationApi.md#get_my_sessions) | **GET** /users/me/sessions | 自分のログインセッションリストを取得
[**link_external_account**](AuthenticationApi.md#link_external_account) | **POST** /users/me/ex-accounts/link | 外部ログインアカウントを紐付ける
[**login**](AuthenticationApi.md#login) | **POST** /login | ログイン
[**logout**](AuthenticationApi.md#logout) | **POST** /logout | ログアウト
[**revoke_my_session**](AuthenticationApi.md#revoke_my_session) | **DELETE** /users/me/sessions/{sessionId} | セッションを無効化
[**unlink_external_account**](AuthenticationApi.md#unlink_external_account) | **POST** /users/me/ex-accounts/unlink | 外部ログインアカウントの紐付けを解除


# **get_my_external_accounts**
> [ExternalProviderUser] get_my_external_accounts()

外部ログインアカウント一覧を取得

自分に紐付けられている外部ログインアカウント一覧を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import authentication_api
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
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 外部ログインアカウント一覧を取得
        api_response = api_instance.get_my_external_accounts()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling AuthenticationApi->get_my_external_accounts: %s\n" % e)
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

# **get_my_sessions**
> [LoginSession] get_my_sessions()

自分のログインセッションリストを取得

自分のログインセッションのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import authentication_api
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
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 自分のログインセッションリストを取得
        api_response = api_instance.get_my_sessions()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling AuthenticationApi->get_my_sessions: %s\n" % e)
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

# **link_external_account**
> link_external_account()

外部ログインアカウントを紐付ける

自分に外部ログインアカウントを紐付けます。 指定した`providerName`がサーバー側で有効である必要があります。 リクエストが受理された場合、外部サービスの認証画面にリダイレクトされ、認証される必要があります。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import authentication_api
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
    api_instance = authentication_api.AuthenticationApi(api_client)
    post_link_external_account = PostLinkExternalAccount(
        provider_name="provider_name_example",
    ) # PostLinkExternalAccount |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 外部ログインアカウントを紐付ける
        api_instance.link_external_account(post_link_external_account=post_link_external_account)
    except traq.ApiException as e:
        print("Exception when calling AuthenticationApi->link_external_account: %s\n" % e)
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

# **login**
> login()

ログイン

ログインします。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import authentication_api
from traq.model.post_login_request import PostLoginRequest
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
    api_instance = authentication_api.AuthenticationApi(api_client)
    redirect = "redirect_example" # str | リダイレクト先 (optional)
    post_login_request = PostLoginRequest(
        name="zBAMDTMv2D2ylmgd10Z3UB6U",
        password="66:ILDLDNVAIP\4\",
    ) # PostLoginRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ログイン
        api_instance.login(redirect=redirect, post_login_request=post_login_request)
    except traq.ApiException as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect** | **str**| リダイレクト先 | [optional]
 **post_login_request** | [**PostLoginRequest**](PostLoginRequest.md)|  | [optional]

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
**204** | No Content ログインしました。 |  -  |
**302** | Found ログインしました。リダイレクトします。 |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized 認証情報が間違っています。 |  -  |
**403** | Forbidden ログインを試行したユーザーアカウントに問題があります。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

ログアウト

ログアウトします。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import authentication_api
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
    api_instance = authentication_api.AuthenticationApi(api_client)
    redirect = "redirect_example" # str | リダイレクト先 (optional)
    all = False # bool | 全てのセッションでログアウトするかどうか (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ログアウト
        api_instance.logout(redirect=redirect, all=all)
    except traq.ApiException as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect** | **str**| リダイレクト先 | [optional]
 **all** | **bool**| 全てのセッションでログアウトするかどうか | [optional] if omitted the server will use the default value of False

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
**204** | No Content ログアウトしました。 |  -  |
**302** | Found ログアウトしました。リダイレクトします。 |  -  |

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
from traq.api import authentication_api
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
    api_instance = authentication_api.AuthenticationApi(api_client)
    session_id = "sessionId_example" # str | セッションUUID

    # example passing only required values which don't have defaults set
    try:
        # セッションを無効化
        api_instance.revoke_my_session(session_id)
    except traq.ApiException as e:
        print("Exception when calling AuthenticationApi->revoke_my_session: %s\n" % e)
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

# **unlink_external_account**
> unlink_external_account()

外部ログインアカウントの紐付けを解除

自分に紐付けられている外部ログインアカウントの紐付けを解除します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import authentication_api
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
    api_instance = authentication_api.AuthenticationApi(api_client)
    post_unlink_external_account = PostUnlinkExternalAccount(
        provider_name="provider_name_example",
    ) # PostUnlinkExternalAccount |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 外部ログインアカウントの紐付けを解除
        api_instance.unlink_external_account(post_unlink_external_account=post_unlink_external_account)
    except traq.ApiException as e:
        print("Exception when calling AuthenticationApi->unlink_external_account: %s\n" % e)
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

