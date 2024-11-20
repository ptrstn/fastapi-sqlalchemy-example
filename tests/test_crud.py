from mypackage.crud import get_user_by_email


def test_get_user_by_email(session):
    email = "non_existing@aol.com"
    db_user = get_user_by_email(session, email=email)
    assert db_user is None
