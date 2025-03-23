# /ollama/api/embeddings

## Table of contents:
- [post](#post)

- [json file](./_ollama_api_embeddings.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Embeddings

**operationId:** embeddings_ollama_api_embeddings_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/GenerateEmbeddingsForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

