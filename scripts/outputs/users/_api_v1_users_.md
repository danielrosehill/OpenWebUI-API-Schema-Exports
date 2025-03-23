# /api/v1/users/

## Table of contents:
- [get](#get)

- [json file](./_api_v1_users_.json)

---
<a name="get"></a>
## get

**tags:** ['users']

**summary:** Get Users

**operationId:** get_users_api_v1_users__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'skip', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Skip'}}, {'name': 'limit', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Limit'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/UserModel'}, 'title': 'Response Get Users Api V1 Users  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

