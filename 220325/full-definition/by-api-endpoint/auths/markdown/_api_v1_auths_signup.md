# /api/v1/auths/signup

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['auths']

**summary:** Signup

**operationId:** signup_api_v1_auths_signup_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/SignupForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/SessionUserResponse'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

