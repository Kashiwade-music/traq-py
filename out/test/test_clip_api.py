# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from traq.api.clip_api import ClipApi


class TestClipApi(unittest.TestCase):
    """ClipApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ClipApi()

    def tearDown(self) -> None:
        pass

    def test_clip_message(self) -> None:
        """Test case for clip_message

        メッセージをクリップフォルダに追加
        """
        pass

    def test_create_clip_folder(self) -> None:
        """Test case for create_clip_folder

        クリップフォルダを作成
        """
        pass

    def test_delete_clip_folder(self) -> None:
        """Test case for delete_clip_folder

        クリップフォルダを削除
        """
        pass

    def test_edit_clip_folder(self) -> None:
        """Test case for edit_clip_folder

        クリップフォルダ情報を編集
        """
        pass

    def test_get_clip_folder(self) -> None:
        """Test case for get_clip_folder

        クリップフォルダ情報を取得
        """
        pass

    def test_get_clip_folders(self) -> None:
        """Test case for get_clip_folders

        クリップフォルダのリストを取得
        """
        pass

    def test_get_clips(self) -> None:
        """Test case for get_clips

        フォルダ内のクリップのリストを取得
        """
        pass

    def test_get_message_clips(self) -> None:
        """Test case for get_message_clips

        自分のクリップを取得
        """
        pass

    def test_unclip_message(self) -> None:
        """Test case for unclip_message

        メッセージをクリップフォルダから除外
        """
        pass


if __name__ == '__main__':
    unittest.main()
