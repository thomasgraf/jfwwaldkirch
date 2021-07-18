# Jugendfeuerwehr Seite

## Run in docker

build -t jfwsite .

docker run -t -i -v /<path to sqlite>/db/:/app/db/ -p 8080:8000 jfwsite