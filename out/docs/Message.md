# Message

メッセージ

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | メッセージUUID | 
**user_id** | **str** | 投稿者UUID | 
**channel_id** | **str** | チャンネルUUID | 
**content** | **str** | メッセージ本文 | 
**created_at** | **datetime** | 投稿日時 | 
**updated_at** | **datetime** | 編集日時 | 
**pinned** | **bool** | ピン留めされているかどうか | 
**stamps** | [**[MessageStamp]**](MessageStamp.md) | 押されているスタンプの配列 | 
**thread_id** | **str, none_type** | スレッドUUID | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


