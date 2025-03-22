# /api/v1/configs/direct_connections

## Table of contents:
- [get](#get)
- [post](#post)

<a name="get" />
## get

**tags:** ['configs']

**summary:** Get Direct Connections Config

**operationId:** get_direct_connections_config_api_v1_configs_direct_connections_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/DirectConnectionsConfigForm'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post" />
## post

**tags:** ['configs']

**summary:** Set Direct Connections Config

**operationId:** set_direct_connections_config_api_v1_configs_direct_connections_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/DirectConnectionsConfigForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/DirectConnectionsConfigForm'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

