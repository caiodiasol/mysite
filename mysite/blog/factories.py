import factory
from faker import Factory as FakerFactory
from django.contrib.auth.models import User
from blog.models import Post

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda _: faker.user_name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super()._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda _: faker.sentence())
    content = factory.LazyAttribute(lambda _: faker.paragraph(nb_sentences=5))
    author = factory.SubFactory(UserFactory)
