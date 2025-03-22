# /api/v1/tasks/emoji/completions

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['tasks']

**summary:** Generate Emoji

**operationId:** generate_emoji_api_v1_tasks_emoji_completions_post

**requestBody:** {'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

