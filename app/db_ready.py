from pandas import DataFrame, read_csv
import uuid

# Reads the contents of the csv, changes it to SQLAlchemy readable format, adds UUID for every passenger, sends it off as SQL

# Transforms integer 1/0 to True/False, a format that SQLAlchemy understands
def sqla_readable(raw):

    df = DataFrame(raw)

    df['Survived'] = df['Survived'].replace([0,1], [False , True])

    return df

# Inserts a UUID made from the name of every passenger
def add_uuid(data_frame):

    df = data_frame   

    names = df['Name'].tolist()
    uuid_list = []

    for name in names:
        uuid_list.append(str(uuid.uuid5(uuid.NAMESPACE_DNS, name)))

    df.insert(0, 'uuid', uuid_list)
    return df


def make_db_ready(file_name, con, db_table, if_exists):
    
    data = read_csv(file_name)
    
    readable_data = sqla_readable(data)
    sensible_data = add_uuid(readable_data)

    sensible_data.rename(columns={'Survived':'survived', 'Pclass':'passengerClass', 'Name':'name', 'Sex':'sex', 'Age':'age', 'Siblings/Spouses Aboard':'siblingsOrSpousesAboard', 'Parents/Children Aboard':'parentsOrChildrenAboard', 'Fare':'fare'}, inplace=True)
    ready_csv_to_db = sensible_data.to_sql(con=con, name=db_table, if_exists=if_exists)
    
    return ready_csv_to_db
