# /api/v1/pipelines/add

## Table of contents:
- [post](#post)

- [json file](./_api_v1_pipelines_add.json)

---
<a name="post"></a>
## post

**tags:** ['pipelines']

**summary:** Add Pipeline

**operationId:** add_pipeline_api_v1_pipelines_add_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/AddPipelineForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

