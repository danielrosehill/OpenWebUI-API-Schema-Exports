# /api/v1/models/model/delete

## Table of contents:
- [delete](#delete)

<a name="delete" />
## delete

**tags:** ['models']

**summary:** Delete Model By Id

**operationId:** delete_model_by_id_api_v1_models_model_delete_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'query', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Model By Id Api V1 Models Model Delete Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

