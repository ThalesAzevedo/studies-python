"""
TESTING SQLITE3 MODULE
"""
#### IMPORTING MODULES
import sqlite3

#### SETUP
conn = sqlite3.connect("banco_de_dados.db")
c = conn.cursor()

#### DEFINING FUNCTIONS 
def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS nomes ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT)")

def update_data():
    update_data = 0
    while update_data != 4:
        update_data = int(input("""Deseja modificar o banco de dados?
            1 para EXIBIR DADOS
            2 para INSERIR DADOS
            3 para DELETAR DADOS
            4 para NÄO MODIFICAR   - """))
        print(update_data)

        if update_data == 1:
            read_data()
        if update_data == 2:
            insert_data()
        if update_data == 3:
            delete_data()

def read_data():
    c.execute("SELECT * FROM nomes")
    print("-"*30)
    print("  id  |  firstname  |  lastname    ")
    for line in c.fetchall():
        print(line)
    print("-"*30)

def insert_data():
    new_data = "y"
    while new_data == "y":
        data_first = input("Digite o primeiro nome:")
        data_last = input("Digite o sobrenome:")
        c.execute("INSERT INTO nomes( firstname, lastname) VALUES(?, ?)", (data_first, data_last))
        conn.commit()
        print("Novos dados foram inseridos.")
        new_data = input("Deseja inserir novos nomes? (Y/N)").lower()
    print("Fechando banco de dados.")

def delete_data():
    value = input("Deletar qual valor da coluna id?")   
    c.execute("DELETE FROM nomes WHERE id = %s" %value)
    # c.commit()
    
#### MAIN 

if __name__ == '__main__':
    createTable()
    update_data()

    c.close()
    conn.close()

