# /api/v1/prompts/list

## Table of contents:
- [get](#get)

- [json file](./_api_v1_prompts_list.json)

---
<a name="get"></a>
## get

**tags:** ['prompts']

**summary:** Get Prompt List

**operationId:** get_prompt_list_api_v1_prompts_list_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'items': {'$ref': '#/components/schemas/PromptUserResponse'}, 'type': 'array', 'title': 'Response Get Prompt List Api V1 Prompts List Get'}}}}}

**security:** [{'HTTPBearer': []}]

