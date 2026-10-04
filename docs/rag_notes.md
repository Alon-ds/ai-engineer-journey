# RAG Notes

## Retrieval-Augmented Generation

RAG combines:

- a retriever
- a vector store
- an LLM

This allows the model to answer based on relevant documents rather than only its training data.

## Typical Flow

1. Chunk documents
2. Generate embeddings
3. Store embeddings in a vector DB
4. Query vector store for relevant context
5. Send retrieved context + prompt to the LLM
6. Return grounded response

## Key Considerations

- Chunk size matters
- Metadata improves retrieval
- Re-rankers can improve quality
- Evaluate with grounded answers and retrieval metrics
