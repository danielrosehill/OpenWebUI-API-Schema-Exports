# /api/v1/users/{user_id}/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['users']

**summary:** Update User By Id

**operationId:** update_user_by_id_api_v1_users__user_id__update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'user_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'User Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/UserUpdateForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/UserModel'}, {'type': 'null'}], 'title': 'Response Update User By Id Api V1 Users  User Id  Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

