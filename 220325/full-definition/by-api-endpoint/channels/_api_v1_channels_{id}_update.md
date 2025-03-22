# /api/v1/channels/{id}/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['channels']

**summary:** Update Channel By Id

**operationId:** update_channel_by_id_api_v1_channels__id__update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ChannelForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ChannelModel'}, {'type': 'null'}], 'title': 'Response Update Channel By Id Api V1 Channels  Id  Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

