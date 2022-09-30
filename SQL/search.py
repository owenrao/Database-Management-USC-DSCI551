import sqlalchemy
import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd

my_conn = sqlalchemy.create_engine("mysql+mysqldb://dsci551:Dsci-551@localhost/sakila")

def main(name_list):
    name_list = ["'"+name.strip("'")+"'" for name in name_list]
    #print(name_list)
    condition = " OR ".join([f"first_name={name}" for name in name_list])
    query = f"SELECT C_A.first_name,C_A.last_name,A_CT.city FROM (SELECT first_name,last_name, address_id FROM customer WHERE {condition}) AS C_A INNER JOIN (SELECT address.address_id,city.city FROM address JOIN city ON address.city_id=city.city_id) AS A_CT ON C_A.address_id=A_CT.address_id;"
    df = pd.read_sql(query, my_conn)
    if df.empty:
        output = "Customer does not exist"
    else:
        output = df.to_string(index=False, header=False).upper()
    print(output)
    return output

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])