# /api/v1/tasks/queries/completions

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['tasks']

**summary:** Generate Queries

**operationId:** generate_queries_api_v1_tasks_queries_completions_post

**requestBody:** {'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

