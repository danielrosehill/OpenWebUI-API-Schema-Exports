# /ollama/config/update

## Table of contents:
- [post](#post)

- [json file](./_ollama_config_update.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Update Config

**operationId:** update_config_ollama_config_update_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/open_webui__routers__ollama__OllamaConfigForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

