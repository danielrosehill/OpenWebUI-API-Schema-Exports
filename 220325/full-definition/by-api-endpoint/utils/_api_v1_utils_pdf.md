# /api/v1/utils/pdf

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['utils']

**summary:** Download Chat As Pdf

**operationId:** download_chat_as_pdf_api_v1_utils_pdf_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ChatTitleMessagesForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

