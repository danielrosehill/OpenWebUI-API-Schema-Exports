# /api/v1/tasks/image_prompt/completions

## Table of contents:
- [post](#post)

- [json file](./_api_v1_tasks_image_prompt_completions.json)

---
<a name="post"></a>
## post

**tags:** ['tasks']

**summary:** Generate Image Prompt

**operationId:** generate_image_prompt_api_v1_tasks_image_prompt_completions_post

**requestBody:** {'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

