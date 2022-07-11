import vertica_python
import pandas.io.sql as psql
import yaml

VERTICA_CONFIG_PATH = 'config.txt' # local path to Vertica DB credentials

conn_info = yaml.load(
    open(VERTICA_CONFIG_PATH, 'r'), 
    Loader=yaml.SafeLoader)
    
sql = """select * from table1"""

# using `with` for auto connection closing after usage
with vertica_python.connect(**conn_info) as connection:
    cur = connection.cursor()    
    df = psql.read_sql(sql, connection)
