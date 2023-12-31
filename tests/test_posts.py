import pytest

from src.core.models.post import Post
from src.core.models.user import User


@pytest.mark.usefixtures('get_db')
class TestPost:

    def test_post_create_update(self):
        user = User.objects.create(
            username="JasonStatham",
            password="jasonsuperPassword123",
            email="jason@statham.test",
        )
        Post.objects.create(
            title="Test Post",
            author=user,
        )
        assert Post.objects.count() == 1
        post = Post.objects.get()
        assert post.title == "Test Post"
        assert post.author.username == "JasonStatham"

        post.title = "Updated Post"
        post.save()
        assert post.title == "Updated Post"

    def test_post_delete(self):
        user = User.objects.create(
            username="JasonStatham",
            password="jasonsuperPassword123",
            email="jason@statham.test",
        )
        Post.objects.create(
            title="Test Post",
            author=user,
        )
        assert Post.objects.count() == 1
        post = Post.objects.get()
        post.delete()
        assert Post.objects.count() == 0
