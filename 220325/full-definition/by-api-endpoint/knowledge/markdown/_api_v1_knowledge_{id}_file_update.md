# /api/v1/knowledge/{id}/file/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['knowledge']

**summary:** Update File From Knowledge By Id

**operationId:** update_file_from_knowledge_by_id_api_v1_knowledge__id__file_update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/KnowledgeFileIdForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/KnowledgeFilesResponse'}, {'type': 'null'}], 'title': 'Response Update File From Knowledge By Id Api V1 Knowledge  Id  File Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

