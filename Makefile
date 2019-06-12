run: clean ## clear log files and start servers
	( \
	source ./bin/activate; \
	pip3 install -r requirements.txt; \
	)
	chmod +x get-image-part_L2.py
	chmod +x get-image-part_L3.py
	@echo "\033[36mIf the server doesn't (re)start after this, try 'make stop' and then 'make run'\033[0m"
	nohup python3 get-image-part_L2.py > L2.log &
	nohup python3 get-image-part_L3.py > L3.log &

clean: ## remove log files
	@rm -f L2.log L3.log

stop: ## stop running servers
	pkill -f get-image-part

help: ## probably the command you're looking for
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-7s\033[0m %s\n", $$1, $$2}'
