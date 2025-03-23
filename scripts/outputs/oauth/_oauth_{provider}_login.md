# /oauth/{provider}/login

## Table of contents:
- [get](#get)

- [json file](./_oauth_{provider}_login.json)

---
<a name="get"></a>
## get

**summary:** Oauth Login

**operationId:** oauth_login_oauth__provider__login_get

**parameters:** [{'name': 'provider', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Provider'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

