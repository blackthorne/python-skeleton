.DEFAULT_GOAL := setup

name=`grep name= setup.py |cut -d'=' -f2|cut -d',' -f1|tr -d \'`
version=`grep version= setup.py |cut -d'=' -f2|cut -d',' -f1|tr -d \'`
author=`grep author= setup.py |cut -d'=' -f2|cut -d',' -f1|tr -d \'`
author_email=`grep author_email= setup.py |cut -d'=' -f2|cut -d',' -f1|tr -d \'`
current_project_dir=`find . -maxdepth 2 -name __init__.py -print0 | xargs -0 -n1 dirname`


setup:
ifdef name
	@echo "Naming project '$(name)'..."
	@if [ ! -d "$(name)" ]; then mv "$(current_project_dir)" "$(name)"; fi
endif
ifdef version
	@echo "Updating version to v$(version)..."
	@sed -E -i '' "s/__version__ = '[^\']*'/__version__ = '$(version)'/" "$(name)/__main__.py"
endif
ifdef author
	@echo "Updating author to '$(author)'..."
	@sed -E -i '' "s/__author__ = '[^\']*'/__author__ = '$(author) <$(author_email)>'/" "$(name)/__main__.py"
endif

dist:
	mkdir -p dist
	tar --exclude="./tests" --exclude="./data" --exclude="./logs" -zcvf dist/$(name)-$(version).tar.gz *

deps:
	@pip install -r requirements.txt

test:
	@py.test tests

clean:
	@rm -rf *.pyc logs/* dist/ tests/.hypothesis .hypothesis .cache