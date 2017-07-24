.DEFAULT_GOAL := setup

name=`grep name= setup.py |cut -d'=' -f2|cut -d',' -f1|tr -d \'` # equivalent to `python setup.py --name`
version=`grep version= setup.py |cut -d'=' -f2|cut -d',' -f1|tr -d \'` # equivalent to `python setup.py --version`
author=`grep author= setup.py |cut -d'=' -f2|cut -d',' -f1|tr -d \'` # equivalent to `python setup.py --author`  
author_email=`grep author_email= setup.py |cut -d'=' -f2|cut -d',' -f1|tr -d \'` # equivalent to `python setup.py --author-email`
current_project_dir=`find . -maxdepth 2 -name __init__.py -print0 | xargs -0 -n1 dirname`

setup:
ifdef name
	@echo "Naming project '$(strip $(name))' ..."
	@if [ ! -d "$(strip $(name))" ]; then mv "$(strip $(current_project_dir))" "$(strip $(name))"; fi
endif
ifdef version
	@echo "Updating version to v$(strip $(version)) ..."
	@sed -E -i '' "s/__version__ = '[^\']*'/__version__ = '$(strip $(version))'/" "$(strip $(name))/__main__.py"
endif
ifdef author
	@echo "Updating author to '$(strip $(author))' ..."
	@sed -E -i '' "s/__author__ = '[^\']*'/__author__ = '$(strip $(author)) <$(strip $(author_email))>'/" "$(strip $(name))/__main__.py"
endif

dist:
	mkdir -p dist
	tar --exclude="./tests" --exclude="./data" --exclude="./logs" -zcvf dist/`python setup.py --fullname`.tar.gz *

deps:
	@pip install -r requirements.txt

test:
	@py.test tests

clean:
	@rm -rf logs/* dist/ tests/.hypothesis .hypothesis .cache build/ .gitignore~ *.egg-info
	@find . -type f -name '*~' -exec rm {} \;
	@find . -type f -name '*.pyc' -exec rm {} \;
install:
	python setup.py install