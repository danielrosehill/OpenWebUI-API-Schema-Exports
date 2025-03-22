# /api/v1/users/default/permissions

## Table of contents:
- [get](#get)
- [post](#post)

<a name="get" />
## get

**tags:** ['users']

**summary:** Get User Permissions

**operationId:** get_user_permissions_api_v1_users_default_permissions_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/UserPermissions'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post" />
## post

**tags:** ['users']

**summary:** Update User Permissions

**operationId:** update_user_permissions_api_v1_users_default_permissions_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/UserPermissions'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

