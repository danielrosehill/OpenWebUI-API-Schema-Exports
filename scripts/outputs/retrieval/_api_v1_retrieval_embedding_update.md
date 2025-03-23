# /api/v1/retrieval/embedding/update

## Table of contents:
- [post](#post)

- [json file](./_api_v1_retrieval_embedding_update.json)

---
<a name="post"></a>
## post

**tags:** ['retrieval']

**summary:** Update Embedding Config

**operationId:** update_embedding_config_api_v1_retrieval_embedding_update_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/EmbeddingModelUpdateForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

