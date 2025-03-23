# /ollama/api/embeddings/{url_idx}

## Table of contents:
- [post](#post)

- [json file](./_ollama_api_embeddings_{url_idx}.json)

---
<a name="post"></a>
## post

**tags:** ['ollama']

**summary:** Embeddings

**operationId:** embeddings_ollama_api_embeddings__url_idx__post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'url_idx', 'in': 'path', 'required': True, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Url Idx'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/GenerateEmbeddingsForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

