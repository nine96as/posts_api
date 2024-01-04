from application.posts.models import Post

def test_new_post_with_fixture(new_post):
    """
    GIVEN a Post model
    WHEN a new Post is created
    THEN check the title and content fields are defined correctly
    """
    assert new_post.title == 'adipisicing'
    assert new_post.content == 'Sint proident anim esse excepteur sint ut eiusmod deserunt velit fugiat consectetur. Laborum officia consectetur ipsum ullamco irure velit occaecat. Exercitation eu ipsum excepteur ut elit commodo ea eiusmod nostrud et ex. Eiusmod exercitation mollit dolore. Laborum cillum cillum ullamco enim esse.'
    assert new_post.__repr__() == f'Post(id: {new_post.id}, title: {new_post.title}, user_id: {new_post.user_id})'
    assert new_post.json == {
        "id": new_post.id,
        "title": new_post.title,
        "content": new_post.content,
        "created_at": new_post.created_at,
        "last_modified": new_post.last_modified,
        "user_id": new_post.user_id
    }