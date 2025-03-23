# /api/v1/channels/{id}/messages/post

## Table of contents:
- [post](#post)

- [json file](./_api_v1_channels_{id}_messages_post.json)

---
<a name="post"></a>
## post

**tags:** ['channels']

**summary:** Post New Message

**operationId:** post_new_message_api_v1_channels__id__messages_post_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/MessageForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/MessageModel'}, {'type': 'null'}], 'title': 'Response Post New Message Api V1 Channels  Id  Messages Post Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

