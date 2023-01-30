import sqlite3

def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           INSERT INTO user ( firstname, lastname, email, password, age)
           VALUES (?, ?, ?, ?, ?);
           """,
           ( firstname, lastname, email, password, age),
       )
       session.commit()
def change_user(firstname: str):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           UPDATE user
           SET firstname = "MAksim"
           WHERE email = "manti.by@gmail.com";
           """,

       )
       session.commit()


if __name__ == "__main__":
    #create_user("Maks", "Pervyshev", "king.by@gmail.com", "che,berlen", 18)
    #change_user("")