# /api/v1/retrieval/delete

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['retrieval']

**summary:** Delete Entries From Collection

**operationId:** delete_entries_from_collection_api_v1_retrieval_delete_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/DeleteForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

