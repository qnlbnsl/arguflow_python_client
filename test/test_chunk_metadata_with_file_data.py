# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.models.chunk_metadata_with_file_data import ChunkMetadataWithFileData

class TestChunkMetadataWithFileData(unittest.TestCase):
    """ChunkMetadataWithFileData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChunkMetadataWithFileData:
        """Test ChunkMetadataWithFileData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChunkMetadataWithFileData`
        """
        model = ChunkMetadataWithFileData()
        if include_optional:
            return ChunkMetadataWithFileData(
                author = trieve_python_client.models.user_dto.UserDTO(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    email = '', 
                    id = '', 
                    username = '', 
                    visible_email = True, 
                    website = '', ),
                chunk_html = '',
                content = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                file_id = '',
                file_name = '',
                id = '',
                link = '',
                metadata = None,
                qdrant_point_id = '',
                tag_set = '',
                time_stamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tracking_id = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                weight = 1.337
            )
        else:
            return ChunkMetadataWithFileData(
                content = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                qdrant_point_id = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                weight = 1.337,
        )
        """

    def testChunkMetadataWithFileData(self):
        """Test ChunkMetadataWithFileData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
