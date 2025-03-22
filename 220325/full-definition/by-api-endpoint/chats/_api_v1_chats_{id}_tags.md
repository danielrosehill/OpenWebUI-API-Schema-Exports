# /api/v1/chats/{id}/tags

## Table of contents:
- [get](#get)
- [post](#post)
- [delete](#delete)

<a name="get" />
## get

**tags:** ['chats']

**summary:** Get Chat Tags By Id

**operationId:** get_chat_tags_by_id_api_v1_chats__id__tags_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/TagModel'}, 'title': 'Response Get Chat Tags By Id Api V1 Chats  Id  Tags Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

<a name="post" />
## post

**tags:** ['chats']

**summary:** Add Tag By Id And Tag Name

**operationId:** add_tag_by_id_and_tag_name_api_v1_chats__id__tags_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/TagForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/TagModel'}, 'title': 'Response Add Tag By Id And Tag Name Api V1 Chats  Id  Tags Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

<a name="delete" />
## delete

**tags:** ['chats']

**summary:** Delete Tag By Id And Tag Name

**operationId:** delete_tag_by_id_and_tag_name_api_v1_chats__id__tags_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/TagForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/TagModel'}, 'title': 'Response Delete Tag By Id And Tag Name Api V1 Chats  Id  Tags Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

