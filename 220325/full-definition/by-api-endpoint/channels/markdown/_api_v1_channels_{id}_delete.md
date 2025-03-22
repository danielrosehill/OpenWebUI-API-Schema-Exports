# /api/v1/channels/{id}/delete

## Table of contents:
- [delete](#delete)

<a name="delete" />
## delete

**tags:** ['channels']

**summary:** Delete Channel By Id

**operationId:** delete_channel_by_id_api_v1_channels__id__delete_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Channel By Id Api V1 Channels  Id  Delete Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

