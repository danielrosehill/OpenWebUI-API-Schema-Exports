# /api/v1/retrieval/query/collection

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['retrieval']

**summary:** Query Collection Handler

**operationId:** query_collection_handler_api_v1_retrieval_query_collection_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/QueryCollectionsForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

