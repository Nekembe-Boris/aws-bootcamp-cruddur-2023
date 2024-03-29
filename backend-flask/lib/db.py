from psycopg_pool import ConnectionPool
import os


class Db:
  def __init__(self):
    self.init_pool()

  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)

  def query_commit_with_returning_id(self, sql, *args)
    try:
      conn = self.pool.connection()
      cur = conn.cursor()
      cur.execute(sql)
      returning_id = cur.fetchone()[0]
      conn.commit()
      return returning_id
    except Exception as error:
      conn.rollback()

  def query_commit(self, sql)
    try:
      conn = self.pool.connection()
      cur = conn.cursor()
      cur.execute(sql)
      conn.commit()
    except Exception as error:
      conn.rollback()
  
  def query_wrap_object(self, template):
  sql = f"""  
  (SELECT COALESCE(row_to_json(object_row),'{ {}}'::json) FROM (
  {template}
  ) object_row);"""

  return sql

  def query_wrap_array(self, template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql


  def query_array_json(self, sql):
    wrapped_sql = self.query_wrap_array(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
        return json[0]    


  def query_object_josn(self, sql):
    wrapped_sql = self.query_wrap_object(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
        return json[0]


db = Db()