# /api/v1/prompts/command/{command}/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['prompts']

**summary:** Update Prompt By Command

**operationId:** update_prompt_by_command_api_v1_prompts_command__command__update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'command', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Command'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/PromptForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/PromptModel'}, {'type': 'null'}], 'title': 'Response Update Prompt By Command Api V1 Prompts Command  Command  Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

