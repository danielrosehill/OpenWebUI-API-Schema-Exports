# /api/v1/pipelines/upload

## Table of contents:
- [post](#post)

- [json file](./_api_v1_pipelines_upload.json)

---
<a name="post"></a>
## post

**tags:** ['pipelines']

**summary:** Upload Pipeline

**operationId:** upload_pipeline_api_v1_pipelines_upload_post

**requestBody:** {'content': {'multipart/form-data': {'schema': {'$ref': '#/components/schemas/Body_upload_pipeline_api_v1_pipelines_upload_post'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

