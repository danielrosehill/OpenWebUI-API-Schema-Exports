# /openai/models

## Table of contents:
- [get](#get)

- [json file](./_openai_models.json)

---
<a name="get"></a>
## get

**tags:** ['openai']

**summary:** Get Models

**operationId:** get_models_openai_models_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

