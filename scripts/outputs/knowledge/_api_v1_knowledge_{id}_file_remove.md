# /api/v1/knowledge/{id}/file/remove

## Table of contents:
- [post](#post)

- [json file](./_api_v1_knowledge_{id}_file_remove.json)

---
<a name="post"></a>
## post

**tags:** ['knowledge']

**summary:** Remove File From Knowledge By Id

**operationId:** remove_file_from_knowledge_by_id_api_v1_knowledge__id__file_remove_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/KnowledgeFileIdForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/KnowledgeFilesResponse'}, {'type': 'null'}], 'title': 'Response Remove File From Knowledge By Id Api V1 Knowledge  Id  File Remove Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

