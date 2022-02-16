"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import traq
from traq.api.channel_api import ChannelApi  # noqa: E501


class TestChannelApi(unittest.TestCase):
    """ChannelApi unit test stubs"""

    def setUp(self):
        self.api = ChannelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_channel(self):
        """Test case for create_channel

        チャンネルを作成  # noqa: E501
        """
        pass

    def test_edit_channel(self):
        """Test case for edit_channel

        チャンネル情報を変更  # noqa: E501
        """
        pass

    def test_edit_channel_subscribers(self):
        """Test case for edit_channel_subscribers

        チャンネルの通知購読者を編集  # noqa: E501
        """
        pass

    def test_edit_channel_topic(self):
        """Test case for edit_channel_topic

        チャンネルトピックを編集  # noqa: E501
        """
        pass

    def test_get_channel(self):
        """Test case for get_channel

        チャンネル情報を取得  # noqa: E501
        """
        pass

    def test_get_channel_bots(self):
        """Test case for get_channel_bots

        チャンネル参加中のBOTのリストを取得  # noqa: E501
        """
        pass

    def test_get_channel_events(self):
        """Test case for get_channel_events

        チャンネルイベントのリストを取得  # noqa: E501
        """
        pass

    def test_get_channel_pins(self):
        """Test case for get_channel_pins

        チャンネルピンのリストを取得  # noqa: E501
        """
        pass

    def test_get_channel_stats(self):
        """Test case for get_channel_stats

        チャンネル統計情報を取得  # noqa: E501
        """
        pass

    def test_get_channel_subscribers(self):
        """Test case for get_channel_subscribers

        チャンネルの通知購読者のリストを取得  # noqa: E501
        """
        pass

    def test_get_channel_topic(self):
        """Test case for get_channel_topic

        チャンネルトピックを取得  # noqa: E501
        """
        pass

    def test_get_channel_viewers(self):
        """Test case for get_channel_viewers

        チャンネル閲覧者リストを取得  # noqa: E501
        """
        pass

    def test_get_channels(self):
        """Test case for get_channels

        チャンネルリストを取得  # noqa: E501
        """
        pass

    def test_get_messages(self):
        """Test case for get_messages

        チャンネルメッセージのリストを取得  # noqa: E501
        """
        pass

    def test_get_user_dm_channel(self):
        """Test case for get_user_dm_channel

        DMチャンネル情報を取得  # noqa: E501
        """
        pass

    def test_post_message(self):
        """Test case for post_message

        チャンネルにメッセージを投稿  # noqa: E501
        """
        pass

    def test_set_channel_subscribers(self):
        """Test case for set_channel_subscribers

        チャンネルの通知購読者を設定  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()