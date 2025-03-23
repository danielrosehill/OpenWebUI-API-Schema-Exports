# /api/v1/utils/gravatar

## Table of contents:
- [get](#get)

- [json file](./_api_v1_utils_gravatar.json)

---
<a name="get"></a>
## get

**tags:** ['utils']

**summary:** Get Gravatar

**operationId:** get_gravatar_api_v1_utils_gravatar_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'email', 'in': 'query', 'required': True, 'schema': {'type': 'string', 'title': 'Email'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

