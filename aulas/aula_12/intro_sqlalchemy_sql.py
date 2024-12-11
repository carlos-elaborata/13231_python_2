from sqlalchemy import Engine, create_engine, text

engine: Engine = create_engine(url="sqlite:///aula_12.db")

with engine.connect() as connection:
    connection.execute(statement=text(text="DROP TABLE IF EXISTS usuario"))

    connection.execute(
        statement=text(
            text="CREATE TABLE usuario (id_ INTEGER PRIMARY KEY,"
            "nome TEXT NOT NULL,"
            "sobrenome TEXT NOT NULL)",
        ),
    )

with engine.connect() as connection:
    # connection.execute(
    #     statement=text(
    #         text="INSERT INTO usuario (nome, sobrenome) VALUES"
    #         "('João', 'de Almeida'),"
    #         "('Maria', 'Helena')",
    #     ),
    # )

    connection.execute(
        statement=text(
            text="INSERT INTO usuario (nome, sobrenome) VALUES(:nome, :sobrenome)",
        ),
        parameters=[
            {"nome": "João", "sobrenome": "de Almeida"},
            {"nome": "Maria", "sobrenome": "Helena"},
        ],
    )

    connection.commit()


with engine.connect() as connection:
    resultado = connection.execute(
        statement=text(text="SELECT id_, nome, sobrenome FROM usuario"),
    )

    linhas = resultado.all()

    for linha in linhas:
        print(f"ID: {linha[0]} Nome: {linha[1]} Sobrenome: {linha[2]}")
    print()
    for id_, nome, sobrenome in linhas:
        print(f"ID: {id_} Nome: {nome} Sobrenome: {sobrenome}")
    print()
    for linha in linhas:
        print(f"ID: {linha.id_} Nome: {linha.nome} Sobrenome: {linha.sobrenome}")


with engine.connect() as connection:
    resultado = connection.execute(
        text("SELECT id_, nome, sobrenome FROM usuario WHERE length(nome) > :nome"),
        parameters={"nome": 4},
    )

    print(resultado.first())
