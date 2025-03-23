# /api/v1/tasks/title/completions

## Table of contents:
- [post](#post)

- [json file](./_api_v1_tasks_title_completions.json)

---
<a name="post"></a>
## post

**tags:** ['tasks']

**summary:** Generate Title

**operationId:** generate_title_api_v1_tasks_title_completions_post

**requestBody:** {'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

