.PHONY: setup redis run worker server clean install-uv

setup: install-uv venv uv-sync

# Установка uv, если не найден
install-uv:
	@if ! command -v uv &> /dev/null; then \
		echo "Утилита uv не найдена, выполняется установка..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
		export PATH="$HOME/.local/bin:$${PATH}"; \
		echo "uv установлен успешно."; \
	else \
		echo "Утилита uv уже установлена."; \
	fi

# Создание виртуального окружения с помощью uv
venv:
	@if [ ! -d "venv" ]; then \
		echo "Создание виртуального окружения..."; \
		uv venv venv --python=/opt/hostedtoolcache/Python/3.14.3/x64/bin/python3; \
	else \
		echo "Виртуальное окружение уже существует"; \
	fi

# Синхронизация зависимостей через uv sync
uv-sync: venv
	@if [ ! -f "pyproject.toml" ] && [ ! -f "requirements.txt" ]; then \
		echo "Ошибка: не найден pyproject.toml или requirements.txt"; \
		exit 1; \
	fi; \
	echo "Синхронизация зависимостей с помощью uv sync..."; \
	uv sync --python venv/bin/python --no-install-workspace --frozen

# Запуск Django development server
server: uv-sync
	echo "Запуск Django development server..."; \
	./venv/bin/python manage.py runserver

# Очистка
clean:
	echo "Очистка окружения..."; \
	pkill -f "python manage.py runserver" 2>/dev/null || true; \
	rm -rf venv .venv; \
	echo "Очистка завершена."