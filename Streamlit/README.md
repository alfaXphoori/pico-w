
## Stremlit 

#### Run Streamlit python file
```bash
streamlit run home_dashboard.py
```

#### Build & Run Dockerfile
- stml = docker image name
```bash
docker build -t stml .
```
- Check docker image
```bash
docker images
```
- Remove docker image
    - xxxx = docker image id
```bash
docker rmi -f xxxx
```
- Run docker file
    - stml = docker image name
    - 8501:8501 = In Port: Out Port
```bash
docker run -p 8501:8501 stml
```

#### Run Docker compose
- UP = start dockercompose
    - -d = run background
```bash
docker compose up -d
```
- Down = stop docker compose
```bash
docker compose down
```
- Check Docker Process
```bash
docker ps
```

