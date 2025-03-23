# /api/v1/auths/api_key

## Table of contents:
- [get](#get)

- [post](#post)

- [delete](#delete)

- [json file](./_api_v1_auths_api_key.json)

---
<a name="get"></a>
## get

**tags:** ['auths']

**summary:** Get Api Key

**operationId:** get_api_key_api_v1_auths_api_key_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ApiKey'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post"></a>
## post

**tags:** ['auths']

**summary:** Generate Api Key

**operationId:** generate_api_key_api_v1_auths_api_key_post

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ApiKey'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="delete"></a>
## delete

**tags:** ['auths']

**summary:** Delete Api Key

**operationId:** delete_api_key_api_v1_auths_api_key_delete

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Api Key Api V1 Auths Api Key Delete'}}}}}

**security:** [{'HTTPBearer': []}]

