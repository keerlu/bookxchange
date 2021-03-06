import pytest
from mixer.backend.django import mixer

from django.contrib.auth import get_user_model


class TestBook:
    @pytest.mark.django_db
    def test_model(self):
        book = mixer.blend("books.Book", title="A book")
        assert book.__str__() == "A book", "Should return title"


class TestBookHolder:
    @pytest.mark.django_db
    def test_model(self):
        book = mixer.blend("books.Book", title="A book")
        user1 = mixer.blend(
            get_user_model(), username="user1", email="mail@example.com"
        )
        book_held = mixer.blend("books.BookHolder", book=book, holder=user1)
        assert book_held.date_requested is None
        assert book_held.holder == user1
