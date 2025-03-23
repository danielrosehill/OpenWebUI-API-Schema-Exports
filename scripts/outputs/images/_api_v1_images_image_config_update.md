# /api/v1/images/image/config/update

## Table of contents:
- [post](#post)

- [json file](./_api_v1_images_image_config_update.json)

---
<a name="post"></a>
## post

**tags:** ['images']

**summary:** Update Image Config

**operationId:** update_image_config_api_v1_images_image_config_update_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ImageConfigForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

