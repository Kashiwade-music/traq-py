# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from traq.models.patch_group_member_request import PatchGroupMemberRequest

class TestPatchGroupMemberRequest(unittest.TestCase):
    """PatchGroupMemberRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchGroupMemberRequest:
        """Test PatchGroupMemberRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchGroupMemberRequest`
        """
        model = PatchGroupMemberRequest()
        if include_optional:
            return PatchGroupMemberRequest(
                role = ''
            )
        else:
            return PatchGroupMemberRequest(
                role = '',
        )
        """

    def testPatchGroupMemberRequest(self):
        """Test PatchGroupMemberRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
