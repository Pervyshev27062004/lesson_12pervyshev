from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

DB_PATH = Path(__file__).resolve().parent / "my_database.sqlite3"
DB_ECHO = True


engine = create_engine(f"sqlite:////{DB_PATH}", echo=DB_ECHO)
if not database_exists(engine.url):
    create_database(engine.url)
