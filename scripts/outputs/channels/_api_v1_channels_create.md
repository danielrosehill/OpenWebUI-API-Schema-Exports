# /api/v1/channels/create

## Table of contents:
- [post](#post)

- [json file](./_api_v1_channels_create.json)

---
<a name="post"></a>
## post

**tags:** ['channels']

**summary:** Create New Channel

**operationId:** create_new_channel_api_v1_channels_create_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ChannelForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ChannelModel'}, {'type': 'null'}], 'title': 'Response Create New Channel Api V1 Channels Create Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

