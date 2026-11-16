# Flask Docker `.env` Project

## Project Structure
- `app.py` – Flask app loading `JWT_SECRET` and `DATABASE_URL` via `os.getenv()`.
- `Dockerfile` – Builds the Python container without hardcoding secrets.
- `docker-compose.yml` – Injects `.env` values into the container using `env_file:`.
- `.env` – Stores your environment variables locally.
- `.gitignore` – Prevents `.env` from being committed to Git.

## How to Run
1. Extract this ZIP archive and open a terminal inside the folder.
2. Run:
   ```bash
   docker-compose up --build
   ```
3. Open `http://localhost:5000` in your browser to verify both variables loaded properly.
