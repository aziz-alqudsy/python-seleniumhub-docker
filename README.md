# python-seleniumhub-docker
## Siraman Rohani SEIT
1. Create docker compose to pull selenium-hub, chrome, and firefox images
2. Create requirements.txt for install requirements (selenium)
3. Create simple automation testing test.py to open browser and go to https://ruangguru.com
4. Create Dockerfile to install python, install requirements, and run the test
5. Create entrypoint.sh to set multiple command
5. Run docker compose `docker-compose -f docker-compose-v3.yml up -d`
6. Build image testing for docker file `docker build -t aziz/seleniumhub:0.1 .`
7. Run container seleniumhub using `docker run --net=host test aziz/seleniumhub:0.1`
