# 1. RUN VIRTUAL ENVIROMENT 
python3.9 -m venv .venv && source .venv/bin/activate

# 2. INSTALL DEPENDENCIES
playwright install && pip install -r requirements.txt

# 3. COPY ENV FILE AND CREATE .env
cp .example.env code/.env
echo "POPULATE ENV FILE .env"