# /api/v1/users/user/info/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['users']

**summary:** Update User Info By Session User

**operationId:** update_user_info_by_session_user_api_v1_users_user_info_update_post

**requestBody:** {'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'title': 'Response Update User Info By Session User Api V1 Users User Info Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

