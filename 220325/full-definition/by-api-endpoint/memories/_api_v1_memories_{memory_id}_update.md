# /api/v1/memories/{memory_id}/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['memories']

**summary:** Update Memory By Id

**operationId:** update_memory_by_id_api_v1_memories__memory_id__update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'memory_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Memory Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/MemoryUpdateModel'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/MemoryModel'}, {'type': 'null'}], 'title': 'Response Update Memory By Id Api V1 Memories  Memory Id  Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

