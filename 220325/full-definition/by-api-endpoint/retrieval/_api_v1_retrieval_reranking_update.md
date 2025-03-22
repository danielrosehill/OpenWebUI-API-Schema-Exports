# /api/v1/retrieval/reranking/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['retrieval']

**summary:** Update Reranking Config

**operationId:** update_reranking_config_api_v1_retrieval_reranking_update_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/RerankingModelUpdateForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

