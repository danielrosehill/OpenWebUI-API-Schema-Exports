# /api/v1/images/generations

## Table of contents:
- [post](#post)

- [json file](./_api_v1_images_generations.json)

---
<a name="post"></a>
## post

**tags:** ['images']

**summary:** Image Generations

**operationId:** image_generations_api_v1_images_generations_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/GenerateImageForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

