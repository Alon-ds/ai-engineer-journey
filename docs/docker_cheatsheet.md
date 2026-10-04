# Docker Cheatsheet

## Common Commands

```bash
docker build -t myapp .
docker run -p 8000:8000 myapp
docker ps
docker logs <container_id>
docker compose up --build
docker compose down
```

## Useful Concepts

- `Dockerfile`: defines image build instructions
- `docker-compose.yml`: defines multi-container services
- Volumes persist state between runs
- Networks connect services together

## Best Practices

- Keep images lightweight
- Use `.dockerignore`
- Separate app and database services
- Prefer explicit version tags
