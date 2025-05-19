from sqlalchemy import create_engine, MetaData, Table, select, insert, delete

engine = create_engine("mysql+pymysql://root:Klodeckel@localhost/Treffpunkt_DB")

metadata = MetaData()
metadata.reflect(bind = engine)
users = metadata.tables["user"]

def getDataFromTable(table_name, attributes = None):
    table = metadata.tables[str(table_name)]
    data = []
    if attributes:
            stmt = select(*[table.c[attribute] for attribute in attributes])
            result = engine.connect().execute(stmt)
            for row in result:
                data.append(row)
                
    return data

def writeDataToTable(table_name, attributes = None, data = None):
    table = metadata.tables[str(table_name)]
    if attributes and data:
        data_dict = dict(zip(attributes, data))
        stmt = insert(table).values(data_dict)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
            
def deleteFromTable(table_name, id_name, to_delete = None):
    table = metadata.tables[str(table_name)]
    if to_delete:
        stmt = delete(table).where(table.c[str(id_name)] == str(to_delete)) 
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        

        
    
       
writeDataToTable("gender",["GENDER_ID", "GENDER_NAME"],["4","based"])
print(getDataFromTable("gender", ["GENDER_ID", "GENDER_NAME"]))
deleteFromTable("gender", "GENDER_ID", "4")
print(getDataFromTable("gender", ["GENDER_ID", "GENDER_NAME"]))

    
