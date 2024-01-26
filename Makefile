deps:
	python3 -m pip install -r analysis/api/requirements.txt
run :
	python3 analysis/api/main.py
website:
	open analysis/app/index.html