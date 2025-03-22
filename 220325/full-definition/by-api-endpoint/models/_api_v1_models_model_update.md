# /api/v1/models/model/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['models']

**summary:** Update Model By Id

**operationId:** update_model_by_id_api_v1_models_model_update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'query', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ModelForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ModelModel'}, {'type': 'null'}], 'title': 'Response Update Model By Id Api V1 Models Model Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

