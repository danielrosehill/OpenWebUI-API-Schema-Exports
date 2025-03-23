# /api/tasks/stop/{task_id}

## Table of contents:
- [post](#post)

- [json file](./_api_tasks_stop_{task_id}.json)

---
<a name="post"></a>
## post

**summary:** Stop Task Endpoint

**operationId:** stop_task_endpoint_api_tasks_stop__task_id__post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'task_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Task Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

