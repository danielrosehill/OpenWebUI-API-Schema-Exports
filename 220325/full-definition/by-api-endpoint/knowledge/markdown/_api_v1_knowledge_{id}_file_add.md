# /api/v1/knowledge/{id}/file/add

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['knowledge']

**summary:** Add File To Knowledge By Id

**operationId:** add_file_to_knowledge_by_id_api_v1_knowledge__id__file_add_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/KnowledgeFileIdForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/KnowledgeFilesResponse'}, {'type': 'null'}], 'title': 'Response Add File To Knowledge By Id Api V1 Knowledge  Id  File Add Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

