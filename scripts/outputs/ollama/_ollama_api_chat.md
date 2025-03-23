# /ollama/api/chat

## Table of contents:
- [post](#post)

- [json file](./_ollama_api_chat.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Generate Chat Completion

**operationId:** generate_chat_completion_ollama_api_chat_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}, {'name': 'bypass_filter', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'boolean'}, {'type': 'null'}], 'default': False, 'title': 'Bypass Filter'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

