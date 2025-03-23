# /ollama/v1/models

## Table of contents:
- [get](#get)

- [json file](./_ollama_v1_models.json)

---
<a name="get"></a>
## get

**tags:** ['ollama']

**summary:** Get Openai Models

**operationId:** get_openai_models_ollama_v1_models_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

