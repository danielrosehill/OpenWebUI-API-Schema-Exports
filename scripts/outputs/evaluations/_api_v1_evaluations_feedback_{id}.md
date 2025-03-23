# /api/v1/evaluations/feedback/{id}

## Table of contents:
- [get](#get)

- [post](#post)

- [delete](#delete)

- [json file](./_api_v1_evaluations_feedback_{id}.json)

---
<a name="get"></a>
## get

**tags:** ['evaluations']

**summary:** Get Feedback By Id

**operationId:** get_feedback_by_id_api_v1_evaluations_feedback__id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FeedbackModel'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

<a name="post"></a>
## post

**tags:** ['evaluations']

**summary:** Update Feedback By Id

**operationId:** update_feedback_by_id_api_v1_evaluations_feedback__id__post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FeedbackForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FeedbackModel'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

<a name="delete"></a>
## delete

**tags:** ['evaluations']

**summary:** Delete Feedback By Id

**operationId:** delete_feedback_by_id_api_v1_evaluations_feedback__id__delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

