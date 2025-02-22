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

from traq.models.parent_changed_event import ParentChangedEvent

class TestParentChangedEvent(unittest.TestCase):
    """ParentChangedEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParentChangedEvent:
        """Test ParentChangedEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParentChangedEvent`
        """
        model = ParentChangedEvent()
        if include_optional:
            return ParentChangedEvent(
                user_id = '',
                before = '',
                after = ''
            )
        else:
            return ParentChangedEvent(
                user_id = '',
                before = '',
                after = '',
        )
        """

    def testParentChangedEvent(self):
        """Test ParentChangedEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
