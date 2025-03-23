# /api/v1/prompts/command/{command}/delete

## Table of contents:
- [delete](#delete)

- [json file](./_api_v1_prompts_command_{command}_delete.json)

---
<a name="delete"></a>
## delete

**tags:** ['prompts']

**summary:** Delete Prompt By Command

**operationId:** delete_prompt_by_command_api_v1_prompts_command__command__delete_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'command', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Command'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Prompt By Command Api V1 Prompts Command  Command  Delete Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

