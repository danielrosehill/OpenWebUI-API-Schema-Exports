# /api/v1/prompts/create

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['prompts']

**summary:** Create New Prompt

**operationId:** create_new_prompt_api_v1_prompts_create_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/PromptForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/PromptModel'}, {'type': 'null'}], 'title': 'Response Create New Prompt Api V1 Prompts Create Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

