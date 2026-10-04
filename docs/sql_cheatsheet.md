# SQL Cheatsheet

## Core Concepts

- `SELECT` retrieves data
- `WHERE` filters rows
- `GROUP BY` groups rows for aggregation
- `JOIN` combines tables
- `ORDER BY` sorts results
- `LIMIT` restricts rows

## Example

```sql
SELECT customers.name, COUNT(orders.id) AS order_count
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
WHERE customers.active = true
GROUP BY customers.name
ORDER BY order_count DESC
LIMIT 10;
```

## Common Data Types

- `INT`, `BIGINT`
- `VARCHAR`, `TEXT`
- `BOOLEAN`
- `DATE`, `TIMESTAMP`
- `DECIMAL`

## Normalization Tips

- Reduce duplication
- Use foreign keys
- Keep logical grouping clear
- Use indexes for performance

## Query Optimization

- Use `EXPLAIN ANALYZE`
- Add indexes on frequent filters
- Avoid `SELECT *` in production queries
- Normalize large datasets carefully
