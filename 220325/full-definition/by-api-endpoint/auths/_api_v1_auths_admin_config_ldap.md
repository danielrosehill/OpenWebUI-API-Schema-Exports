# /api/v1/auths/admin/config/ldap

## Table of contents:
- [get](#get)
- [post](#post)

<a name="get" />
## get

**tags:** ['auths']

**summary:** Get Ldap Config

**operationId:** get_ldap_config_api_v1_auths_admin_config_ldap_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post" />
## post

**tags:** ['auths']

**summary:** Update Ldap Config

**operationId:** update_ldap_config_api_v1_auths_admin_config_ldap_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/LdapConfigForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

