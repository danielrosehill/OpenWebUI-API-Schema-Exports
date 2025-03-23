# /api/v1/channels/{id}/messages/{message_id}/delete

## Table of contents:
- [delete](#delete)

- [json file](./_api_v1_channels_{id}_messages_{message_id}_delete.json)

---
<a name="delete"></a>
## delete

**tags:** ['channels']

**summary:** Delete Message By Id

**operationId:** delete_message_by_id_api_v1_channels__id__messages__message_id__delete_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}, {'name': 'message_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Message Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Message By Id Api V1 Channels  Id  Messages  Message Id  Delete Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

