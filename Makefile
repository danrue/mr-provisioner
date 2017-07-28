APP_DIR=mr_provisioner
FRONTEND_DIR=$(APP_DIR)/admin/ui
DOCS_DIR=docs

.PHONY: frontend
frontend:
	make -C $(FRONTEND_DIR)

.PHONY: lint
lint:
	flake8 $(APP_DIR) --exclude node_modules

.PHONY: docs
docs:
	make -C $(DOCS_DIR) html

.PHONY: dist
dist: frontend
	./setup.py sdist

test:
	pytest --cov=mr_provisioner -s
