

from Db.connection import Conn
from sqlalchemy.engine.row import Row
from sqlalchemy.engine.base import Connection
from sqlalchemy.engine.cursor import LegacyCursorResult


class Methods:

    def create(stmt, params=None) -> int:
        with Conn.conn() as conn:
            result: LegacyCursorResult
            result = conn.execute(stmt)
            return result.lastrowid

    def get(stmt, param=None) -> list:
        with Conn.conn() as conn:
            conn: Connection
            executeconn: LegacyCursorResult = conn.execute(stmt)
            result = executeconn.fetchall()
            nresult = []
            for data in result:
                data: Row
                nresult.append(data._asdict())
            return nresult

    def update(stmt, params=None) -> None:
        with Conn.conn() as conn:
            conn.execute(stmt)
