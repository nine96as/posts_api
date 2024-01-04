from application.users.models import User

def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the name and password fields are defined correctly
    """
    assert new_user.username == 'a'
    assert new_user.password == 'jkl'
    assert new_user.__repr__() == f'User(id: {new_user.id}, username: {new_user.username})'
    assert new_user.json == {
        "id": new_user.id,
        "username": new_user.username,
        "created_at": new_user.created_at
    }