# /ollama/api/show

## Table of contents:
- [post](#post)

- [json file](./_ollama_api_show.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Show Model Info

**operationId:** show_model_info_ollama_api_show_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ModelNameForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

