from pathlib import Path

from usuarios import Usuario

BASE_DIR: Path = Path(__file__).parent / "arquivos"
ARQ_ENTRADA = "usuarios.txt"
ARQ_SAIDA = "relatorio.txt"


def bytes_para_megabytes(tamanho_bytes: int) -> float:
    return tamanho_bytes / 1024**2


def prc_espaco_ocupado(total: float, tamanho_mb: float) -> float:
    return tamanho_mb / total * 100


try:
    with Path(BASE_DIR / ARQ_ENTRADA).open(encoding="utf-8") as entrada:
        usuarios: list[Usuario] = []
        total_bytes: int = 0

        linhas: list[str] = entrada.readlines()

        for linha in linhas:
            nome: str
            tamanho_bytes: str
            nome, tamanho_bytes = linha.split()

            usuario = Usuario(nome=nome, tamanho_bytes=int(tamanho_bytes))
            usuarios.append(usuario)

            total_bytes += int(tamanho_bytes)

    total_mb: float = bytes_para_megabytes(tamanho_bytes=total_bytes)
    media_mb: float = total_bytes / len(usuarios)

    usuarios.sort(key=lambda x: x.tamanho_bytes, reverse=True)

    with Path(BASE_DIR / ARQ_SAIDA).open(mode="w", encoding="utf-8") as saida:
        saida.write("ACME Inc.         Uso do espaço em disco pelos usuários\n")
        saida.write("-" * 55)
        saida.write("\nNr.  Usuário        Espaço utilizado     % do uso\n\n")

        for i, u in enumerate(usuarios, start=1):
            espaco: float = bytes_para_megabytes(tamanho_bytes=u.tamanho_bytes)
            porcentagem: float = prc_espaco_ocupado(total=total_mb, tamanho_mb=espaco)
            saida.write(f"{i} {u.nome} {espaco:.2f}MB {porcentagem:.2f}%\n")
except FileNotFoundError:
    print("O arquivo de entrada não existe.")
