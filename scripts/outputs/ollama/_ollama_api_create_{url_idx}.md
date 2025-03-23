# /ollama/api/create/{url_idx}

## Table of contents:
- [post](#post)

- [json file](./_ollama_api_create_{url_idx}.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Create Model

**operationId:** create_model_ollama_api_create__url_idx__post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'path', 'required': True, 'schema': {'type': 'integer', 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/CreateModelForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

