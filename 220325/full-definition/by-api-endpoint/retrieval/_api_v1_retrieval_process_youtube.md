# /api/v1/retrieval/process/youtube

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['retrieval']

**summary:** Process Youtube Video

**operationId:** process_youtube_video_api_v1_retrieval_process_youtube_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ProcessUrlForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

