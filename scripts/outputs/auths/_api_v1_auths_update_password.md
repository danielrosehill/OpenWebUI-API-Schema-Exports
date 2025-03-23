# /api/v1/auths/update/password

## Table of contents:
- [post](#post)

- [json file](./_api_v1_auths_update_password.json)

---
<a name="post"></a>
## post

**tags:** ['auths']

**summary:** Update Password

**operationId:** update_password_api_v1_auths_update_password_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/UpdatePasswordForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Update Password Api V1 Auths Update Password Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

