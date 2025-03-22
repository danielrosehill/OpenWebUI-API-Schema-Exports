# /api/v1/pipelines/

## Table of contents:
- [get](#get)

<a name="get" />
## get

**tags:** ['pipelines']

**summary:** Get Pipelines

**operationId:** get_pipelines_api_v1_pipelines__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'urlIdx', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Urlidx'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

