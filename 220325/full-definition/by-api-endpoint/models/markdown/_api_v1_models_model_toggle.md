# /api/v1/models/model/toggle

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['models']

**summary:** Toggle Model By Id

**operationId:** toggle_model_by_id_api_v1_models_model_toggle_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'query', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ModelResponse'}, {'type': 'null'}], 'title': 'Response Toggle Model By Id Api V1 Models Model Toggle Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

