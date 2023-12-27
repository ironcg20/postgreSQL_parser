import re


def parseQuery(query):
    query_id_pattern = r'query_id: (\S+)'
    sql_text_pattern = r'sql_text: (.+?)query_type:'
    database_name_pattern = r'database_name: (\w+)'
    schema_name_pattern = r'schema_name: (\w+)'

    query_id_match = re.search(query_id_pattern, query)
    sql_text_match = re.search(sql_text_pattern, query, re.DOTALL)
    database_name_match = re.search(database_name_pattern, query)
    schema_name_match = re.search(schema_name_pattern, query)

    if query_id_match:
        query_id = query_id_match.group(1)
        # print(f"Query ID: {query_id}")

    if sql_text_match:
        sql_text = sql_text_match.group(1).strip()
        print(f"SQL Text:\n{sql_text}")
    else:
        print("SQL text not found.")

    if database_name_match:
        database_name = database_name_match.group(1)
        # print(f"Database Name: {database_name}")

    if schema_name_match:
        schema_name = schema_name_match.group(1)
        # print(f"Schema Name: {schema_name}")


if __name__ == "__main__":
    with open("query.txt", 'r') as file:
        query = file.read()
    parseQuery(query)
