# /api/v1/tools/id/{id}/valves/spec

## Table of contents:
- [get](#get)

<a name="get" />
## get

**tags:** ['tools']

**summary:** Get Tools Valves Spec By Id

**operationId:** get_tools_valves_spec_by_id_api_v1_tools_id__id__valves_spec_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'title': 'Response Get Tools Valves Spec By Id Api V1 Tools Id  Id  Valves Spec Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

