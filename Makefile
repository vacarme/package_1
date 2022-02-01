# ----------------------------------
#          INSTALL & TEST
# ----------------------------------

install:
	@pip install . -U

test:
	@coverage run -m pytest tests/test_*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr mlproject-*.dist-info
	@rm -fr mlproject.egg-info
