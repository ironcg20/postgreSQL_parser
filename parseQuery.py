import re

def parseQuery(query):
    query_id_pattern = r'query_id: (\S+)'
    query_id_match = re.search(query_id_pattern, query)

    if query_id_match and sql_text_match:
    print(query_id_pattern)


if __name__ == "__main__":
    with open("query.txt", 'r') as file:
        query=file.read()
    parseQuery(query)