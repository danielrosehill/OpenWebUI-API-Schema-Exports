# /api/v1/knowledge/{id}

## Table of contents:
- [get](#get)

- [json file](./_api_v1_knowledge_{id}.json)

---
<a name="get"></a>
## get

**tags:** ['knowledge']

**summary:** Get Knowledge By Id

**operationId:** get_knowledge_by_id_api_v1_knowledge__id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/KnowledgeFilesResponse'}, {'type': 'null'}], 'title': 'Response Get Knowledge By Id Api V1 Knowledge  Id  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

