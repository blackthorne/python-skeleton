init:
	pip install -r requirements.txt

test:
	py.test tests

clean:
	rm -r *.pyc logs/* tests/.hypothesis .hypothesis .cache
