# /api/v1/prompts/command/{command}

## Table of contents:
- [get](#get)

- [json file](./_api_v1_prompts_command_{command}.json)

---
<a name="get"></a>
## get

**tags:** ['prompts']

**summary:** Get Prompt By Command

**operationId:** get_prompt_by_command_api_v1_prompts_command__command__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'command', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Command'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/PromptModel'}, {'type': 'null'}], 'title': 'Response Get Prompt By Command Api V1 Prompts Command  Command  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

