# /openai/verify

## Table of contents:
- [post](#post)

- [json file](./_openai_verify.json)

---
<a name="post"></a>
## post

**tags:** ['openai']

**summary:** Verify Connection

**operationId:** verify_connection_openai_verify_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/open_webui__routers__openai__ConnectionVerificationForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

