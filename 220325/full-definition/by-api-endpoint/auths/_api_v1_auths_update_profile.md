# /api/v1/auths/update/profile

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['auths']

**summary:** Update Profile

**operationId:** update_profile_api_v1_auths_update_profile_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/UpdateProfileForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/open_webui__models__auths__UserResponse'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

