# /api/v1/channels/{id}/messages/{message_id}/update

## Table of contents:
- [post](#post)

- [json file](./_api_v1_channels_{id}_messages_{message_id}_update.json)

---
<a name="post"></a>
## post

**tags:** ['channels']

**summary:** Update Message By Id

**operationId:** update_message_by_id_api_v1_channels__id__messages__message_id__update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}, {'name': 'message_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Message Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/MessageForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/MessageModel'}, {'type': 'null'}], 'title': 'Response Update Message By Id Api V1 Channels  Id  Messages  Message Id  Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

