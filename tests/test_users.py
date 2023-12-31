import pytest

from src.core.models.user import User


@pytest.mark.usefixtures('get_db')
class TestUser:
    def test_user_create_update(self):
        User.objects.create(
            username="JasonStatham",
            password="jasonsuperPassword123",
            email="jason@statham.test",
        )
        assert User.objects.count() == 1
        user = User.objects.get()
        assert user.username == "JasonStatham"
        assert user.email == "jason@statham.test"

        user.username = "JsonStatHam"
        user.save()
        assert user.username == "JsonStatHam"


    def test_user_delete(self):
        User.objects.create(
            username="JasonStatham",
            password="jasonsuperPassword123",
            email="jason@statham.test",
        )
        assert User.objects.count() == 1
        user = User.objects.get()
        user.delete()
        assert User.objects.count() == 0

