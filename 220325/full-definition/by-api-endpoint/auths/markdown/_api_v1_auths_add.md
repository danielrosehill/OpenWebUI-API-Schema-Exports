# /api/v1/auths/add

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['auths']

**summary:** Add User

**operationId:** add_user_api_v1_auths_add_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/AddUserForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/SigninResponse'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

