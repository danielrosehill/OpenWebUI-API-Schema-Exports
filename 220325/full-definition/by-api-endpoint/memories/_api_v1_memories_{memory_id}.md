# /api/v1/memories/{memory_id}

## Table of contents:
- [delete](#delete)

<a name="delete" />
## delete

**tags:** ['memories']

**summary:** Delete Memory By Id

**operationId:** delete_memory_by_id_api_v1_memories__memory_id__delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'memory_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Memory Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Memory By Id Api V1 Memories  Memory Id  Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

