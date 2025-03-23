# /api/v1/channels/{id}/messages/{message_id}/reactions/remove

## Table of contents:
- [post](#post)

- [json file](./_api_v1_channels_{id}_messages_{message_id}_reactions_remove.json)

---
<a name="post"></a>
## post

**tags:** ['channels']

**summary:** Remove Reaction By Id And User Id And Name

**operationId:** remove_reaction_by_id_and_user_id_and_name_api_v1_channels__id__messages__message_id__reactions_remove_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}, {'name': 'message_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Message Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ReactionForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Remove Reaction By Id And User Id And Name Api V1 Channels  Id  Messages  Message Id  Reactions Remove Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

