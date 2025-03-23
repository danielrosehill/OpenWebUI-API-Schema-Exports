# /api/chat/actions/{action_id}

## Table of contents:
- [post](#post)

- [json file](./_api_chat_actions_{action_id}.json)

---
<a name="post"></a>
## post

**summary:** Chat Action

**operationId:** chat_action_api_chat_actions__action_id__post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'action_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Action Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

