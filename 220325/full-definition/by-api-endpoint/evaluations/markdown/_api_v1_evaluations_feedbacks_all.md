# /api/v1/evaluations/feedbacks/all

## Table of contents:
- [get](#get)
- [delete](#delete)

<a name="get" />
## get

**tags:** ['evaluations']

**summary:** Get All Feedbacks

**operationId:** get_all_feedbacks_api_v1_evaluations_feedbacks_all_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'items': {'$ref': '#/components/schemas/FeedbackUserResponse'}, 'type': 'array', 'title': 'Response Get All Feedbacks Api V1 Evaluations Feedbacks All Get'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="delete" />
## delete

**tags:** ['evaluations']

**summary:** Delete All Feedbacks

**operationId:** delete_all_feedbacks_api_v1_evaluations_feedbacks_all_delete

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}}

**security:** [{'HTTPBearer': []}]

