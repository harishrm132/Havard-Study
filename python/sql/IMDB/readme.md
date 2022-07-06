```sql
SELECT id FROM people WHERE @name = "Steve Carell";
SELECT show_id FROM stars WHERE person_id = (SELECT id FROM People WHERE name = "Steve Carell");
```

## Injection Attack
## Race Conditions
## Transactions
    -   Begin Transaction
    -   Commit
    -   Rollback