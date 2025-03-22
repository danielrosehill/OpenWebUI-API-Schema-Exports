# /api/v1/retrieval/query/doc

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['retrieval']

**summary:** Query Doc Handler

**operationId:** query_doc_handler_api_v1_retrieval_query_doc_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/QueryDocForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

