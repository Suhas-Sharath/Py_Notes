import sqlite3

conn = sqlite3.connect("anime.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS anime (
               anime_id integer PRIMARY KEY,
               title text NOT NULL,
               release_year interger,
               rating integer
    )""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS characters (
               character_id integer PRIMARY KEY,
               anime_id integer ,
               name text NOT NULL,
               role text,
               FOREIGN KEY (anime_id) REFERENCES anime(anime_id)
    )""")


def insert_into_anime(anime_id,title, release_year, rating):
    """
    Inserts a new record into the anime table.

    Args:
        Anime_id (int): The Id of the anime.
        title (str): The title of the anime.
        release_year (int): The release year of the anime.
        rating (int): The rating of the anime.
    """
    cursor = conn.cursor()
    cursor.execute("INSERT INTO anime (anime_id, title, release_year, rating) VALUES (?,?, ?, ?)",
                   (anime_id,title, release_year, rating))
    conn.commit()

def insert_into_characters(character_id,anime_id, name, role):
    """
    Inserts a new character record into the characters table.

    Args:
        character_id (int) : The ID of the Character.
        anime_id (int): The ID of the anime to which the character belongs.
        name (str): The name of the character.
        role (str): The role of the character.
    """
    cursor = conn.cursor()
    cursor.execute("INSERT INTO characters (character_id,anime_id, name, role) VALUES (?,?, ?, ?)",
                   (character_id,anime_id, name, role))
    conn.commit()

def display_anime():
    """
    Displays all records in the anime table.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM anime")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def display_characters():
    """
    Displays all records in the characters table.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM characters")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def custom_display(query):
    """
    Custom Query which can be designed by the User.

    example:
        SELECT c.character_id, c.anime_id, c.name, c.role
        FROM characters as c
        JOIN anime as a ON c.anime_id = a.anime_id
        WHERE a.rating > 7.7;

    """
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Main program
if __name__ == "__main__":
    while True:
        print("\nMenu")
        print("1. Add Anime ")
        print("2. Add Character")
        print("3. View Anime Table")
        print("4. View Character Table")
        print("5. Custom Query")
        print("0. Exit")

        choice = input("Enter your choice: ")

        print('=' * 75)
        if choice == '1':
            anime_id = input("enter the anime id: ")
            title = input("enter the anime name: ")
            release_year = input("enter the anime release year: ")
            rating = input("enter the anime rating: ")
            insert_into_anime(anime_id,title, release_year, rating)
        elif choice == '2':
            character_id = input("enter the character id: ")
            anime_id = input("enter the anime id: ")
            name = input("enter the character name: ")
            role = input("enter the role: ")
            insert_into_characters(character_id,anime_id, name, role)
        
        elif choice == '3':
            display_anime()
        
        elif choice == '4':
            display_characters()
        
        elif choice == '5':
            query = input("enter the custom query")  
            custom_display(query)
        
        elif choice == '0':
            break
        else:
            print("enter a valid choice")
            
        print('=' * 75)