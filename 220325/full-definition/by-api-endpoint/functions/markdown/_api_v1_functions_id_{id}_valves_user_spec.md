# /api/v1/functions/id/{id}/valves/user/spec

## Table of contents:
- [get](#get)

<a name="get" />
## get

**tags:** ['functions']

**summary:** Get Function User Valves Spec By Id

**operationId:** get_function_user_valves_spec_by_id_api_v1_functions_id__id__valves_user_spec_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'title': 'Response Get Function User Valves Spec By Id Api V1 Functions Id  Id  Valves User Spec Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

