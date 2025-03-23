# /api/v1/evaluations/feedback

## Table of contents:
- [post](#post)

- [json file](./_api_v1_evaluations_feedback.json)

---
<a name="post"></a>
## post

**tags:** ['evaluations']

**summary:** Create Feedback

**operationId:** create_feedback_api_v1_evaluations_feedback_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FeedbackForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FeedbackModel'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

