# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from traq.api.webhook_api import WebhookApi


class TestWebhookApi(unittest.TestCase):
    """WebhookApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WebhookApi()

    def tearDown(self) -> None:
        pass

    def test_change_webhook_icon(self) -> None:
        """Test case for change_webhook_icon

        Webhookのアイコンを変更
        """
        pass

    def test_create_webhook(self) -> None:
        """Test case for create_webhook

        Webhookを新規作成
        """
        pass

    def test_delete_webhook(self) -> None:
        """Test case for delete_webhook

        Webhookを削除
        """
        pass

    def test_edit_webhook(self) -> None:
        """Test case for edit_webhook

        Webhook情報を変更
        """
        pass

    def test_get_webhook(self) -> None:
        """Test case for get_webhook

        Webhook情報を取得
        """
        pass

    def test_get_webhook_icon(self) -> None:
        """Test case for get_webhook_icon

        Webhookのアイコンを取得
        """
        pass

    def test_get_webhook_messages(self) -> None:
        """Test case for get_webhook_messages

        Webhookの投稿メッセージのリストを取得
        """
        pass

    def test_get_webhooks(self) -> None:
        """Test case for get_webhooks

        Webhook情報のリストを取得します
        """
        pass

    def test_post_webhook(self) -> None:
        """Test case for post_webhook

        Webhookを送信
        """
        pass


if __name__ == '__main__':
    unittest.main()
