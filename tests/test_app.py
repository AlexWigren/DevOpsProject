import pytest

import app as crud_app


@pytest.fixture
def app(tmp_path):
    test_app = crud_app.create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{tmp_path / 'test.db'}",
        }
    )
    with test_app.app_context():
        yield test_app
        crud_app.db.session.remove()
        crud_app.db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_index_lists_users(client):
    crud_app.db.session.add(
        crud_app.User(name="Ada Lovelace", city="London", contact="ada@lovelace.net")
    )
    crud_app.db.session.commit()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Ada Lovelace" in response.data


def test_add_page_renders_form(client):
    response = client.get("/add")

    assert response.status_code == 200
    assert b"Add New User" in response.data


def test_add_user_persists_submitted_fields(client):
    response = client.post(
        "/add",
        data={"name": "Ada Lovelace", "city": "London", "contact": "ada@lovelace.net"},
    )

    assert response.status_code == 302
    user = crud_app.db.session.scalar(
        crud_app.db.select(crud_app.User).where(crud_app.User.name == "Ada Lovelace")
    )
    assert user is not None
    assert (user.name, user.city, user.contact) == ("Ada Lovelace", "London", "ada@lovelace.net")


def test_edit_user_updates_submitted_fields(client):
    user = crud_app.User(name="Old Name", city="Old City", contact="000")
    crud_app.db.session.add(user)
    crud_app.db.session.commit()

    response = client.post(
        f"/edit/{user.id}",
        data={"name": "Ada Lovelace", "city": "London", "contact": "ada@lovelace.net"},
    )

    assert response.status_code == 302
    crud_app.db.session.expire_all()
    updated_user = crud_app.db.session.get(crud_app.User, user.id)
    assert updated_user is not None
    assert (updated_user.name, updated_user.city, updated_user.contact) == (
        "Ada Lovelace",
        "London",
        "ada@lovelace.net",
    )


def test_delete_user_removes_user(client):
    user = crud_app.User(name="Ada Lovelace", city="London", contact="ada@lovelace.net")
    crud_app.db.session.add(user)
    crud_app.db.session.commit()

    response = client.get(f"/delete/{user.id}")

    assert response.status_code == 302
    crud_app.db.session.expire_all()
    assert crud_app.db.session.get(crud_app.User, user.id) is None