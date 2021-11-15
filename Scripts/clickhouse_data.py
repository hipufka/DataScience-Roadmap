import pandas
from clickhouse_driver import Client

client = Client(
                user='<username>',
                password='<password>',
                database='<db>',
                host='<ip>',
                port='<port>'
            )
            
 df = client.query_dataframe("""select *
                            from <scheme>.<table> 
                            limit 10""")
