# /ollama/models/upload

## Table of contents:
- [post](#post)

- [json file](./_ollama_models_upload.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Upload Model

**operationId:** upload_model_ollama_models_upload_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'multipart/form-data': {'schema': {'$ref': '#/components/schemas/Body_upload_model_ollama_models_upload_post'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

