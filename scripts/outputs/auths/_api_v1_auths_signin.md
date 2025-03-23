# /api/v1/auths/signin

## Table of contents:
- [post](#post)

- [json file](./_api_v1_auths_signin.json)

---
<a name="post"></a>
## post

**tags:** ['auths']

**summary:** Signin

**operationId:** signin_api_v1_auths_signin_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/SigninForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/SessionUserResponse'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

