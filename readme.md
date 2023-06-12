
<details>
<summary><b>Текст тестового задания "Автоматизация тестирования API"</b></summary>

## Автоматизация тестирования API. Часть 1

Необходимо подготовить проект с автотестами, которые будут проверять работу всех API-эндпоинтов, описанных ниже.


### Технические требования:

- API url https://jsonplaceholder.typicode.com/
- Методы, требующие проверки:
GET /posts, POST /posts, DELETE /posts
- Методы могут принимать параметры userId, id, title, body
- В качестве языка программирования используйте python
- Добавьте в README инструкцию по поднятию проекта
- Используйте библиотеку requests, а также pytest


## Автоматизация тестирования API. Часть 2

Напишите Dockerfile к своему приложению по проверке API-методов из части 1.

### Технические требования:
- добавьте команду запуска в README.

</details>


---


# Автоматизация тестирования API

Проект с автотестами, проверяющий работу эндпоинта `https://jsonplaceholder.typicode.com/posts`.

## Особенности JSONPlaceholder

- Отсутствует проверка типа возвращаемых данных - сервер [возвращает тело запроса](https://github.com/typicode/json-server/blob/master/src/server/router/singular.js#L15-L28) (`POST /posts`) либо выполнение такого запроса [не вызывает ошибки из-за "имитации" действий](https://github.com/typicode/json-server/blob/master/src/server/router/plural.js#L306-L327) (`DELETE /posts`), хотя ожидается ошибка от сервера. Тесты с этой особенностью **отмечены маркером xfail**.

## Требования

- [Python](https://www.python.org/downloads/) 3.7 или выше
- [Docker](https://docs.docker.com/engine/install/) (необязательно)
- [Git](https://git-scm.com/book/ru/v2/Введение-Установка-Git)

## Установка и запуск автотестов

1. Склонируйте репозиторий:

   ```
   git clone <repository-url>
   ```

2. Перейдите в папку проекта:

   ```
   cd api_autotests
   ```

Дальнейшие шаги зависят от того, как вы хотите запустить данный проект.


<details>
  <summary><b>Без Docker</b></summary>

3. Разверните изолированную среду (опционально, но рекомендуется):

   ```
   python -m venv env
   ```

   На Windows:

   ```
   env\Scripts\activate
   ```

   
   На macOS/Linux:
   ```
   source env/bin/activate
   ```

4. Установите требуемые зависимости:

   ```
   pip install -r requirements.txt
   ```

5. Запустите тестирование:

   ```
   pytest
   ```
</details>

<details>
  <summary><b>Используя Docker</b></summary>


3. Соберите образ:

   ```
   docker build -t api-autotests .
   ```

4. Запустите контейнер с данным образом (внимание: `--rm` удалит контейнер после выполнения):

   ```
   docker run --rm api-autotests
   ```

5. Удалите образ если запускать его больше не требуется и все данные собраны (опционально):

   ```
   docker image rm api-autotests
   ```
</details>
