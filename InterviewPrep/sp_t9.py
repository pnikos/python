import re

line="2026-10-04T10:15:23Z DB_QUERY name=GetCustomer db=customer duration=183 rows=42"

def is_db_query(line):
	return bool(re.search("DB_QUERY", line))

def get_first_number(line):
	match = re.search(r"\d+", line)

	return int(match.group())

def get_query_name(line):
	match = re.search(r"name=(\w+)", line)

	if match:
		return match.group(1)
	else:
		return None

def extract_db_query_fields(line):
	pattern = (
		r"name=(?P<query_name>\w+) "
		r"db=(?P<database>\w+) "
		r"duration=(?P<duration>\d+) "
		r"rows=(?P<rows>\d+)"
	)
	match = re.search(pattern, line)

	row = {
		"query_name": match.group("query_name"),
		"database": match.group("database"),
		"duration": int(match.group("duration")),
		"rows": int(match.group("rows"))
	}

	return row

print(extract_db_query_fields(line))
print("="*40)

def extract_field_alt(line, field):
	match = re.search(r""+field+"=(?P<field>\S+) ",line)
	
	if match:
		return match.group(1) 
	else:
		return None

def extract_field(line, field):
	match = re.search(rf"{field}=(\S+)",line)
	
	if match:
		return match.group(1) 
	else:
		return None

print(extract_field(line, "duration"))

def extract_db_query_fields_new(line):
	row = {
		"query_name": extract_field(line, "name"),
		"database": extract_field(line, "db"),
		"duration": int(extract_field(line, "duration")),
		"rows": int(extract_field(line, "rows"))
	}
	return row

print(extract_db_query_fields_new(line))
print("-"*50)

def parse_db_query(line):

	match = re.search(r"\bDB_QUERY\b", line)
	if not match:
		return "Not a DB QUERY"

	query_name = extract_field(line, "name")
	if not query_name:
		return None

	database = extract_field(line, "db")
	if not database:
		return None

	try:
		duration = int(extract_field(line, "duration"))
	except (TypeError, ValueError):
		return None

	try:
		rows = int(extract_field(line, "rows"))
	except (TypeError, ValueError):
		return None

	query = {
		"query_name": query_name,
		"database": database,
		"duration": duration,
		"rows": rows
	}
	return query

print(
parse_db_query(
    "DB_QUERY name=BrokenQuery db=customer duration=abc rows=12"
)
)
print("-"*40)


def parse_key_values(line):
	pairs = re.findall(r"(\w+)=(\S+)", line)
	data = dict(pairs)

	return data

print(parse_key_values("name=GetCustomer db=customer duration=183 rows=42"))