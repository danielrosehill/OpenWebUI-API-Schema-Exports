# /api/v1/configs/banners

## Table of contents:
- [get](#get)

- [post](#post)

- [json file](./_api_v1_configs_banners.json)

---
<a name="get"></a>
## get

**tags:** ['configs']

**summary:** Get Banners

**operationId:** get_banners_api_v1_configs_banners_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'items': {'$ref': '#/components/schemas/BannerModel'}, 'type': 'array', 'title': 'Response Get Banners Api V1 Configs Banners Get'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post"></a>
## post

**tags:** ['configs']

**summary:** Set Banners

**operationId:** set_banners_api_v1_configs_banners_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/SetBannersForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'items': {'$ref': '#/components/schemas/BannerModel'}, 'type': 'array', 'title': 'Response Set Banners Api V1 Configs Banners Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

