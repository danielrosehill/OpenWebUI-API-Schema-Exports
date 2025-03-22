# /api/v1/tasks/tags/completions

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['tasks']

**summary:** Generate Chat Tags

**operationId:** generate_chat_tags_api_v1_tasks_tags_completions_post

**requestBody:** {'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

