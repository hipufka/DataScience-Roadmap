import yaml
import pandas as pd

CH_CONFIG_PATH = 'config.txt' # local path to ClickHouse DB credentials

client = Client(
  **yaml.load(
    open(CH_CONFIG_PATH, 'r'), 
    Loader=yaml.SafeLoader
  )['database']
)

# load data from Clickhouse table to pandas dataframe
threshold_date = '2008-01-01'

main_table = client.query_dataframe("""select *
                                    from schema.table as c 
                                    where c.user_id is not null 
                                        and toDate(c.updated_date) <= '{}'
                                        """
                                     .format(threshold_date))
                                     
                                     
"""YAML file example
database:
  user: python
  password: secret
  schema: marketing
  host: 111.111.111.1
  port: 1111
 """
