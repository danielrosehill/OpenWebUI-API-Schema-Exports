# /ollama/api/push/{url_idx}

## Table of contents:
- [delete](#delete)

- [json file](./_ollama_api_push_{url_idx}.json)

---
<a name="delete"></a>
## delete

**tags:** ['ollama']

**summary:** Push Model

**operationId:** push_model_ollama_api_push__url_idx__delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'path', 'required': True, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/PushModelForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

