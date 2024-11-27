"""Exercício 04.

Relatório de Uso do Espaço em Disco
Desenvolva um programa que gere um relatório ordenado do uso de espaço em disco por
usuário, a partir das informações contidas em um arquivo de texto.
O arquivo "usuarios.txt" possui o seguinte formato:
    alexandre       456123789
    anderson        1245698456
    antonio         123456456
    carlos          91257581
    cesar           987458
    rosemary        789456125
A partir deste arquivo, você deve:
    1. Criar um arquivo chamado relatorio.txt, conforme exemplo, ordenando os
    usuários pelo espaço utilizado, de forma decrescente;
        Exemplo:
                ACME Inc.         Uso do espaço em disco pelos usuários
                -------------------------------------------------------
                Nr.  Usuário        Espaço utilizado     % do uso

                1    anderson       1187,99 MB           46,02%
                2    rosemary       752,88 MB            29,16%
                3    alexandre      434,99 MB            16,85%
                4    antonio        117,73 MB            4,56%
                5    carlos         87,03 MB             3,37%
                6    cesar          0,94 MB              0,04%

                Espaço total ocupado: 2581,57 MB
                Espaço médio ocupado: 430,26 MB
    2. Identificar qual(is) entidades devem ser modeladas como objetos e criar as
    classes apropriadas;
    3. Criar a estrutura de arquivos para acomodar as classes criadas.
Observação: Utilize 1 KB = 1024 bytes e 1 MB = 1024 KB.
"""
