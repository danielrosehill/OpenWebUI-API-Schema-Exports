# /api/v1/channels/{id}/messages/{message_id}/reactions/add

## Table of contents:
- [post](#post)

- [json file](./_api_v1_channels_{id}_messages_{message_id}_reactions_add.json)

---
<a name="post"></a>
## post

**tags:** ['channels']

**summary:** Add Reaction To Message

**operationId:** add_reaction_to_message_api_v1_channels__id__messages__message_id__reactions_add_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}, {'name': 'message_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Message Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ReactionForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Add Reaction To Message Api V1 Channels  Id  Messages  Message Id  Reactions Add Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

