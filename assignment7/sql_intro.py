import sqlite3

try:
    # Task 1: Create a New SQLite Database
    with sqlite3.connect("../db/magazines.db") as conn:
        # Turn on the foreign key restraint
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        print("Database is connected.")
except sqlite3.Error as e:
    print(f"Database was not made successfully: {e}")

#Task 2: Define Database Structure

try:
    #Create the Publishers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY, 
        publisher_name TEXT UNIQUE NOT NULL
        );
    ''')

    #Create the Magazines table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY, 
            magazine_name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        );
    ''')

    #Create the Subscribers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            subscriber_name TEXT NOT NULL,
            subscriber_address TEXT NOT NULL
        );
    ''')

    #Create the Subscriptions table (Join table)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
        );
    ''')

    print("Tables have been created successfully.")
   
    # ---- Insert Functions with len(results) checks ----

    def add_publisher(cursor, name):
        cursor.execute("SELECT * FROM publishers WHERE publisher_name = ?", (name,))
        results = cursor.fetchall()
        #Use len to prevent repeat entries
        if len(results) > 0:
            print(f"Publisher '{name}' already exists.")
            return
        try:
            cursor.execute("INSERT INTO publishers (publisher_name) VALUES (?)", (name,))
            print(f"Publisher '{name}' added.")
        except sqlite3.IntegrityError as e:
            print(f"Failed to add publisher '{name}': {e}")

    def add_magazine(cursor, name, pub_id):
        cursor.execute("SELECT * FROM magazines WHERE magazine_name = ?", (name,))
        results = cursor.fetchall()
        #Use len to prevent repeat entries
        if len(results) > 0:
            print(f"Magazine '{name}' already exists.")
            return
        try:
            cursor.execute(
                "INSERT INTO magazines (magazine_name, publisher_id) VALUES (?, ?)",
                (name, pub_id)
            )
            print(f"Magazine '{name}' added.")
        except sqlite3.IntegrityError as e:
            print(f"Failed to add magazine '{name}': {e}")

    def add_subscriber(cursor, name, address):
        cursor.execute(
            "SELECT * FROM subscribers WHERE subscriber_name = ? AND subscriber_address = ?",
            (name, address)
        )
        results = cursor.fetchall()
        #Use len to prevent repeat entries
        if len(results) > 0:
            print(f"Subscriber '{name} at {address}' already exists.")
            return
        try:
            cursor.execute(
                "INSERT INTO subscribers (subscriber_name, subscriber_address) VALUES (?, ?)",
                (name, address)
            )
            print(f"Subscriber '{name} at {address}' added.")
        except sqlite3.IntegrityError as e:
            print(f"Failed to add subscriber '{name} at {address}': {e}")

    def add_subscription(cursor, sub_id, mag_id, exp_date):
        cursor.execute(
            "SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
            (sub_id, mag_id)
        )
        results = cursor.fetchall()
        #Use len to prevent repeat entries
        if len(results) > 0:
            print(f"Subscription (subscriber {sub_id}, magazine {mag_id}) already exists.")
            return
        try:
            cursor.execute(
                "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                (sub_id, mag_id, exp_date)
            )
            print(f"Subscription (subscriber {sub_id}, magazine {mag_id}) added.")
        except sqlite3.IntegrityError as e:
            print(f"Failed to add subscription: {e}")

    #Sample Data
    #Adding publishers
    add_publisher(cursor, "The Publisher that makes AARP")
    add_publisher(cursor, "IDK if Time is a Publisher")
    add_publisher(cursor, "Cool Guy")

    #Adding magazines
    add_magazine(cursor, "AARP", 1)
    add_magazine(cursor, "Time", 2)
    add_magazine(cursor, "The Bestest Magazine Ever in the Universe", 3)

    #Adding subscribers
    add_subscriber(cursor, "Jimmy", "90210 Beverly Dr.")
    add_subscriber(cursor, "Snoopy", "321 Red Baron Ave.")
    add_subscriber(cursor, "Mork", "0009 Ork Wy.")
    add_subscriber(cursor, "Jimmy", "314 Neutron St.")

    #Adding subscriptions
    add_subscription(cursor, 1, 1, "2025-12-31")
    add_subscription(cursor, 2, 2, "2025-12-25")
    add_subscription(cursor, 3, 3, "2025-09-09")
    add_subscription(cursor, 4, 3, "2025-05-15")

    #Commit to not lose the information
    conn.commit()
    print("Sample data inserted successfully.")

    #Task 4: Write SQL Queries
    #Write a query to retrieve all information from the subscribers table
    print("\nAll Subscribers:")
    cursor.execute("SELECT * FROM subscribers;")
    for row in cursor.fetchall():
        print(row)

    #Write a query to retrieve all magazines sorted by name
    print("\nAll Magazines (sorted alphabetically):")
    cursor.execute("SELECT * FROM magazines ORDER BY magazine_name;")
    for row in cursor.fetchall():
        print(row)

    #Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN
    lookup_publisher = "Cool Guy"
    print(f"\nMagazines published by {lookup_publisher}:")
    cursor.execute("""
        SELECT m.*
        FROM magazines AS m
        JOIN publishers AS p
          ON m.publisher_id = p.publisher_id
        WHERE p.publisher_name = ?
    """, (lookup_publisher,))
    for row in cursor.fetchall():
        print(row)
        
except sqlite3.Error as e:
    print(f"Tables were not created successfully: {e}")
