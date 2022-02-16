# FileInfo

ファイル情報

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ファイルUUID | 
**name** | **str** | ファイル名 | 
**mime** | **str** | MIMEタイプ | 
**size** | **int** | ファイルサイズ | 
**md5** | **str** | MD5ハッシュ | 
**is_animated_image** | **bool** | アニメーション画像かどうか | 
**created_at** | **datetime** | アップロード日時 | 
**thumbnails** | [**[ThumbnailInfo]**](ThumbnailInfo.md) |  | 
**thumbnail** | [**FileInfoThumbnail**](FileInfoThumbnail.md) |  | 
**channel_id** | **str, none_type** | 属しているチャンネルUUID | 
**uploader_id** | **str, none_type** | アップロード者UUID | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


