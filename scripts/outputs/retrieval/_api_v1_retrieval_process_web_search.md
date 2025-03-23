# /api/v1/retrieval/process/web/search

## Table of contents:
- [post](#post)

- [json file](./_api_v1_retrieval_process_web_search.json)

---
<a name="post"></a>
## post

**tags:** ['retrieval']

**summary:** Process Web Search

**operationId:** process_web_search_api_v1_retrieval_process_web_search_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/SearchForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

