# UserDetail

ユーザー詳細情報

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ユーザーUUID | 
**state** | [**UserAccountState**](UserAccountState.md) |  | 
**bot** | **bool** | BOTかどうか | 
**icon_file_id** | **str** | アイコンファイルUUID | 
**display_name** | **str** | ユーザー表示名 | 
**name** | **str** | ユーザー名 | 
**twitter_id** | **str** | Twitter ID | 
**last_online** | **datetime, none_type** | 最終オンライン日時 | 
**updated_at** | **datetime** | 更新日時 | 
**tags** | [**[UserTag]**](UserTag.md) | タグリスト | 
**groups** | **[str]** | 所属グループのUUIDの配列 | 
**bio** | **str** | 自己紹介(biography) | 
**home_channel** | **str, none_type** | ホームチャンネル | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


