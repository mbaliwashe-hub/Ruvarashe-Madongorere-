def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

while True:
    user_input = input("Enter an integer: ")
    try:
        num = int(user_input)
        result = classify_number(num)
        print("The number is:", result)
        break  # Exit the loop after a valid input
    except ValueError:
        print("Invalid input. Please enter a valid integer.")





        def calculate_average(*args):
            """
            Calculates the average of any number of numeric inputs.

            Parameters:
                *args: A variable number of numeric arguments.

            Returns:
                The average of the input numbers as a float.
                Returns 0 if no numbers are provided.
            """
            if len(args) == 0:
                return 0
            total = sum(args)
            count = len(args)
            average = total / count
            return average

        print(calculate_average(10, 20, 30))  # Output: 20.0
        print(calculate_average(5, 15))  # Output: 10.0
        print(calculate_average())  # Output:






        while True:
            try:
                number = int(input("Enter a number: "))
                print("You entered:", number)
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a valid number.")

                names = ["Alice", "Bob", "Charlie", "Diana"]

                with open("names.txt", "w") as file:
                    for name in names:
                        file.write(name + "\n")

                with open("names.txt", "r") as file:
                    for line in file:
                        print(line.strip())






                    celsius = [0, 10, 20, 30, 40]

                    fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))

                    print("Temperatures in Fahrenheit:", fahrenheit)






                    def divide_numbers(numerator, denominator):
                        try:
                            result = numerator / denominator
                            return result
                        except ZeroDivisionError:
                            print("Error: Cannot divide by zero.")
                        except TypeError:
                            print("Error: Invalid input type. Please use numbers only.")


                    print(divide_numbers(10, 2))  # Should return 5.0
                    print(divide_numbers(10, 0))  # Should print error
                    print(divide_numbers("10", 2))  # Should print error





                    class NegativeNumberError(Exception):
                        pass


                    def check_positive(number):
                        if number < 0:
                            raise NegativeNumberError("Negative number is not allowed.")
                        else:
                            print("Number is positive.")


                    try:
                        num = int(input("Enter a number: "))
                        check_positive(num)
                    except NegativeNumberError as e:
                        print("Error:", e)
                    except ValueError:
                        print("Invalid input. Please enter an integer.")







                        import random

                        numbers = [random.randint(1, 100) for _ in range(10)]

                        average = sum(numbers) / len(numbers)

                        print("Random numbers:", numbers)
                        print("Average:", average)





import re
from typing import List, Optional


def extract_emails(text: str) -> List[str]:

    # Email regex pattern - matches most common email formats
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails


def validate_date(date_string: str) -> bool:
    # Date pattern for YYYY-MM-DD format
    # This checks format but not if the date is actually valid (e.g., Feb 30th)
    date_pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
    return bool(re.match(date_pattern, date_string))


def replace_word(text: str, old_word: str, new_word: str) -> str:
    # Use word boundaries to match whole words only
    pattern = r'\b' + re.escape(old_word) + r'\b'
    return re.sub(pattern, new_word, text, flags=re.IGNORECASE)


def split_by_non_alphanumeric(text: str) -> List[str]:
    # Split by any non-alphanumeric character
    segments = re.split(r'[^A-Za-z0-9]+', text)
    # Filter out empty strings
    return [segment for segment in segments if segment]


def main():
    print("=" * 60)
    print("REGULAR EXPRESSIONS DEMONSTRATION")
    print("=" * 60)

    # I. Email Extraction
    print("\n1. EMAIL EXTRACTION:")
    print("-" * 30)
    sample_text = """
    Contact us at info@company.com or support@example.org.
    You can also reach John at john.doe123@gmail.com or
    the admin team at admin_team@test-domain.co.uk.
    Invalid emails like @invalid.com or missing@.com won't be matched.
    """

    emails = extract_emails(sample_text)
    print(f"Sample text:\n{sample_text}")
    print(f"Found emails: {emails}")
    print(f"Total emails found: {len(emails)}")

    # II. Date Validation
    print("\n2. DATE VALIDATION (YYYY-MM-DD):")
    print("-" * 35)
    test_dates = [
        "2023-12-25",  # Valid
        "2024-02-29",  # Valid format (leap year)
        "2023-13-01",  # Invalid month
        "2023-12-32",  # Invalid day
        "23-12-25",  # Invalid year format
        "2023/12/25",  # Wrong separator
        "2023-1-1",  # Missing leading zeros
        "2023-01-01"  # Valid
    ]

    for date in test_dates:
        is_valid = validate_date(date)
        status = "✓ VALID" if is_valid else "✗ INVALID"
        print(f"{date:<12} -> {status}")

    # III. Word Replacement
    print("\n3. WORD REPLACEMENT:")
    print("-" * 25)
    original_text = "The cat sat on the mat. The cat was happy because the cat found food."
    old_word = "cat"
    new_word = "dog"

    replaced_text = replace_word(original_text, old_word, new_word)
    print(f"Original text: {original_text}")
    print(f"Replace '{old_word}' with '{new_word}':")
    print(f"Result: {replaced_text}")

    # Test case sensitivity
    mixed_case_text = "The Cat and the cat and the CAT are all cats."
    replaced_mixed = replace_word(mixed_case_text, "cat", "dog")
    print(f"\nCase-insensitive replacement:")
    print(f"Original: {mixed_case_text}")
    print(f"Result: {replaced_mixed}")

    # IV. Split by Non-Alphanumeric
    print("\n4. SPLIT BY NON-ALPHANUMERIC CHARACTERS:")
    print("-" * 45)
    test_strings = [
        "hello,world!how@are#you$today?",
        "user123@domain.com",
        "price: $29.99 (tax included)",
        "file_name-v2.1.txt",
        "one::two;;three,,four!!five"
    ]

    for test_str in test_strings:
        segments = split_by_non_alphanumeric(test_str)
        print(f"'{test_str}'")
        print(f"  -> {segments}")
        print()


if __name__ == "__main__":
    main()







    import socket
    import threading
    import time
    import sys

    # Configuration
    HOST = 'localhost'  # Server host
    PORT = 12345  # Server port
    BUFFER_SIZE = 1024  # Buffer size for receiving data


    class SimpleServer:


        def __init__(self, host=HOST, port=PORT):
            self.host = host
            self.port = port
            self.server_socket = None
            self.running = False

        def start(self):

            try:
                # Create socket
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # Set socket options to reuse address
                self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

                # Bind socket to host and port
                self.server_socket.bind((self.host, self.port))

                # Listen for incoming connections (max 5 queued connections)
                self.server_socket.listen(5)
                self.running = True

                print(f"Server started on {self.host}:{self.port}")
                print("Waiting for client connections...")
                print("Press Ctrl+C to stop the server")

                while self.running:
                    try:
                        # Accept incoming connection
                        client_socket, client_address = self.server_socket.accept()
                        print(f"Connection established with {client_address}")

                        # Handle client in a separate thread
                        client_thread = threading.Thread(
                            target=self.handle_client,
                            args=(client_socket, client_address)
                        )
                        client_thread.daemon = True
                        client_thread.start()

                    except socket.error as e:
                        if self.running:  # Only print error if server is supposed to be running
                            print(f"Error accepting connection: {e}")
                        break

            except socket.error as e:
                print(f"Server error: {e}")
            except KeyboardInterrupt:
                print("\nServer shutdown requested by user")
            finally:
                self.stop()

        def handle_client(self, client_socket, client_address):

            try:
                # Send greeting message
                message = "Hello from server!"
                client_socket.send(message.encode('utf-8'))
                print(f"Message sent to {client_address}: '{message}'")

                # Keep connection open for a moment
                time.sleep(1)

            except socket.error as e:
                print(f"Error handling client {client_address}: {e}")
            finally:
                # Close client connection
                try:
                    client_socket.close()
                    print(f"Connection closed with {client_address}")
                except socket.error as e:
                    print(f"Error closing connection with {client_address}: {e}")

        def stop(self):

            self.running = False
            if self.server_socket:
                try:
                    self.server_socket.close()
                    print("Server stopped")
                except socket.error as e:
                    print(f"Error closing server socket: {e}")


    class SimpleClient:

        def __init__(self, host=HOST, port=PORT):
            self.host = host
            self.port = port

        def connect_and_receive(self):

            client_socket = None

            try:
                # Create socket
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # Set connection timeout
                client_socket.settimeout(10.0)

                print(f"Connecting to server at {self.host}:{self.port}...")

                # Connect to server
                client_socket.connect((self.host, self.port))
                print("Connected to server successfully!")

                # Receive message from server
                data = client_socket.recv(BUFFER_SIZE)

                if data:
                    message = data.decode('utf-8')
                    print(f"Message received from server: '{message}'")
                    return message
                else:
                    print("No data received from server")
                    return None

            except socket.timeout:
                print("Connection timeout - server may not be running")
                return None
            except ConnectionRefusedError:
                print("Connection refused - make sure the server is running")
                return None
            except socket.gaierror as e:
                print(f"Address resolution error: {e}")
                return None
            except socket.error as e:
                print(f"Socket error: {e}")
                return None
            except Exception as e:
                print(f"Unexpected error: {e}")
                return None
            finally:
                # Close socket
                if client_socket:
                    try:
                        client_socket.close()
                        print("Client connection closed")
                    except socket.error as e:
                        print(f"Error closing client socket: {e}")


    def run_server():
        server = SimpleServer()
        server.start()


    def run_client():
        client = SimpleClient()
        return client.connect_and_receive()


    def main():

        if len(sys.argv) > 1:
            if sys.argv[1].lower() == 'server':
                print("Starting server mode...")
                run_server()
            elif sys.argv[1].lower() == 'client':
                print("Starting client mode...")
                run_client()
            else:
                print("Usage: python script.py [server|client]")
                print("If no argument provided, will run interactive demo")
        else:
            # Interactive demo
            print("=" * 50)
            print("CLIENT-SERVER PROGRAM DEMONSTRATION")
            print("=" * 50)
            print("\nThis demo will:")
            print("1. Start a server in a background thread")
            print("2. Create multiple clients to connect to the server")
            print("3. Show the communication between client and server")
            print("\nStarting demo...\n")

            # Start server in background thread
            server = SimpleServer()
            server_thread = threading.Thread(target=server.start)
            server_thread.daemon = True
            server_thread.start()

            # Give server time to start
            time.sleep(1)

            # Create and run multiple clients
            print("\n" + "-" * 30)
            print("Running client connections:")
            print("-" * 30)

            for i in range(3):
                print(f"\nClient {i + 1}:")
                client = SimpleClient()
                message = client.connect_and_receive()
                time.sleep(1)  # Small delay between clients

            print("\n" + "-" * 30)
            print("Demo completed!")
            print("Press Ctrl+C to exit")
            print("-" * 30)

            # Keep main thread alive
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nShutting down...")
                server.stop()


    if __name__ == "__main__":
        main()

        import requests
        import sqlite3
        import json
        from typing import Dict, List, Optional, Any

        # ============================================================================
        # PART 1: WHAT IS AN API AND HOW TO USE IT
        # ============================================================================

        """
        What is an API?

        API (Application Programming Interface) is a set of rules and protocols that allows 
        different software applications to communicate with each other. It defines how 
        requests and responses should be formatted.

        Think of an API as a waiter in a restaurant:
        - You (the client) tell the waiter (API) what you want from the menu
        - The waiter takes your request to the kitchen (server)
        - The kitchen prepares your order and gives it back to the waiter
        - The waiter brings your food (data) back to you

        Common API Types:
        - REST APIs: Use HTTP methods (GET, POST, PUT, DELETE)
        - GraphQL APIs: Query language for APIs
        - SOAP APIs: XML-based protocol
        - WebSocket APIs: Real-time communication

        HTTP Methods:
        - GET: Retrieve data
        - POST: Create new data
        - PUT: Update existing data
        - DELETE: Remove data
        """


        class APIDemo:
            """Demonstrates various ways to interact with APIs using the requests library."""

            def __init__(self):
                self.session = requests.Session()
                # Set default headers that will be used for all requests
                self.session.headers.update({
                    'User-Agent': 'Python API Demo/1.0'
                })

            def basic_get_request(self, url: str) -> Optional[Dict]:
                """
                Make a basic GET request to an API.

                Args:
                    url (str): The API endpoint URL

                Returns:
                    Optional[Dict]: JSON response data or None if request failed
                """
                try:
                    print(f"Making GET request to: {url}")

                    # Make the GET request
                    response = requests.get(url)

                    # Check if request was successful (status code 200-299)
                    response.raise_for_status()

                    # Parse JSON response
                    data = response.json()
                    print(f"✓ Request successful! Status code: {response.status_code}")

                    return data

                except requests.exceptions.RequestException as e:
                    print(f"✗ Request failed: {e}")
                    return None
                except json.JSONDecodeError as e:
                    print(f"✗ Failed to parse JSON: {e}")
                    return None

            def advanced_get_request(self, url: str, params: Dict = None, headers: Dict = None) -> Optional[Dict]:
                """
                Make an advanced GET request with parameters and headers.

                Args:
                    url (str): The API endpoint URL
                    params (Dict): Query parameters
                    headers (Dict): Additional headers

                Returns:
                    Optional[Dict]: API response data
                """
                try:
                    # Prepare request parameters
                    request_headers = headers or {}
                    request_params = params or {}

                    print(f"Making advanced GET request to: {url}")
                    if request_params:
                        print(f"Parameters: {request_params}")
                    if request_headers:
                        print(f"Headers: {request_headers}")

                    # Make the request with timeout
                    response = requests.get(
                        url,
                        params=request_params,
                        headers=request_headers,
                        timeout=10  # 10-second timeout
                    )

                    # Check response status
                    response.raise_for_status()

                    # Display response information
                    print(f"✓ Response Status: {response.status_code}")
                    print(f"✓ Response Headers: {dict(response.headers)}")
                    print(f"✓ Response Size: {len(response.content)} bytes")

                    return response.json()

                except requests.exceptions.Timeout:
                    print("✗ Request timed out")
                    return None
                except requests.exceptions.ConnectionError:
                    print("✗ Connection error - check your internet connection")
                    return None
                except requests.exceptions.HTTPError as e:
                    print(f"✗ HTTP error: {e}")
                    print(f"Response content: {response.text[:200]}...")
                    return None
                except Exception as e:
                    print(f"✗ Unexpected error: {e}")
                    return None

            def demonstrate_api_calls(self):
                """Demonstrate various API calls with real examples."""
                print("=" * 60)
                print("API DEMONSTRATION")
                print("=" * 60)

                # Example 1: Simple GET request to JSONPlaceholder (fake REST API)
                print("\n1. Basic GET Request - Fetch a Post:")
                print("-" * 40)
                post_data = self.basic_get_request("https://jsonplaceholder.typicode.com/posts/1")
                if post_data:
                    print(f"Title: {post_data.get('title')}")
                    print(f"Body: {post_data.get('body')[:100]}...")

                # Example 2: GET request with parameters
                print("\n2. GET Request with Parameters - Fetch User Posts:")
                print("-" * 55)
                params = {"userId": 1}
                posts_data = self.advanced_get_request(
                    "https://jsonplaceholder.typicode.com/posts",
                    params=params
                )
                if posts_data:
                    print(f"Found {len(posts_data)} posts for user 1")
                    print(f"First post title: {posts_data[0].get('title')}")

                # Example 3: GET request with custom headers
                print("\n3. GET Request with Custom Headers:")
                print("-" * 40)
                custom_headers = {"Accept": "application/json"}
                user_data = self.advanced_get_request(
                    "https://jsonplaceholder.typicode.com/users/1",
                    headers=custom_headers
                )
                if user_data:
                    print(f"User: {user_data.get('name')} ({user_data.get('email')})")
                    print(f"Company: {user_data.get('company', {}).get('name')}")


        # ============================================================================
        # PART 2: SQLITE DATABASE CONNECTION AND OPERATIONS
        # ============================================================================

        """
        What is SQLite?

        SQLite is a lightweight, serverless, self-contained SQL database engine that 
        stores data in a single file. It's perfect for development, testing, and 
        applications that don't require a full database server.

        Why use SQLite?
        - No server setup required
        - Zero configuration
        - Cross-platform
        - ACID compliant
        - Supports most SQL features
        - Perfect for desktop and mobile apps

        Steps to connect to SQLite database:
        1. Import sqlite3 module (built into Python)
        2. Create/connect to database file
        3. Create a cursor object
        4. Execute SQL commands
        5. Commit changes (for modifications)
        6. Close the connection
        """


        class SQLiteDemo:
            """Demonstrates SQLite database operations with comprehensive examples."""

            def __init__(self, db_name: str = "demo_database.db"):
                self.db_name = db_name
                self.connection = None
                self.cursor = None

            def connect_to_database(self):
                """
                Step 1 & 2: Connect to SQLite database

                Purpose: Establishes connection to the database file.
                If the file doesn't exist, SQLite creates it automatically.
                """
                try:
                    print(f"Connecting to database: {self.db_name}")

                    # Create connection to database
                    # If file doesn't exist, it will be created
                    self.connection = sqlite3.connect(self.db_name)

                    # Configure connection to return rows as dictionaries
                    self.connection.row_factory = sqlite3.Row

                    print("✓ Database connection established")
                    return True

                except sqlite3.Error as e:
                    print(f"✗ Database connection failed: {e}")
                    return False

            def create_cursor(self):
                """
                Step 3: Create a cursor object

                Purpose: Cursor allows you to execute SQL commands and fetch results.
                Think of it as a pointer that moves through the result set.
                """
                if not self.connection:
                    print("✗ No database connection available")
                    return False

                try:
                    self.cursor = self.connection.cursor()
                    print("✓ Database cursor created")
                    return True

                except sqlite3.Error as e:
                    print(f"✗ Cursor creation failed: {e}")
                    return False

            def create_tables(self):
                """
                Step 4: Execute SQL commands to create tables

                Purpose: Set up the database structure (tables, indexes, etc.)
                """
                if not self.cursor:
                    print("✗ No cursor available")
                    return False

                try:
                    print("Creating database tables...")

                    # Create users table
                    self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            age INTEGER,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    ''')

                    # Create posts table
                    self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS posts (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            title TEXT NOT NULL,
                            content TEXT,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users (id)
                        )
                    ''')

                    print("✓ Tables created successfully")
                    return True

                except sqlite3.Error as e:
                    print(f"✗ Table creation failed: {e}")
                    return False

            def insert_sample_data(self):
                """
                Insert sample data into the database

                Purpose: Populate tables with test data for demonstration
                """
                if not self.cursor:
                    return False

                try:
                    print("Inserting sample data...")

                    # Insert users
                    users_data = [
                        ("Alice Johnson", "alice@example.com", 28),
                        ("Bob Smith", "bob@example.com", 35),
                        ("Carol Davis", "carol@example.com", 42)
                    ]

                    self.cursor.executemany(
                        "INSERT OR IGNORE INTO users (name, email, age) VALUES (?, ?, ?)",
                        users_data
                    )

                    # Insert posts
                    posts_data = [
                        (1, "My First Post", "This is the content of my first post"),
                        (1, "Another Post", "More interesting content here"),
                        (2, "Bob's Thoughts", "Sharing my thoughts with the world"),
                        (3, "Carol's Update", "Latest news from Carol")
                    ]

                    self.cursor.executemany(
                        "INSERT OR IGNORE INTO posts (user_id, title, content) VALUES (?, ?, ?)",
                        posts_data
                    )

                    print("✓ Sample data inserted")
                    return True

                except sqlite3.Error as e:
                    print(f"✗ Data insertion failed: {e}")
                    return False

            def query_data(self):
                """
                Execute SELECT queries to retrieve data

                Purpose: Demonstrate different ways to fetch and display data
                """
                if not self.cursor:
                    return False

                try:
                    print("\nQuerying database:")
                    print("-" * 30)

                    # Query 1: Fetch all users
                    print("1. All Users:")
                    self.cursor.execute("SELECT * FROM users")
                    users = self.cursor.fetchall()

                    for user in users:
                        print(f"   ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Age: {user['age']}")

                    # Query 2: Fetch posts with user information (JOIN)
                    print("\n2. Posts with User Information:")
                    self.cursor.execute("""
                        SELECT p.title, p.content, u.name as author
                        FROM posts p
                        JOIN users u ON p.user_id = u.id
                        ORDER BY p.created_at DESC
                    """)
                    posts = self.cursor.fetchall()

                    for post in posts:
                        print(f"   '{post['title']}' by {post['author']}")
                        print(f"      Content: {post['content'][:50]}...")

                    # Query 3: Count posts by user
                    print("\n3. Posts Count by User:")
                    self.cursor.execute("""
                        SELECT u.name, COUNT(p.id) as post_count
                        FROM users u
                        LEFT JOIN posts p ON u.id = p.user_id
                        GROUP BY u.id, u.name
                    """)
                    counts = self.cursor.fetchall()

                    for count in counts:
                        print(f"   {count['name']}: {count['post_count']} posts")

                    return True

                except sqlite3.Error as e:
                    print(f"✗ Query execution failed: {e}")
                    return False

            def commit_changes(self):
                """
                Step 5: Commit changes to the database

                Purpose: Save all changes made during the transaction.
                Without commit, changes are only temporary.
                """
                if not self.connection:
                    return False

                try:
                    self.connection.commit()
                    print("✓ Changes committed to database")
                    return True

                except sqlite3.Error as e:
                    print(f"✗ Commit failed: {e}")
                    return False

            def close_connection(self):
                """
                Step 6: Close the database connection

                Purpose: Free up system resources and ensure data integrity.
                Always close connections when done.
                """
                try:
                    if self.cursor:
                        self.cursor.close()
                        print("✓ Cursor closed")

                    if self.connection:
                        self.connection.close()
                        print("✓ Database connection closed")

                    return True

                except sqlite3.Error as e:
                    print(f"✗ Error closing connection: {e}")
                    return False

            def demonstrate_database_operations(self):
                """Complete demonstration of SQLite database operations."""
                print("=" * 60)
                print("SQLITE DATABASE DEMONSTRATION")
                print("=" * 60)

                # Step 1-2: Connect to database
                if not self.connect_to_database():
                    return

                # Step 3: Create cursor
                if not self.create_cursor():
                    return

                # Step 4: Create tables and insert data
                if not self.create_tables():
                    return

                if not self.insert_sample_data():
                    return

                # Step 5: Commit changes
                if not self.commit_changes():
                    return

                # Demonstrate queries
                self.query_data()

                # Step 6: Close connection
                self.close_connection()


        def main():
            """Main function to demonstrate both API and Database concepts."""
            print("COMPREHENSIVE GUIDE: APIs AND DATABASES")
            print("=" * 80)

            # Demonstrate API usage
            api_demo = APIDemo()
            api_demo.demonstrate_api_calls()

            print("\n\n")

            # Demonstrate SQLite database usage
            db_demo = SQLiteDemo()
            db_demo.demonstrate_database_operations()

            print("\n" + "=" * 80)
            print("SUMMARY")
            print("=" * 80)
            print("""
        API (Application Programming Interface):
        - Set of rules for software communication
        - Use requests library for HTTP requests
        - Handle errors and timeouts properly
        - Common methods: GET, POST, PUT, DELETE

        SQLite Database Steps:
        1. Import sqlite3 and connect to database file
        2. Create cursor object for executing commands
        3. Execute SQL commands (CREATE, INSERT, SELECT, etc.)
        4. Commit changes to save modifications
        5. Close connection to free resources

        Both are essential for modern Python applications!
            """)


        if __name__ == "__main__":
            main()



















