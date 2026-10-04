# FastAPI Notes

## Why FastAPI?

FastAPI is excellent for:

- REST APIs
- Type-safe request validation
- Automatic schema generation
- Async support
- Fast development

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}
```

## Good Practices

- Use Pydantic models for validation
- Keep endpoints small and focused
- Add tests for business logic
- Use dependency injection
- Structure services clearly
