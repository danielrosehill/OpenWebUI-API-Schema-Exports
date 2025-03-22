# /api/v1/auths/ldap

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['auths']

**summary:** Ldap Auth

**operationId:** ldap_auth_api_v1_auths_ldap_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/LdapForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/SessionUserResponse'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

