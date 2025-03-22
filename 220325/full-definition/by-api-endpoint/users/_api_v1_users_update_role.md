# /api/v1/users/update/role

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['users']

**summary:** Update User Role

**operationId:** update_user_role_api_v1_users_update_role_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/UserRoleUpdateForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/UserModel'}, {'type': 'null'}], 'title': 'Response Update User Role Api V1 Users Update Role Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

