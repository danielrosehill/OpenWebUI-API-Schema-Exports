# /api/v1/retrieval/process/text

## Table of contents:
- [post](#post)

- [json file](./_api_v1_retrieval_process_text.json)

---
<a name="post"></a>
## post

**tags:** ['retrieval']

**summary:** Process Text

**operationId:** process_text_api_v1_retrieval_process_text_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ProcessTextForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

