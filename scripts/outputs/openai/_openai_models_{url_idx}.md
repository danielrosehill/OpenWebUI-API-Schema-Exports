# /openai/models/{url_idx}

## Table of contents:
- [get](#get)

- [json file](./_openai_models_{url_idx}.json)

---
<a name="get"></a>
## get

**tags:** ['openai']

**summary:** Get Models

**operationId:** get_models_openai_models__url_idx__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'path', 'required': True, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

