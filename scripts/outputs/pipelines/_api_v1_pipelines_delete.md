# /api/v1/pipelines/delete

## Table of contents:
- [delete](#delete)

- [json file](./_api_v1_pipelines_delete.json)

---
<a name="delete"></a>
## delete

**tags:** ['pipelines']

**summary:** Delete Pipeline

**operationId:** delete_pipeline_api_v1_pipelines_delete_delete

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/DeletePipelineForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

