# /api/v1/users/user/settings

## Table of contents:
- [get](#get)

- [json file](./_api_v1_users_user_settings.json)

---
<a name="get"></a>
## get

**tags:** ['users']

**summary:** Get User Settings By Session User

**operationId:** get_user_settings_by_session_user_api_v1_users_user_settings_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/UserSettings'}, {'type': 'null'}], 'title': 'Response Get User Settings By Session User Api V1 Users User Settings Get'}}}}}

**security:** [{'HTTPBearer': []}]

