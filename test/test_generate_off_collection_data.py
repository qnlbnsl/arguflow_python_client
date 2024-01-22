# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.models.generate_off_collection_data import GenerateOffCollectionData

class TestGenerateOffCollectionData(unittest.TestCase):
    """GenerateOffCollectionData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenerateOffCollectionData:
        """Test GenerateOffCollectionData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateOffCollectionData`
        """
        model = GenerateOffCollectionData()
        if include_optional:
            return GenerateOffCollectionData(
                collection_id = '',
                page = 0,
                query = ''
            )
        else:
            return GenerateOffCollectionData(
                collection_id = '',
        )
        """

    def testGenerateOffCollectionData(self):
        """Test GenerateOffCollectionData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
