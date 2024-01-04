import pytest
from application import app, db
from application.posts.models import Post

@pytest.fixture(scope='module')
def new_post():
    post = Post('adipisicing', 'Sint proident anim esse excepteur sint ut eiusmod deserunt velit fugiat consectetur. Laborum officia consectetur ipsum ullamco irure velit occaecat. Exercitation eu ipsum excepteur ut elit commodo ea eiusmod nostrud et ex. Eiusmod exercitation mollit dolore. Laborum cillum cillum ullamco enim esse.')
    return post
