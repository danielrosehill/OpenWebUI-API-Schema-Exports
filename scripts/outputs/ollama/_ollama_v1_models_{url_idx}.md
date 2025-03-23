# /ollama/v1/models/{url_idx}

## Table of contents:
- [get](#get)

- [json file](./_ollama_v1_models_{url_idx}.json)

---
<a name="get"></a>
## get

**tags:** ['ollama']

**summary:** Get Openai Models

**operationId:** get_openai_models_ollama_v1_models__url_idx__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'path', 'required': True, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

