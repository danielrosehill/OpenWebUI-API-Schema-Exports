# /api/v1/channels/{id}/messages

## Table of contents:
- [get](#get)

<a name="get" />
## get

**tags:** ['channels']

**summary:** Get Channel Messages

**operationId:** get_channel_messages_api_v1_channels__id__messages_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}, {'name': 'skip', 'in': 'query', 'required': False, 'schema': {'type': 'integer', 'default': 0, 'title': 'Skip'}}, {'name': 'limit', 'in': 'query', 'required': False, 'schema': {'type': 'integer', 'default': 50, 'title': 'Limit'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/MessageUserResponse'}, 'title': 'Response Get Channel Messages Api V1 Channels  Id  Messages Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

