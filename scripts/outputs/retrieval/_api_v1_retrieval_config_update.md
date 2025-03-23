# /api/v1/retrieval/config/update

## Table of contents:
- [post](#post)

- [json file](./_api_v1_retrieval_config_update.json)

---
<a name="post"></a>
## post

**tags:** ['retrieval']

**summary:** Update Rag Config

**operationId:** update_rag_config_api_v1_retrieval_config_update_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ConfigUpdateForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

