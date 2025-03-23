# /api/v1/retrieval/process/file

## Table of contents:
- [post](#post)

- [json file](./_api_v1_retrieval_process_file.json)

---
<a name="post"></a>
## post

**tags:** ['retrieval']

**summary:** Process File

**operationId:** process_file_api_v1_retrieval_process_file_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ProcessFileForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

