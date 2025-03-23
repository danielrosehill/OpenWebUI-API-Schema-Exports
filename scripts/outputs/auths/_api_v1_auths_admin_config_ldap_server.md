# /api/v1/auths/admin/config/ldap/server

## Table of contents:
- [get](#get)

- [post](#post)

- [json file](./_api_v1_auths_admin_config_ldap_server.json)

---
<a name="get"></a>
## get

**tags:** ['auths']

**summary:** Get Ldap Server

**operationId:** get_ldap_server_api_v1_auths_admin_config_ldap_server_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/LdapServerConfig'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post"></a>
## post

**tags:** ['auths']

**summary:** Update Ldap Server

**operationId:** update_ldap_server_api_v1_auths_admin_config_ldap_server_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/LdapServerConfig'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

