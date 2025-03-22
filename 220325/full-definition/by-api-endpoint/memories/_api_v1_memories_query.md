# /api/v1/memories/query

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['memories']

**summary:** Query Memory

**operationId:** query_memory_api_v1_memories_query_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/QueryMemoryForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

