import json
from contextlib import contextmanager
import psycopg
from psycopg.rows import dict_row
from app.config import setting

def connection():
    # Render PostgreSQL External Database URL for a FastAPI process running on your computer
    url = setting().database_url
    if not url:
        raise RuntimeError("DATABASE_URL is not set in the environment variables.")

    with psycopg.connect(url, row_factory=dict_row, connection_timeout=10) as conn:
        yield conn
        
def audit(conn, actor, tenant, action, detail):
    conn.execute('INSERT into audit_events (actor, tenant_id, action, details) VALUES(%s, %s, %s, %s)', 
                 (actor, tenant, action, json.dumps(detail)))
    
