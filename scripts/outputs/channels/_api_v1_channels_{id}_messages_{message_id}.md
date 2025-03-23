# /api/v1/channels/{id}/messages/{message_id}

## Table of contents:
- [get](#get)

- [json file](./_api_v1_channels_{id}_messages_{message_id}.json)

---
<a name="get"></a>
## get

**tags:** ['channels']

**summary:** Get Channel Message

**operationId:** get_channel_message_api_v1_channels__id__messages__message_id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}, {'name': 'message_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Message Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/MessageUserResponse'}, {'type': 'null'}], 'title': 'Response Get Channel Message Api V1 Channels  Id  Messages  Message Id  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

