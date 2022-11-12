# noale
Web Scrapper desenvolvido para a empresa Noale.
A solicitação da empresa exigia a captação de dados de páginas dinâmicas. As informações recebidas foram as
coordenadas geográficas e o nome das cidades. Nesse sentido, foi utilizado o script urlGenerator.py para
gerar as +6400 linhas de urls com os queries corretos. Após isso, e utilizando o Selenium, um webdriver foi 
programado para navegar por todas as +6400 urls e obter os dados em um arquivo data.txt, formatado por
tabulação simples.
