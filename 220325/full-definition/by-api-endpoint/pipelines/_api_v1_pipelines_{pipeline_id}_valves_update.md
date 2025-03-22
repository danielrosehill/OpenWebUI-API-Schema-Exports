# /api/v1/pipelines/{pipeline_id}/valves/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['pipelines']

**summary:** Update Pipeline Valves

**operationId:** update_pipeline_valves_api_v1_pipelines__pipeline_id__valves_update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'pipeline_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Pipeline Id'}}, {'name': 'urlIdx', 'in': 'query', 'required': True, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Urlidx'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

