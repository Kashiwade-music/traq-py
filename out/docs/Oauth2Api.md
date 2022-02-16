# traq.Oauth2Api

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](Oauth2Api.md#create_client) | **POST** /clients | OAuth2クライアントを作成
[**delete_client**](Oauth2Api.md#delete_client) | **DELETE** /clients/{clientId} | OAuth2クライアントを削除
[**edit_client**](Oauth2Api.md#edit_client) | **PATCH** /clients/{clientId} | OAuth2クライアント情報を変更
[**get_client**](Oauth2Api.md#get_client) | **GET** /clients/{clientId} | OAuth2クライアント情報を取得
[**get_clients**](Oauth2Api.md#get_clients) | **GET** /clients | OAuth2クライアントのリストを取得
[**get_my_tokens**](Oauth2Api.md#get_my_tokens) | **GET** /users/me/tokens | 有効トークンのリストを取得
[**get_o_auth2_authorize**](Oauth2Api.md#get_o_auth2_authorize) | **GET** /oauth2/authorize | OAuth2 認可エンドポイント
[**post_o_auth2_authorize**](Oauth2Api.md#post_o_auth2_authorize) | **POST** /oauth2/authorize | OAuth2 認可エンドポイント
[**post_o_auth2_authorize_decide**](Oauth2Api.md#post_o_auth2_authorize_decide) | **POST** /oauth2/authorize/decide | OAuth2 認可承諾API
[**post_o_auth2_token**](Oauth2Api.md#post_o_auth2_token) | **POST** /oauth2/token | OAuth2 トークンエンドポイント
[**revoke_my_token**](Oauth2Api.md#revoke_my_token) | **DELETE** /users/me/tokens/{tokenId} | トークンの認可を取り消す
[**revoke_o_auth2_token**](Oauth2Api.md#revoke_o_auth2_token) | **POST** /oauth2/revoke | OAuth2 トークン無効化エンドポイント


# **create_client**
> OAuth2ClientDetail create_client()

OAuth2クライアントを作成

OAuth2クライアントを作成します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import oauth2_api
from traq.model.post_client_request import PostClientRequest
from traq.model.o_auth2_client_detail import OAuth2ClientDetail
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    post_client_request = PostClientRequest(
        name="name_example",
        callback_url="callback_url_example",
        scopes=[
            OAuth2Scope("read"),
        ],
        description="description_example",
    ) # PostClientRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # OAuth2クライアントを作成
        api_response = api_instance.create_client(post_client_request=post_client_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->create_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_client_request** | [**PostClientRequest**](PostClientRequest.md)|  | [optional]

### Return type

[**OAuth2ClientDetail**](OAuth2ClientDetail.md)

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

# **delete_client**
> delete_client(client_id)

OAuth2クライアントを削除

指定したOAuth2クライアントを削除します。 対象のクライアントの管理権限が必要です。正常に削除された場合、このクライアントに対する認可は全て取り消されます。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import oauth2_api
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    client_id = "clientId_example" # str | OAuth2クライアントUUID

    # example passing only required values which don't have defaults set
    try:
        # OAuth2クライアントを削除
        api_instance.delete_client(client_id)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->delete_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| OAuth2クライアントUUID |

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
**404** | Not Found OAuth2クライアントが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_client**
> edit_client(client_id)

OAuth2クライアント情報を変更

指定したOAuth2クライアントの情報を変更します。 対象のクライアントの管理権限が必要です。 クライアント開発者UUIDを変更した場合は、変更先ユーザーにクライアント管理権限が移譲され、自分自身は権限を失います。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import oauth2_api
from traq.model.patch_client_request import PatchClientRequest
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    client_id = "clientId_example" # str | OAuth2クライアントUUID
    patch_client_request = PatchClientRequest(
        name="name_example",
        description="description_example",
        callback_url="callback_url_example",
        developer_id="developer_id_example",
    ) # PatchClientRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # OAuth2クライアント情報を変更
        api_instance.edit_client(client_id)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->edit_client: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # OAuth2クライアント情報を変更
        api_instance.edit_client(client_id, patch_client_request=patch_client_request)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->edit_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| OAuth2クライアントUUID |
 **patch_client_request** | [**PatchClientRequest**](PatchClientRequest.md)|  | [optional]

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
**404** | Not Found OAuth2クライアントが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client**
> bool, date, datetime, dict, float, int, list, str, none_type get_client(client_id)

OAuth2クライアント情報を取得

指定したOAuth2クライアントの情報を取得します。 詳細情報の取得には対象のクライアントの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import oauth2_api
from traq.model.o_auth2_client import OAuth2Client
from traq.model.o_auth2_client_detail import OAuth2ClientDetail
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    client_id = "clientId_example" # str | OAuth2クライアントUUID
    detail = False # bool | 詳細情報を含めるかどうか (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # OAuth2クライアント情報を取得
        api_response = api_instance.get_client(client_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->get_client: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # OAuth2クライアント情報を取得
        api_response = api_instance.get_client(client_id, detail=detail)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->get_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| OAuth2クライアントUUID |
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

# **get_clients**
> [OAuth2Client] get_clients()

OAuth2クライアントのリストを取得

自身が開発者のOAuth2クライアントのリストを取得します。 `all`が`true`の場合、全開発者の全クライアントのリストを返します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import oauth2_api
from traq.model.o_auth2_client import OAuth2Client
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    all = False # bool | 全てのクライアントを取得するかどうか (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # OAuth2クライアントのリストを取得
        api_response = api_instance.get_clients(all=all)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->get_clients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| 全てのクライアントを取得するかどうか | [optional] if omitted the server will use the default value of False

### Return type

[**[OAuth2Client]**](OAuth2Client.md)

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
from traq.api import oauth2_api
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
    api_instance = oauth2_api.Oauth2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 有効トークンのリストを取得
        api_response = api_instance.get_my_tokens()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->get_my_tokens: %s\n" % e)
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

# **get_o_auth2_authorize**
> get_o_auth2_authorize(client_id)

OAuth2 認可エンドポイント

OAuth2 認可エンドポイント

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import oauth2_api
from traq.model.o_auth2_prompt import OAuth2Prompt
from traq.model.o_auth2_response_type import OAuth2ResponseType
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    client_id = "client_id_example" # str | 
    response_type = OAuth2ResponseType("code") # OAuth2ResponseType |  (optional)
    redirect_uri = "redirect_uri_example" # str |  (optional)
    scope = "scope_example" # str |  (optional)
    state = "state_example" # str |  (optional)
    code_challenge = "code_challenge_example" # str |  (optional)
    code_challenge_method = "code_challenge_method_example" # str |  (optional)
    nonce = "nonce_example" # str |  (optional)
    prompt = OAuth2Prompt("none") # OAuth2Prompt |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # OAuth2 認可エンドポイント
        api_instance.get_o_auth2_authorize(client_id)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->get_o_auth2_authorize: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # OAuth2 認可エンドポイント
        api_instance.get_o_auth2_authorize(client_id, response_type=response_type, redirect_uri=redirect_uri, scope=scope, state=state, code_challenge=code_challenge, code_challenge_method=code_challenge_method, nonce=nonce, prompt=prompt)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->get_o_auth2_authorize: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  |
 **response_type** | **OAuth2ResponseType**|  | [optional]
 **redirect_uri** | **str**|  | [optional]
 **scope** | **str**|  | [optional]
 **state** | **str**|  | [optional]
 **code_challenge** | **str**|  | [optional]
 **code_challenge_method** | **str**|  | [optional]
 **nonce** | **str**|  | [optional]
 **prompt** | **OAuth2Prompt**|  | [optional]

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
**302** | 結果に応じてリダイレクトします。 |  -  |
**400** | リクエストが不正です。 |  -  |
**403** | リクエストが許可されていません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_o_auth2_authorize**
> post_o_auth2_authorize(client_id)

OAuth2 認可エンドポイント

OAuth2 認可エンドポイント

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import oauth2_api
from traq.model.o_auth2_prompt import OAuth2Prompt
from traq.model.o_auth2_response_type import OAuth2ResponseType
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    client_id = "client_id_example" # str | 
    response_type = OAuth2ResponseType("code") # OAuth2ResponseType |  (optional)
    redirect_uri = "redirect_uri_example" # str |  (optional)
    scope = "scope_example" # str |  (optional)
    state = "state_example" # str |  (optional)
    code_challenge = "code_challenge_example" # str |  (optional)
    code_challenge_method = "code_challenge_method_example" # str |  (optional)
    nonce = "nonce_example" # str |  (optional)
    prompt = OAuth2Prompt("none") # OAuth2Prompt |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # OAuth2 認可エンドポイント
        api_instance.post_o_auth2_authorize(client_id)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->post_o_auth2_authorize: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # OAuth2 認可エンドポイント
        api_instance.post_o_auth2_authorize(client_id, response_type=response_type, redirect_uri=redirect_uri, scope=scope, state=state, code_challenge=code_challenge, code_challenge_method=code_challenge_method, nonce=nonce, prompt=prompt)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->post_o_auth2_authorize: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  |
 **response_type** | [**OAuth2ResponseType**](OAuth2ResponseType.md)|  | [optional]
 **redirect_uri** | **str**|  | [optional]
 **scope** | **str**|  | [optional]
 **state** | **str**|  | [optional]
 **code_challenge** | **str**|  | [optional]
 **code_challenge_method** | **str**|  | [optional]
 **nonce** | **str**|  | [optional]
 **prompt** | [**OAuth2Prompt**](OAuth2Prompt.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | 結果に応じてリダイレクトします。 |  -  |
**400** | リクエストが不正です。 |  -  |
**403** | リクエストが許可されていません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_o_auth2_authorize_decide**
> post_o_auth2_authorize_decide(submit)

OAuth2 認可承諾API

OAuth2 認可承諾

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import oauth2_api
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    submit = "submit_example" # str | 承諾する場合は\\\"approve\\\"

    # example passing only required values which don't have defaults set
    try:
        # OAuth2 認可承諾API
        api_instance.post_o_auth2_authorize_decide(submit)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->post_o_auth2_authorize_decide: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit** | **str**| 承諾する場合は\\\&quot;approve\\\&quot; |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | RedirectURIに結果をリダイレクトします。 |  -  |
**400** | リクエストが不正です。 |  -  |
**403** | リクエストが許可されていません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_o_auth2_token**
> OAuth2Token post_o_auth2_token(grant_type)

OAuth2 トークンエンドポイント

OAuth2 トークンエンドポイント

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import oauth2_api
from traq.model.o_auth2_token import OAuth2Token
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    grant_type = "grant_type_example" # str | 
    code = "code_example" # str |  (optional)
    redirect_uri = "redirect_uri_example" # str |  (optional)
    client_id = "client_id_example" # str |  (optional)
    code_verifier = "code_verifier_example" # str |  (optional)
    username = "username_example" # str |  (optional)
    password = "password_example" # str |  (optional)
    scope = "scope_example" # str |  (optional)
    refresh_token = "refresh_token_example" # str |  (optional)
    client_secret = "client_secret_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # OAuth2 トークンエンドポイント
        api_response = api_instance.post_o_auth2_token(grant_type)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->post_o_auth2_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # OAuth2 トークンエンドポイント
        api_response = api_instance.post_o_auth2_token(grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, code_verifier=code_verifier, username=username, password=password, scope=scope, refresh_token=refresh_token, client_secret=client_secret)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->post_o_auth2_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  |
 **code** | **str**|  | [optional]
 **redirect_uri** | **str**|  | [optional]
 **client_id** | **str**|  | [optional]
 **code_verifier** | **str**|  | [optional]
 **username** | **str**|  | [optional]
 **password** | **str**|  | [optional]
 **scope** | **str**|  | [optional]
 **refresh_token** | **str**|  | [optional]
 **client_secret** | **str**|  | [optional]

### Return type

[**OAuth2Token**](OAuth2Token.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | トークンが正常に発行されました。 |  -  |
**400** | トークン発行に失敗しました。 |  -  |
**403** | トークン発行に失敗しました。 |  -  |

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
from traq.api import oauth2_api
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    token_id = "tokenId_example" # str | OAuth2トークンUUID

    # example passing only required values which don't have defaults set
    try:
        # トークンの認可を取り消す
        api_instance.revoke_my_token(token_id)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->revoke_my_token: %s\n" % e)
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

# **revoke_o_auth2_token**
> revoke_o_auth2_token(token)

OAuth2 トークン無効化エンドポイント

OAuth2 トークン無効化エンドポイント

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import oauth2_api
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
    api_instance = oauth2_api.Oauth2Api(api_client)
    token = "token_example" # str | 無効化するOAuth2トークンまたはOAuth2リフレッシュトークン

    # example passing only required values which don't have defaults set
    try:
        # OAuth2 トークン無効化エンドポイント
        api_instance.revoke_o_auth2_token(token)
    except traq.ApiException as e:
        print("Exception when calling Oauth2Api->revoke_o_auth2_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| 無効化するOAuth2トークンまたはOAuth2リフレッシュトークン |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

