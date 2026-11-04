<!-- EnterpriseAI — Step-by-Step Implementation Order -->

1 — Setup and infrastructure
requirements.txt — Define dependencies for FastAPI, LangGraph, boto3, Pinecone, PostgreSQL, and Rius instrumentation.
.env.example → .env — Configure AWS credentials, Bedrock models, S3 bucket, Pinecone, Render PostgreSQL, and Rius settings. Never commit .env.
app/config.py — Centralize environment-variable loading and application configuration.
infra/schema.sql — Define database tables for documents, chat history, HITL approvals, feedback, and audit events.
app/db.py — Configure PostgreSQL connections and database helpers.
scripts/init_db.py — Create and verify the database schema.
app/aws.py — Configure AWS clients, S3 operations, Bedrock Nova Lite chat, and Titan V2 embeddings.