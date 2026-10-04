# Git Cheatsheet

## Core Commands

```bash
git status
git add .
git commit -m "feat: add project structure"
git push origin main
git pull --rebase origin main
git checkout -b feature/my-branch
```

## Useful Branch Workflow

```bash
git checkout main
git pull origin main
git checkout -b feature/fastapi-service
git add .
git commit -m "feat(api): add FastAPI service"
git push -u origin feature/fastapi-service
```

## Undo / Recovery

```bash
git restore --staged file.txt
git restore file.txt
git log --oneline --decorate --graph
git revert <commit_hash>
```

## Best Practices

- Commit small, logical units
- Write clear commit messages
- Keep branches short-lived
- Review diff before pushing
