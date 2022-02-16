# BotDetail

BOT詳細情報

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | BOT UUID | 
**updated_at** | **datetime** | 更新日時 | 
**created_at** | **datetime** | 作成日時 | 
**mode** | [**BotMode**](BotMode.md) |  | 
**state** | [**BotState**](BotState.md) |  | 
**subscribe_events** | **[str]** | BOTが購読しているイベントの配列 | 
**developer_id** | **str** | BOT開発者UUID | 
**description** | **str** | 説明 | 
**bot_user_id** | **str** | BOTユーザーUUID | 
**tokens** | [**BotTokens**](BotTokens.md) |  | 
**endpoint** | **str** | BOTサーバーエンドポイント | 
**privileged** | **bool** | 特権BOTかどうか | 
**channels** | **[str]** | BOTが参加しているチャンネルのUUID配列 | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


