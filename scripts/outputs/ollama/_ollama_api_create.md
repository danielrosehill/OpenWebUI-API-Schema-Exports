# /ollama/api/create

## Table of contents:
- [post](#post)

- [json file](./_ollama_api_create.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Create Model

**operationId:** create_model_ollama_api_create_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'query', 'required': False, 'schema': {'type': 'integer', 'default': 0, 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/CreateModelForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

