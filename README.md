# python-crawler-twitter-api

## how to run project

1. Fazer download do projeto com o comando `git clone https://github.com/ATCamposs/python-crawler-twitter-api.git`
2. Entre na pasta do projeto com o comando `cd python-crawler-twitter-api`
3. Instale os pacotes necessários com o comando `pip3 install -r requirements.txt`
4. Rode o arquivo principal do projeto com o comando `python3 main.py`

**Resultado**

Será criada uma pasta com a data atual no formato yyyy-mm-dd (ex: 2022-09-12) com os arquivos:
 - `top_apps_by_total_quote.csv`
 - `top_apps_by_total_quote.json` 
 - `top_apps_by_total_quote.db` 
 
O resultado serão dados extraidos e ordenados do arquivo principal `AppleStore.csv`, com a busca ocorrendo na seguinte ordem:
1. Top 1 app por `rating_count_tot` no genero `News` (Twitter)
2. Top 10 apps por `rating_count_tot` nos generos `Music e Book`
3. Buscar o perfil de cada app da lista pelo nome disponível no CSV, dentro do top 1 app da primeira busca
4. Contar a quantidade de citações(tweets) de cada perfil
5. Ordenar o resultado com base na quantidade de citações de cada perfil
6. Gerar um CSV um JSON e um banco local com os dados obtidos no passo 5.
 
 *exemplo*:
 
 id | track_name | n_citacoes | size_bytes | price | prime_genre
--- | --- | --- | --- | --- | --- 
284035177 | Pandora - Music & Radio | 180903 | 130242560 | 0.0 | Music
510855668 | Amazon Music | 39470 | 77778944 | 0.0 | Music
418987775 | TuneIn Radio - MLB NBA Audiobooks Podcasts Music | 24785 | 101735424 | 0.0 | Music
284993459 | "Shazam - Discover music |  artists |  videos & lyrics" | 19067 | 147093504 | 0.0 | Music
324684580 | Spotify Music | 10912 | 132510720 | 0.0 | Music
302584613 | "Kindle – Read eBooks |  Magazines & Textbooks" | 9355 | 169747456 | 0.0 | Book
509993510 | Smule Sing! | 7012 | 109940736 | 0.0 | Music
290638154 | iHeartRadio – Free Music & Radio Stations | 6731 | 116443136 | 0.0 | Music
336353151 | SoundCloud - Music & Audio | 1097 | 105009152 | 0.0 | Music
421254504 | Magic Piano by Smule | 2 | 55030784 | 0.0 | Music
