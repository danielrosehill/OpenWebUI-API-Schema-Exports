# /openai/chat/completions

## Table of contents:
- [post](#post)

- [json file](./_openai_chat_completions.json)

---
<a name="post"></a>
## post

**tags:** ['openai']

**summary:** Generate Chat Completion

**operationId:** generate_chat_completion_openai_chat_completions_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'bypass_filter', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'boolean'}, {'type': 'null'}], 'default': False, 'title': 'Bypass Filter'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

