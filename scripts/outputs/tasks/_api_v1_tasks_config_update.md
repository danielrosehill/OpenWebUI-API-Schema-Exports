# /api/v1/tasks/config/update

## Table of contents:
- [post](#post)

- [json file](./_api_v1_tasks_config_update.json)

---
<a name="post"></a>
## post

**tags:** ['tasks']

**summary:** Update Task Config

**operationId:** update_task_config_api_v1_tasks_config_update_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/TaskConfigForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

