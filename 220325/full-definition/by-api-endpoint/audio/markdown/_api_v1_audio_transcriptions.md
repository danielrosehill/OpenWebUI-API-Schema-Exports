# /api/v1/audio/transcriptions

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['audio']

**summary:** Transcription

**operationId:** transcription_api_v1_audio_transcriptions_post

**requestBody:** {'content': {'multipart/form-data': {'schema': {'$ref': '#/components/schemas/Body_transcription_api_v1_audio_transcriptions_post'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

