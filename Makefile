install:
	pip install -r requirements.txt

start:
	uv run flask --app example --debug run --port 8000

new_user:
	uv run flask --app new_users --debug run --port 8000
