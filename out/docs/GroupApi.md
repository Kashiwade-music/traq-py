# traq.GroupApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_group_admin**](GroupApi.md#add_user_group_admin) | **POST** /groups/{groupId}/admins | グループ管理者を追加
[**add_user_group_member**](GroupApi.md#add_user_group_member) | **POST** /groups/{groupId}/members | グループメンバーを追加
[**change_user_group_icon**](GroupApi.md#change_user_group_icon) | **PUT** /groups/{groupId}/icon | ユーザーグループのアイコンを変更
[**create_user_group**](GroupApi.md#create_user_group) | **POST** /groups | ユーザーグループを作成
[**delete_user_group**](GroupApi.md#delete_user_group) | **DELETE** /groups/{groupId} | ユーザーグループを削除
[**edit_user_group**](GroupApi.md#edit_user_group) | **PATCH** /groups/{groupId} | ユーザーグループを編集
[**edit_user_group_member**](GroupApi.md#edit_user_group_member) | **PATCH** /groups/{groupId}/members/{userId} | グループメンバーを編集
[**get_user_group**](GroupApi.md#get_user_group) | **GET** /groups/{groupId} | ユーザーグループを取得
[**get_user_group_admins**](GroupApi.md#get_user_group_admins) | **GET** /groups/{groupId}/admins | グループ管理者を取得
[**get_user_group_members**](GroupApi.md#get_user_group_members) | **GET** /groups/{groupId}/members | グループメンバーを取得
[**get_user_groups**](GroupApi.md#get_user_groups) | **GET** /groups | ユーザーグループのリストを取得
[**remove_user_group_admin**](GroupApi.md#remove_user_group_admin) | **DELETE** /groups/{groupId}/admins/{userId} | グループ管理者を削除
[**remove_user_group_member**](GroupApi.md#remove_user_group_member) | **DELETE** /groups/{groupId}/members/{userId} | グループメンバーを削除


# **add_user_group_admin**
> add_user_group_admin(group_id)

グループ管理者を追加

指定したグループに管理者を追加します。 対象のユーザーグループの管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
from traq.model.post_user_group_admin_request import PostUserGroupAdminRequest
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID
    post_user_group_admin_request = PostUserGroupAdminRequest(
        id="id_example",
    ) # PostUserGroupAdminRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # グループ管理者を追加
        api_instance.add_user_group_admin(group_id)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->add_user_group_admin: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # グループ管理者を追加
        api_instance.add_user_group_admin(group_id, post_user_group_admin_request=post_user_group_admin_request)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->add_user_group_admin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |
 **post_user_group_admin_request** | [**PostUserGroupAdminRequest**](PostUserGroupAdminRequest.md)|  | [optional]

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
**204** | No Content 追加されました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden ユーザーグループを操作する権限がありません。 |  -  |
**404** | Not Found ユーザーグループが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_group_member**
> add_user_group_member(group_id)

グループメンバーを追加

指定したグループにメンバーを追加します。 対象のユーザーグループの管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
from traq.model.user_group_member import UserGroupMember
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID
    user_group_member = UserGroupMember(
        id="id_example",
        role="role_example",
    ) # UserGroupMember |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # グループメンバーを追加
        api_instance.add_user_group_member(group_id)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->add_user_group_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # グループメンバーを追加
        api_instance.add_user_group_member(group_id, user_group_member=user_group_member)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->add_user_group_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |
 **user_group_member** | [**UserGroupMember**](UserGroupMember.md)|  | [optional]

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
**204** | No Content 追加されました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden ユーザーグループを操作する権限がありません。 |  -  |
**404** | Not Found ユーザーグループが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_group_icon**
> change_user_group_icon(group_id, file)

ユーザーグループのアイコンを変更

ユーザーグループのアイコンを変更します。 対象のユーザーグループの管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID
    file = open('/path/to/file', 'rb') # file_type | アイコン画像(1MBまでのpng, jpeg, gif)

    # example passing only required values which don't have defaults set
    try:
        # ユーザーグループのアイコンを変更
        api_instance.change_user_group_icon(group_id, file)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->change_user_group_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |
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
**404** | Not Found ユーザーグループが見つかりません。 |  -  |
**413** | Request Entity Too Large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_group**
> UserGroup create_user_group()

ユーザーグループを作成

ユーザーグループを作成します。 作成者は自動的にグループ管理者になります。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
from traq.model.user_group import UserGroup
from traq.model.post_user_group_request import PostUserGroupRequest
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
    api_instance = group_api.GroupApi(api_client)
    post_user_group_request = PostUserGroupRequest(
        name="name_example",
        description="description_example",
        type="type_example",
    ) # PostUserGroupRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ユーザーグループを作成
        api_response = api_instance.create_user_group(post_user_group_request=post_user_group_request)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->create_user_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_user_group_request** | [**PostUserGroupRequest**](PostUserGroupRequest.md)|  | [optional]

### Return type

[**UserGroup**](UserGroup.md)

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
**403** | Forbidden 指定したグループを作成する権限がありません。 |  -  |
**409** | Conflict 指定した名前のグループは既に存在します。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_group**
> delete_user_group(group_id)

ユーザーグループを削除

指定したユーザーグループを削除します。 対象のユーザーグループの管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID

    # example passing only required values which don't have defaults set
    try:
        # ユーザーグループを削除
        api_instance.delete_user_group(group_id)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->delete_user_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |

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
**204** | No Content ユーザーグループが削除されました。 |  -  |
**403** | Forbidden ユーザーグループを操作する権限がありません。 |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user_group**
> edit_user_group(group_id)

ユーザーグループを編集

指定したユーザーグループの情報を編集します。 対象のユーザーグループの管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
from traq.model.patch_user_group_request import PatchUserGroupRequest
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID
    patch_user_group_request = PatchUserGroupRequest(
        name="name_example",
        description="description_example",
        type="type_example",
    ) # PatchUserGroupRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ユーザーグループを編集
        api_instance.edit_user_group(group_id)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->edit_user_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ユーザーグループを編集
        api_instance.edit_user_group(group_id, patch_user_group_request=patch_user_group_request)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->edit_user_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |
 **patch_user_group_request** | [**PatchUserGroupRequest**](PatchUserGroupRequest.md)|  | [optional]

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
**204** | No Content 編集されました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden ユーザーグループを操作する権限がありません。 |  -  |
**404** | Not Found |  -  |
**409** | Conflict 変更後のグループ名のグループは既に存在します。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user_group_member**
> edit_user_group_member(group_id, user_id)

グループメンバーを編集

指定したユーザーグループ内の指定したユーザーの属性を編集します。 対象のユーザーグループの管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
from traq.model.patch_group_member_request import PatchGroupMemberRequest
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID
    user_id = "userId_example" # str | ユーザーUUID
    patch_group_member_request = PatchGroupMemberRequest(
        role="role_example",
    ) # PatchGroupMemberRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # グループメンバーを編集
        api_instance.edit_user_group_member(group_id, user_id)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->edit_user_group_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # グループメンバーを編集
        api_instance.edit_user_group_member(group_id, user_id, patch_group_member_request=patch_group_member_request)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->edit_user_group_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |
 **user_id** | **str**| ユーザーUUID |
 **patch_group_member_request** | [**PatchGroupMemberRequest**](PatchGroupMemberRequest.md)|  | [optional]

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
**400** | Bad Request ユーザーがグループに存在しないか、リクエストが不正です。 |  -  |
**403** | Forbidden ユーザーグループを操作する権限がありません。 |  -  |
**404** | Not Found ユーザーグループが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group**
> UserGroup get_user_group(group_id)

ユーザーグループを取得

指定したユーザーグループの情報を取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
from traq.model.user_group import UserGroup
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID

    # example passing only required values which don't have defaults set
    try:
        # ユーザーグループを取得
        api_response = api_instance.get_user_group(group_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->get_user_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |

### Return type

[**UserGroup**](UserGroup.md)

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

# **get_user_group_admins**
> [str] get_user_group_admins(group_id)

グループ管理者を取得

指定したグループの管理者のリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID

    # example passing only required values which don't have defaults set
    try:
        # グループ管理者を取得
        api_response = api_instance.get_user_group_admins(group_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->get_user_group_admins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |

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
**404** | Not Found ユーザーグループが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group_members**
> [UserGroupMember] get_user_group_members(group_id)

グループメンバーを取得

指定したグループのメンバーのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
from traq.model.user_group_member import UserGroupMember
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID

    # example passing only required values which don't have defaults set
    try:
        # グループメンバーを取得
        api_response = api_instance.get_user_group_members(group_id)
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->get_user_group_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |

### Return type

[**[UserGroupMember]**](UserGroupMember.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found ユーザーグループが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_groups**
> [UserGroup] get_user_groups()

ユーザーグループのリストを取得

ユーザーグループのリストを取得します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
from traq.model.user_group import UserGroup
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
    api_instance = group_api.GroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ユーザーグループのリストを取得
        api_response = api_instance.get_user_groups()
        pprint(api_response)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->get_user_groups: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[UserGroup]**](UserGroup.md)

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

# **remove_user_group_admin**
> remove_user_group_admin(group_id, user_id)

グループ管理者を削除

指定したユーザーグループから指定した管理者を削除します。 対象のユーザーグループの管理者権限が必要です。 グループから管理者が存在しなくなる場合は400エラーを返します。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID
    user_id = "userId_example" # str | ユーザーUUID

    # example passing only required values which don't have defaults set
    try:
        # グループ管理者を削除
        api_instance.remove_user_group_admin(group_id, user_id)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->remove_user_group_admin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |
 **user_id** | **str**| ユーザーUUID |

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
**204** | No Content 指定したユーザーがユーザーグループ管理者から削除されました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden ユーザーグループを操作する権限がありません。 |  -  |
**404** | Not Found ユーザーグループが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_group_member**
> remove_user_group_member(group_id, user_id)

グループメンバーを削除

指定したユーザーグループから指定したユーザーを削除します。 既にグループから削除されているメンバーを指定した場合は204を返します。 対象のユーザーグループの管理者権限が必要です。

### Example

* OAuth Authentication (OAuth2):

```python
import time
import traq
from traq.api import group_api
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "groupId_example" # str | ユーザーグループUUID
    user_id = "userId_example" # str | ユーザーUUID

    # example passing only required values which don't have defaults set
    try:
        # グループメンバーを削除
        api_instance.remove_user_group_member(group_id, user_id)
    except traq.ApiException as e:
        print("Exception when calling GroupApi->remove_user_group_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ユーザーグループUUID |
 **user_id** | **str**| ユーザーUUID |

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
**204** | No Content 指定したユーザーがユーザーグループから削除されました。 |  -  |
**403** | Forbidden ユーザーグループを操作する権限がありません。 |  -  |
**404** | Not Found ユーザーグループが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

