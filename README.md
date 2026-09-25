# Users API ETL Pipeline

## What I did
Built a complete ETL pipeline to extract user data from REST API and load into SQLite.

## Flow
API -> Pandas (json_normalize) -> SQLite -> SQL Query

## Steps
1. **Extract:** GET https://jsonplaceholder.typicode.com/users
2. **Transform:** Flattened nested JSON (address, company) using `pd.json_normalize()`
3. **Load:** Loaded clean data into `users.db`
4. **Query:** Found users living in cities starting with 'S'

5. 
## Tech Used
- Python
- Requests
- Pandas
- SQLite

## How to Run
```bash
python users_etl_pipeline.py
```
