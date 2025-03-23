# /ollama/api/pull/{url_idx}

## Table of contents:
- [post](#post)

- [json file](./_ollama_api_pull_{url_idx}.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Pull Model

**operationId:** pull_model_ollama_api_pull__url_idx__post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'path', 'required': True, 'schema': {'type': 'integer', 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ModelNameForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

