# Version

バージョン・サーバーフラグ情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **str** | traQ(サーバー)リビジョン | 
**version** | **str** | traQ(サーバー)バージョン | 
**flags** | [**VersionFlags**](VersionFlags.md) |  | 

## Example

```python
from traq.models.version import Version

# TODO update the JSON string below
json = "{}"
# create an instance of Version from a JSON string
version_instance = Version.from_json(json)
# print the JSON string representation of the object
print Version.to_json()

# convert the object into a dict
version_dict = version_instance.to_dict()
# create an instance of Version from a dict
version_form_dict = version.from_dict(version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


