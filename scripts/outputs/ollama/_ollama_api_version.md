# /ollama/api/version

## Table of contents:
- [get](#get)

- [json file](./_ollama_api_version.json)

---
<a name="get"></a>
## get

**tags:** ['ollama']

**summary:** Get Ollama Versions

**operationId:** get_ollama_versions_ollama_api_version_get

**parameters:** [{'name': 'url_idx', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

