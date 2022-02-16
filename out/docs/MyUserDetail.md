# MyUserDetail

自分のユーザー詳細情報

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ユーザーUUID | 
**bio** | **str** | 自己紹介(biography) | 
**groups** | **[str]** | 所属グループのUUIDの配列 | 
**tags** | [**[UserTag]**](UserTag.md) | タグリスト | 
**updated_at** | **datetime** | 更新日時 | 
**last_online** | **datetime, none_type** | 最終オンライン日時 | 
**twitter_id** | **str** | Twitter ID | 
**name** | **str** | ユーザー名 | 
**display_name** | **str** | ユーザー表示名 | 
**icon_file_id** | **str** | アイコンファイルUUID | 
**bot** | **bool** | BOTかどうか | 
**state** | [**UserAccountState**](UserAccountState.md) |  | 
**permissions** | [**[UserPermission]**](UserPermission.md) | 所有している権限の配列 | 
**home_channel** | **str, none_type** | ホームチャンネル | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


