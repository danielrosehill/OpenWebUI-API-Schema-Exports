# /api/v1/tools/create

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['tools']

**summary:** Create New Tools

**operationId:** create_new_tools_api_v1_tools_create_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ToolForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ToolResponse'}, {'type': 'null'}], 'title': 'Response Create New Tools Api V1 Tools Create Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

