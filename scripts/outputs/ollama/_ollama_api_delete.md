# /ollama/api/delete

## Table of contents:
- [delete](#delete)

- [json file](./_ollama_api_delete.json)

---
<a name="delete"></a>
## delete

**tags:** ['ollama']

**summary:** Delete Model

**operationId:** delete_model_ollama_api_delete_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ModelNameForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

