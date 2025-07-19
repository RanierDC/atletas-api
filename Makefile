run: 
	@uvicorn api.main:app --reload
run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head
create-migrations: 
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)