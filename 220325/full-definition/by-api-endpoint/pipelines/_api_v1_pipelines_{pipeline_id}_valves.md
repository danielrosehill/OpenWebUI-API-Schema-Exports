# /api/v1/pipelines/{pipeline_id}/valves

## Table of contents:
- [get](#get)

<a name="get" />
## get

**tags:** ['pipelines']

**summary:** Get Pipeline Valves

**operationId:** get_pipeline_valves_api_v1_pipelines__pipeline_id__valves_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'pipeline_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Pipeline Id'}}, {'name': 'urlIdx', 'in': 'query', 'required': True, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Urlidx'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

