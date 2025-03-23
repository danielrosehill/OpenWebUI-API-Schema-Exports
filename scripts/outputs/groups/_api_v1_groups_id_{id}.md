# /api/v1/groups/id/{id}

## Table of contents:
- [get](#get)

- [json file](./_api_v1_groups_id_{id}.json)

---
<a name="get"></a>
## get

**tags:** ['groups']

**summary:** Get Group By Id

**operationId:** get_group_by_id_api_v1_groups_id__id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/GroupResponse'}, {'type': 'null'}], 'title': 'Response Get Group By Id Api V1 Groups Id  Id  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

