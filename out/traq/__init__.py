# coding: utf-8

# flake8: noqa

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "3.15.2"

# import apis into sdk package
from traq.api.activity_api import ActivityApi
from traq.api.authentication_api import AuthenticationApi
from traq.api.bot_api import BotApi
from traq.api.channel_api import ChannelApi
from traq.api.clip_api import ClipApi
from traq.api.file_api import FileApi
from traq.api.group_api import GroupApi
from traq.api.me_api import MeApi
from traq.api.message_api import MessageApi
from traq.api.notification_api import NotificationApi
from traq.api.oauth2_api import Oauth2Api
from traq.api.ogp_api import OgpApi
from traq.api.pin_api import PinApi
from traq.api.public_api import PublicApi
from traq.api.stamp_api import StampApi
from traq.api.star_api import StarApi
from traq.api.user_api import UserApi
from traq.api.user_tag_api import UserTagApi
from traq.api.webhook_api import WebhookApi
from traq.api.webrtc_api import WebrtcApi

# import ApiClient
from traq.api_response import ApiResponse
from traq.api_client import ApiClient
from traq.configuration import Configuration
from traq.exceptions import OpenApiException
from traq.exceptions import ApiTypeError
from traq.exceptions import ApiValueError
from traq.exceptions import ApiKeyError
from traq.exceptions import ApiAttributeError
from traq.exceptions import ApiException

# import models into sdk package
from traq.models.active_o_auth2_token import ActiveOAuth2Token
from traq.models.activity_timeline_message import ActivityTimelineMessage
from traq.models.bot import Bot
from traq.models.bot_detail import BotDetail
from traq.models.bot_event_log import BotEventLog
from traq.models.bot_event_result import BotEventResult
from traq.models.bot_mode import BotMode
from traq.models.bot_state import BotState
from traq.models.bot_tokens import BotTokens
from traq.models.bot_user import BotUser
from traq.models.channel import Channel
from traq.models.channel_event import ChannelEvent
from traq.models.channel_event_detail import ChannelEventDetail
from traq.models.channel_list import ChannelList
from traq.models.channel_stats import ChannelStats
from traq.models.channel_stats_stamp import ChannelStatsStamp
from traq.models.channel_stats_user import ChannelStatsUser
from traq.models.channel_subscribe_level import ChannelSubscribeLevel
from traq.models.channel_topic import ChannelTopic
from traq.models.channel_view_state import ChannelViewState
from traq.models.channel_viewer import ChannelViewer
from traq.models.child_created_event import ChildCreatedEvent
from traq.models.clip_folder import ClipFolder
from traq.models.clipped_message import ClippedMessage
from traq.models.dm_channel import DMChannel
from traq.models.external_provider_user import ExternalProviderUser
from traq.models.file_info import FileInfo
from traq.models.file_info_thumbnail import FileInfoThumbnail
from traq.models.forced_notification_changed_event import ForcedNotificationChangedEvent
from traq.models.get_bot200_response import GetBot200Response
from traq.models.get_client200_response import GetClient200Response
from traq.models.get_notify_citation import GetNotifyCitation
from traq.models.login_session import LoginSession
from traq.models.message import Message
from traq.models.message_clip import MessageClip
from traq.models.message_pin import MessagePin
from traq.models.message_search_result import MessageSearchResult
from traq.models.message_stamp import MessageStamp
from traq.models.my_channel_view_state import MyChannelViewState
from traq.models.my_user_detail import MyUserDetail
from traq.models.name_changed_event import NameChangedEvent
from traq.models.o_auth2_client import OAuth2Client
from traq.models.o_auth2_client_detail import OAuth2ClientDetail
from traq.models.o_auth2_prompt import OAuth2Prompt
from traq.models.o_auth2_response_type import OAuth2ResponseType
from traq.models.o_auth2_scope import OAuth2Scope
from traq.models.o_auth2_token import OAuth2Token
from traq.models.ogp import Ogp
from traq.models.ogp_media import OgpMedia
from traq.models.parent_changed_event import ParentChangedEvent
from traq.models.patch_bot_request import PatchBotRequest
from traq.models.patch_channel_request import PatchChannelRequest
from traq.models.patch_channel_subscribers_request import PatchChannelSubscribersRequest
from traq.models.patch_client_request import PatchClientRequest
from traq.models.patch_clip_folder_request import PatchClipFolderRequest
from traq.models.patch_group_member_request import PatchGroupMemberRequest
from traq.models.patch_me_request import PatchMeRequest
from traq.models.patch_stamp_palette_request import PatchStampPaletteRequest
from traq.models.patch_stamp_request import PatchStampRequest
from traq.models.patch_user_group_request import PatchUserGroupRequest
from traq.models.patch_user_request import PatchUserRequest
from traq.models.patch_user_tag_request import PatchUserTagRequest
from traq.models.patch_webhook_request import PatchWebhookRequest
from traq.models.pin import Pin
from traq.models.pin_added_event import PinAddedEvent
from traq.models.pin_removed_event import PinRemovedEvent
from traq.models.post_bot_action_join_request import PostBotActionJoinRequest
from traq.models.post_bot_action_leave_request import PostBotActionLeaveRequest
from traq.models.post_bot_request import PostBotRequest
from traq.models.post_channel_request import PostChannelRequest
from traq.models.post_client_request import PostClientRequest
from traq.models.post_clip_folder_message_request import PostClipFolderMessageRequest
from traq.models.post_clip_folder_request import PostClipFolderRequest
from traq.models.post_link_external_account import PostLinkExternalAccount
from traq.models.post_login_request import PostLoginRequest
from traq.models.post_message_request import PostMessageRequest
from traq.models.post_message_stamp_request import PostMessageStampRequest
from traq.models.post_my_fcm_device_request import PostMyFCMDeviceRequest
from traq.models.post_stamp_palette_request import PostStampPaletteRequest
from traq.models.post_star_request import PostStarRequest
from traq.models.post_unlink_external_account import PostUnlinkExternalAccount
from traq.models.post_user_group_admin_request import PostUserGroupAdminRequest
from traq.models.post_user_group_request import PostUserGroupRequest
from traq.models.post_user_request import PostUserRequest
from traq.models.post_user_tag_request import PostUserTagRequest
from traq.models.post_web_rtc_authenticate_request import PostWebRTCAuthenticateRequest
from traq.models.post_webhook_request import PostWebhookRequest
from traq.models.put_channel_subscribe_level_request import PutChannelSubscribeLevelRequest
from traq.models.put_channel_subscribers_request import PutChannelSubscribersRequest
from traq.models.put_channel_topic_request import PutChannelTopicRequest
from traq.models.put_my_password_request import PutMyPasswordRequest
from traq.models.put_notify_citation_request import PutNotifyCitationRequest
from traq.models.put_user_password_request import PutUserPasswordRequest
from traq.models.stamp import Stamp
from traq.models.stamp_history_entry import StampHistoryEntry
from traq.models.stamp_palette import StampPalette
from traq.models.stamp_stats import StampStats
from traq.models.subscribers_changed_event import SubscribersChangedEvent
from traq.models.tag import Tag
from traq.models.thumbnail_info import ThumbnailInfo
from traq.models.thumbnail_type import ThumbnailType
from traq.models.topic_changed_event import TopicChangedEvent
from traq.models.unread_channel import UnreadChannel
from traq.models.user import User
from traq.models.user_account_state import UserAccountState
from traq.models.user_detail import UserDetail
from traq.models.user_group import UserGroup
from traq.models.user_group_member import UserGroupMember
from traq.models.user_permission import UserPermission
from traq.models.user_settings import UserSettings
from traq.models.user_stats import UserStats
from traq.models.user_stats_stamp import UserStatsStamp
from traq.models.user_subscribe_state import UserSubscribeState
from traq.models.user_tag import UserTag
from traq.models.version import Version
from traq.models.version_flags import VersionFlags
from traq.models.visibility_changed_event import VisibilityChangedEvent
from traq.models.web_rtc_authenticate_result import WebRTCAuthenticateResult
from traq.models.web_rtc_user_state import WebRTCUserState
from traq.models.web_rtc_user_state_sessions_inner import WebRTCUserStateSessionsInner
from traq.models.webhook import Webhook
