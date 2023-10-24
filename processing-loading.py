# file_processing.py

file_path = "/app/sample_file.txt" # Change file path to match your file path
global cnt
cnt = False
def parse_line(line):
    # Split the line into road_id, Direction, and polyline
    parts = line.strip().split(' ')
    road_id = parts[0]
    direction = int(parts[1])
    polyline = parts[2:]
    return road_id, direction, polyline

def read_file(filename):
    data = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            road_id, direction, polyline = parse_line(line)
            data.append((road_id, direction, polyline))
    push_data(data)
    return data

# database_push.py
import psycopg2
def create_table():
    conn = psycopg2.connect(
        dbname="roadlinks-db",
        user="postgres",
        password="postgres",
        host="postgres",
        port="5432"
    )
    
    cur = conn.cursor()
    table_creation = '''
        CREATE TABLE road_links (
            road_id VARCHAR(50),
            direction INT,
            polyline TEXT[]
        );
    '''
    cur.execute(table_creation)
    conn.commit()
    cur.close
    conn.close()
def push_data(data):
    conn = psycopg2.connect(
        dbname="roadlinks-db",
        user="postgres",
        password="postgres",
        host="postgres",
        #POSTGRES_MASTER_HOST
        port="5432"
    )
    
    cur = conn.cursor()


    # Check if the table exists
    cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'road_links')")
    table_exists = cur.fetchone()[0]
    print(table_exists)
    # If the table doesn't exist, create it
    if not table_exists:
        cur.execute("CREATE TABLE road_links (road_id VARCHAR(50), direction INT, polyline TEXT[])")
        cnt=True
    # Insert data into the table
    for row in data:
        cur.execute("INSERT INTO road_links (road_id, direction, polyline) VALUES (%s, %s, %s)", row)
        print("INSERT INTO roadlinks (road_id, direction, polyline) VALUES (%s, %s, %s)", row)
    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

if __name__ == '__main__':
    #create_table()
    read_file(file_path)
