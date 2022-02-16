# UserGroup

ユーザーグループ

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | グループUUID | 
**name** | **str** | グループ名 | 
**description** | **str** | グループ説明 | 
**type** | **str** | グループタイプ | 
**icon** | **str** | グループアイコンUUID | 
**members** | [**[UserGroupMember]**](UserGroupMember.md) | グループメンバーの配列 | 
**created_at** | **datetime** | 作成日時 | 
**updated_at** | **datetime** | 更新日時 | 
**admins** | **[str]** | グループ管理者のUUIDの配列 | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


