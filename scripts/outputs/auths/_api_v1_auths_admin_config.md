# /api/v1/auths/admin/config

## Table of contents:
- [get](#get)

- [post](#post)

- [json file](./_api_v1_auths_admin_config.json)

---
<a name="get"></a>
## get

**tags:** ['auths']

**summary:** Get Admin Config

**operationId:** get_admin_config_api_v1_auths_admin_config_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post"></a>
## post

**tags:** ['auths']

**summary:** Update Admin Config

**operationId:** update_admin_config_api_v1_auths_admin_config_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/AdminConfig'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

