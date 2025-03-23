# /api/chat/completions

## Table of contents:
- [post](#post)

- [json file](./_api_chat_completions.json)

---
<a name="post"></a>
## post

**summary:** Chat Completion

**operationId:** chat_completion_api_chat_completions_post

**requestBody:** {'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

