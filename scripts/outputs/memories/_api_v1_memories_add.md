# /api/v1/memories/add

## Table of contents:
- [post](#post)

- [json file](./_api_v1_memories_add.json)

---
<a name="post"></a>
## post

**tags:** ['memories']

**summary:** Add Memory

**operationId:** add_memory_api_v1_memories_add_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/AddMemoryForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/MemoryModel'}, {'type': 'null'}], 'title': 'Response Add Memory Api V1 Memories Add Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

