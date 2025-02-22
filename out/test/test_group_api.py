# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from traq.api.group_api import GroupApi


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GroupApi()

    def tearDown(self) -> None:
        pass

    def test_add_user_group_admin(self) -> None:
        """Test case for add_user_group_admin

        グループ管理者を追加
        """
        pass

    def test_add_user_group_member(self) -> None:
        """Test case for add_user_group_member

        グループメンバーを追加
        """
        pass

    def test_change_user_group_icon(self) -> None:
        """Test case for change_user_group_icon

        ユーザーグループのアイコンを変更
        """
        pass

    def test_create_user_group(self) -> None:
        """Test case for create_user_group

        ユーザーグループを作成
        """
        pass

    def test_delete_user_group(self) -> None:
        """Test case for delete_user_group

        ユーザーグループを削除
        """
        pass

    def test_edit_user_group(self) -> None:
        """Test case for edit_user_group

        ユーザーグループを編集
        """
        pass

    def test_edit_user_group_member(self) -> None:
        """Test case for edit_user_group_member

        グループメンバーを編集
        """
        pass

    def test_get_user_group(self) -> None:
        """Test case for get_user_group

        ユーザーグループを取得
        """
        pass

    def test_get_user_group_admins(self) -> None:
        """Test case for get_user_group_admins

        グループ管理者を取得
        """
        pass

    def test_get_user_group_members(self) -> None:
        """Test case for get_user_group_members

        グループメンバーを取得
        """
        pass

    def test_get_user_groups(self) -> None:
        """Test case for get_user_groups

        ユーザーグループのリストを取得
        """
        pass

    def test_remove_user_group_admin(self) -> None:
        """Test case for remove_user_group_admin

        グループ管理者を削除
        """
        pass

    def test_remove_user_group_member(self) -> None:
        """Test case for remove_user_group_member

        グループメンバーを削除
        """
        pass


if __name__ == '__main__':
    unittest.main()
