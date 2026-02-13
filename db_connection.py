"""Shared PostgreSQL connection utilities."""

from imports import POSTGRESQL_DATABASE_NAME, POSTGRESQL_HOSTNAME, POSTGRESQL_PASSWORD, POSTGRESQL_PORT, POSTGRESQL_USERNAME, psycopg2

_connection = None


def get_shared_db_connection():
    """Return a single PostgreSQL connection for the current process."""
    global _connection
    if _connection is None or _connection.closed != 0:
        _connection = psycopg2.connect(
            database=POSTGRESQL_DATABASE_NAME,
            host=POSTGRESQL_HOSTNAME,
            port=POSTGRESQL_PORT,
            user=POSTGRESQL_USERNAME,
            password=POSTGRESQL_PASSWORD,
        )
        _connection.autocommit = True
    return _connection


def get_shared_db_cursor():
    """Return a fresh cursor from the shared PostgreSQL connection."""
    return get_shared_db_connection().cursor()
