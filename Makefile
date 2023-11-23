.PHONY: release


PACKAGE := $(shell grep '^name =' pyproject.toml | cut -d '"' -f2)
VERSION := $(shell grep '^VERSION =' ${PACKAGE}/settings.py | cut -d '"' -f2)

# TODO: migrate to hatch
release:
	git checkout main && git pull origin && git fetch -p
	@git log --pretty=format:"%C(yellow)%h%Creset %s%Cgreen%d" --reverse -20
	@echo "\nReleasing v$(VERSION) in 10 seconds. Press <CTRL+C> to abort\n" && sleep 10
	make test && git commit -a -m 'v$(VERSION)' && git tag -a v$(VERSION) -m 'v$(VERSION)'
	git push --follow-tags
