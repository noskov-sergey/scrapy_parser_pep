# Асинхронный парсер PEP

Парсер документов PEP на базе фреймворка Scrapy.

## Описание

- Собирает номер, название и статус всех PEP.
- Подсчитывает общее количество каждого статуса, а также общую сумму всех статусов.

Парсер собирает данные с сайта ```https://www.python.org/```

Вся собранная информация сохраняется в файлах ```csv``` в папке ```results/...```

## Как запустить проект

1. Клонировать репозиторий:

```python
git clone https://github.com/noskov-sergey/scrapy_parser_pep
```

2. Создать виртуальное окружение:

```python
python -m venv venv
```

3. Активировать виртуальное окружение, обновить версию ```pip``` и установить зависимости из ```requirements.txt```:

```python
source venv/bin/activate
```

```python
python -m pip install -–upgrade pip.
```

```python
pip install -r requirements.txt
```

4. Запустить  в консоле:

```python
scrapy crawl pep
```

[⬆Оглавление](#оглавление)

[Sergey Noskov](https://github.com/noskov-sergey/)