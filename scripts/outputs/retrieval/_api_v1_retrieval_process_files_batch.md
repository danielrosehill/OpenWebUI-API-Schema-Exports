# /api/v1/retrieval/process/files/batch

## Table of contents:
- [post](#post)

- [json file](./_api_v1_retrieval_process_files_batch.json)

---
<a name="post"></a>
## post

**tags:** ['retrieval']

**summary:** Process Files Batch

**description:** Process a batch of files and save them to the vector database.

**operationId:** process_files_batch_api_v1_retrieval_process_files_batch_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/BatchProcessFilesForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/BatchProcessFilesResponse'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

