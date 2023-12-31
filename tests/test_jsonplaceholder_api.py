import pytest
from fixtures.fixture_jsonplaceholder_api import json_placeholder_api
from http import HTTPStatus

def test_get_posts(json_placeholder_api):
    response = json_placeholder_api.get_posts()
    assert response.status_code == HTTPStatus.OK, "Failed to retrieve posts. Expected status code 200."
    assert len(response.content) > 0, "Failed to retrieve posts. Response content is empty."


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_posts_with_id(json_placeholder_api, post_id):
    response = json_placeholder_api.get_posts_by_id(post_id)
    response_json = response.json()

    assert response.status_code == HTTPStatus.OK, f"Failed to retrieve post with ID {post_id}. Expected status code 200."
    assert response_json.get("id") == post_id, f"Failed to retrieve post with ID {post_id}. ID mismatch in the response."


@pytest.mark.parametrize("post_id", [-1, "string", 3.14, "'", '"', 8086])
def test_get_posts_with_invalid_id(json_placeholder_api, post_id):
    response = json_placeholder_api.get_posts_by_id(post_id)
    assert response.status_code == HTTPStatus.NOT_FOUND, f"Retrieved a post with invalid ID {post_id}. Expected status code 404."


@pytest.mark.parametrize(
    "userId, title, body",
    [
        (1111, "Hello world!", "Example body."),
        (1213, "Test-test-test!", "Yet another example body!"),
    ],
)
def test_post_posts_with_data(json_placeholder_api, userId, title, body):
    response = json_placeholder_api.post_posts(userId=userId, title=title, body=body)
    response_json = response.json()

    assert response.status_code == HTTPStatus.CREATED, "Failed to create a new post. Expected status code 201."
    assert response_json.get("userId") == userId, f"Failed to create a new post. userId mismatch in the response."
    assert response_json.get("title") == title, f"Failed to create a new post. title mismatch in the response."
    assert response_json.get("body") == body, f"Failed to create a new post. body mismatch in the response."


@pytest.mark.xfail(
    strict=True, reason="JSONPlaceholder returns the request body in the response."
)
@pytest.mark.parametrize(
    "userId, title, body",
    [
        ("!@#$", "Invalid userId", "Special Symbols"),
        (3.14, "Invalid userId", "Float"),
        (-9001, "Invalid userId", "Negative value"),
        (" ", " ", " "),
    ],
)
def test_post_posts_with_invalid_data(json_placeholder_api, userId, title, body):
    response = json_placeholder_api.post_posts(userId=userId, title=title, body=body)

    assert response.status_code == HTTPStatus.BAD_REQUEST, "Unexpected success in creating a post with invalid data."


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_delete_posts_with_id(json_placeholder_api, post_id):
    response = json_placeholder_api.delete_posts(post_id)

    assert response.status_code == HTTPStatus.OK, f"Failed to delete post with ID {post_id}. Expected status code 200."


@pytest.mark.xfail(strict=True, reason="JSONPlaceholder does not validate the ID.")
@pytest.mark.parametrize("post_id", [-1, 1.23, "qwerty"])
def test_delete_posts_with_invalid_id(json_placeholder_api, post_id):
    response = json_placeholder_api.delete_posts(post_id)

    assert response.status_code == HTTPStatus.BAD_REQUEST, f"Unexpected success in deleting post with invalid ID {post_id}."
