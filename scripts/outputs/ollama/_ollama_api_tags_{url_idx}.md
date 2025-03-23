# /ollama/api/tags/{url_idx}

## Table of contents:
- [get](#get)

- [json file](./_ollama_api_tags_{url_idx}.json)

---
<a name="get"></a>
## get

**tags:** ['ollama']

**summary:** Get Ollama Tags

**operationId:** get_ollama_tags_ollama_api_tags__url_idx__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'path', 'required': True, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

