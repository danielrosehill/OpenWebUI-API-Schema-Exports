# /api/v1/utils/markdown

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['utils']

**summary:** Get Html From Markdown

**operationId:** get_html_from_markdown_api_v1_utils_markdown_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/MarkdownForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

