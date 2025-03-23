# /api/v1/audio/config/update

## Table of contents:
- [post](#post)

- [json file](./_api_v1_audio_config_update.json)

---
<a name="post"></a>
## post

**tags:** ['audio']

**summary:** Update Audio Config

**operationId:** update_audio_config_api_v1_audio_config_update_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/AudioConfigUpdateForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

