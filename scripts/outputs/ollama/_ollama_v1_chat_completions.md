# /ollama/v1/chat/completions

## Table of contents:
- [post](#post)

- [json file](./_ollama_v1_chat_completions.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Generate Openai Chat Completion

**operationId:** generate_openai_chat_completion_ollama_v1_chat_completions_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

