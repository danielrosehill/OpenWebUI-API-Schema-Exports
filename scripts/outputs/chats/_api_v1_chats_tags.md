# /api/v1/chats/tags

## Table of contents:
- [post](#post)

- [json file](./_api_v1_chats_tags.json)

---
<a name="post"></a>
## post

**tags:** ['chats']

**summary:** Get User Chat List By Tag Name

**operationId:** get_user_chat_list_by_tag_name_api_v1_chats_tags_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/TagFilterForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'items': {'$ref': '#/components/schemas/ChatTitleIdResponse'}, 'type': 'array', 'title': 'Response Get User Chat List By Tag Name Api V1 Chats Tags Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

