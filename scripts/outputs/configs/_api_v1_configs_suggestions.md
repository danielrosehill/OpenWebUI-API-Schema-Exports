# /api/v1/configs/suggestions

## Table of contents:
- [post](#post)

- [json file](./_api_v1_configs_suggestions.json)

---
<a name="post"></a>
## post

**tags:** ['configs']

**summary:** Set Default Suggestions

**operationId:** set_default_suggestions_api_v1_configs_suggestions_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/SetDefaultSuggestionsForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'items': {'$ref': '#/components/schemas/PromptSuggestion'}, 'type': 'array', 'title': 'Response Set Default Suggestions Api V1 Configs Suggestions Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

