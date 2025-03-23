# /ollama/api/delete/{url_idx}

## Table of contents:
- [delete](#delete)

- [json file](./_ollama_api_delete_{url_idx}.json)

---
<a name="delete"></a>
## delete

**tags:** ['ollama']

**summary:** Delete Model

**operationId:** delete_model_ollama_api_delete__url_idx__delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'path', 'required': True, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ModelNameForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

