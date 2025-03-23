# /api/v1/functions/id/{id}/valves

## Table of contents:
- [get](#get)

- [json file](./_api_v1_functions_id_{id}_valves.json)

---
<a name="get"></a>
## get

**tags:** ['functions']

**summary:** Get Function Valves By Id

**operationId:** get_function_valves_by_id_api_v1_functions_id__id__valves_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'title': 'Response Get Function Valves By Id Api V1 Functions Id  Id  Valves Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

