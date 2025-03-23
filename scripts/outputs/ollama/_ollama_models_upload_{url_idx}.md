# /ollama/models/upload/{url_idx}

## Table of contents:
- [post](#post)

- [json file](./_ollama_models_upload_{url_idx}.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Upload Model

**operationId:** upload_model_ollama_models_upload__url_idx__post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'path', 'required': True, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'multipart/form-data': {'schema': {'$ref': '#/components/schemas/Body_upload_model_ollama_models_upload__url_idx__post'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

