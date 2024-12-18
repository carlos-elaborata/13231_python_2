from crud_entidades import AUTORES_ENDPOINT, LIVROS_ENDPOINT, criar_entidades

autores: list[dict[str, str | list[int]]] = [
    {"name": "J.R.R. Tolkien"},  # ID esperado: 1
    {"name": "G.R.R Martin"},  # ID esperado: 2
    {"name": "J.K Rowling"},  # ID esperado: 3
    {"name": "Leo Tolstoy"},  # ID esperado: 4
    {"name": "Fyodor Dostoievski"},  # ID esperado: 5
]


livros: list[dict[str, str | list[int]]] = [
    {
        "title": "The Hobbit",
        "genre": "Fantasy",
        "isbn": "978-0547951973",
        "authors_ids": [1],  # Tolkien
    },
    {
        "title": "A Game of Thrones",
        "genre": "Fantasy",
        "isbn": "978-0553103540",
        "authors_ids": [2],  # G.R.R Martin
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "genre": "Fantasy",
        "isbn": "978-1338878929",
        "authors_ids": [3],  # J.K Rowling
    },
    {
        "title": "War and Peace",
        "genre": "Romance",
        "isbn": "978-1853260629",
        "authors_ids": [4],  # Leo Tolstoy
    },
    {
        "title": "Crime and Punishment",
        "genre": "Romance",
        "isbn": "978-0679734505",
        "authors_ids": [5],  # Fyodor Dostoievski
    },
    {
        "title": "The Silmarillion",
        "genre": "Fantasy",
        "isbn": "978-0544338012",
        "authors_ids": [1],  # Tolkien
    },
    {
        "title": "The Children of Húrin",
        "genre": "Fantasy",
        "isbn": "978-0063379725",
        "authors_ids": [1],  # Tolkien
    },
    {
        "title": "The Fellowship of the Ring",
        "genre": "Fantasy",
        "isbn": "978-0547928210",
        "authors_ids": [1],  # Tolkien
    },
    {
        "title": "The Two Towers",
        "genre": "Fantasy",
        "isbn": "978-0547928203",
        "authors_ids": [1],  # Tolkien
    },
    {
        "title": "The Return of the King",
        "genre": "Fantasy",
        "isbn": "978-0547928197",
        "authors_ids": [1],  # Tolkien
    },
    {
        "title": "A Clash of Kings",
        "genre": "Fantasy",
        "isbn": "978-0553108033",
        "authors_ids": [2],  # G.R.R Martin
    },
    {
        "title": "A Storm of Swords",
        "genre": "Fantasy",
        "isbn": "978-0553106633",
        "authors_ids": [2],  # G.R.R Martin
    },
    {
        "title": "A Feast for Crows",
        "genre": "Fantasy",
        "isbn": "978-0553801507",
        "authors_ids": [2],  # G.R.R Martin
    },
    {
        "title": "A Dance with Dragons",
        "genre": "Fantasy",
        "isbn": "978-0553801477",
        "authors_ids": [2],  # G.R.R Martin
    },
    {
        "title": "Harry Potter and the Chamber of Secrets",
        "genre": "Fantasy",
        "isbn": "978-1338878936",
        "authors_ids": [3],  # J.K Rowling
    },
    {
        "title": "Harry Potter and the Prisoner of Azkaban",
        "genre": "Fantasy",
        "isbn": "978-1338878943",
        "authors_ids": [3],  # J.K Rowling
    },
    {
        "title": "Harry Potter and the Goblet of Fire",
        "genre": "Fantasy",
        "isbn": "978-1338878950",
        "authors_ids": [3],  # J.K Rowling
    },
    {
        "title": "Harry Potter and the Order of the Phoenix",
        "genre": "Fantasy",
        "isbn": "978-1338878967",
        "authors_ids": [3],  # J.K Rowling
    },
    {
        "title": "Harry Potter and the Half-Blood Prince",
        "genre": "Fantasy",
        "isbn": "978-1338878974",
        "authors_ids": [3],  # J.K Rowling
    },
    {
        "title": "Harry Potter and the Deathly Hallows",
        "genre": "Fantasy",
        "isbn": "978-1338878981",
        "authors_ids": [3],  # J.K Rowling
    },
    {
        "title": "Anna Karenina",
        "genre": "Romance",
        "isbn": "978-0143035008",
        "authors_ids": [4],  # Leo Tolstoy
    },
    {
        "title": "The Brothers Karamazov",
        "genre": "Romance",
        "isbn": "978-0140449242",
        "authors_ids": [5],  # Fyodor Dostoievski
    },
    {
        "title": "White Nights",
        "genre": "Fiction",
        "isbn": "978-1676885634",
        "authors_ids": [5, 4],  # Fyodor Dostoievski e Leo Tolstoy
    },
]


def criar_autores(autores: list[dict[str, str | list[int]]]) -> None:
    print("Novo autor:")
    for autor in autores:
        novo_autor: dict[str, str | int | list[dict[str, str | int]]] = criar_entidades(
            entidade=autor,
            endpoint=AUTORES_ENDPOINT,
        )

        if "detail" in novo_autor:
            print(f"Erro ao criar autor: {novo_autor['detail']}")
            continue

        print(f"ID: {novo_autor['id_']}\n  Autor: {novo_autor['name']}")


def criar_livros(livros: list[dict[str, str | list[int]]]) -> None:
    print("\nNovo livro:")
    for livro in livros:
        novo_livro: dict[str, str | int | list[dict[str, str | int]]] = criar_entidades(
            entidade=livro,
            endpoint=LIVROS_ENDPOINT,
        )

        if "detail" in novo_livro:
            print(f"Erro ao criar livro: {novo_livro['detail']}")
            continue

        print(f"ID: {novo_livro['id_']}")
        print(f"  Título: {novo_livro['title']}")
        print(f"  Gênero: {novo_livro['genre']}")
        print(f"  ISBN: {novo_livro['isbn']}")
        if isinstance(novo_livro["authors"], list):
            for autor in novo_livro["authors"]:
                print(f"    Autor: {autor['name']}")


criar_autores(autores=autores)
criar_livros(livros=livros)
