# /oauth/{provider}/callback

## Table of contents:
- [get](#get)

- [json file](./_oauth_{provider}_callback.json)

---
<a name="get"></a>
## get

**summary:** Oauth Callback

**operationId:** oauth_callback_oauth__provider__callback_get

**parameters:** [{'name': 'provider', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Provider'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

