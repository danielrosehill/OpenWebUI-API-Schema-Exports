# /api/webhook

## Table of contents:
- [get](#get)

- [post](#post)

- [json file](./_api_webhook.json)

---
<a name="get"></a>
## get

**summary:** Get Webhook Url

**operationId:** get_webhook_url_api_webhook_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post"></a>
## post

**summary:** Update Webhook Url

**operationId:** update_webhook_url_api_webhook_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/UrlForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

