from application import db
from application.posts.models import Post

db.drop_all()
print('Dropping db')

db.create_all()
print('Creating db')

print('Seeding db')
post1 = Post(title="deserunt", content="Adipisicing occaecat aliquip laborum aute est qui sit aute ex consequat magna. Minim ea elit elit culpa quis deserunt non veniam. Minim enim quis esse minim. Est pariatur aute officia est nisi ex nostrud ullamco et incididunt adipisicing ipsum eiusmod. Eu consectetur ad do ad laboris officia adipisicing. Nostrud non amet nisi commodo aute ad nostrud ut eiusmod. Tempor anim excepteur nisi nulla qui esse mollit culpa do ut pariatur consequat culpa.")

post2 = Post(title="laboris", content="Anim mollit incididunt ea. Anim sit ut dolor ipsum exercitation amet. Cillum dolore consequat tempor adipisicing duis proident cupidatat et commodo sit nisi cupidatat velit. Sit ex non commodo veniam. Ea mollit quis consequat.")

post3 = Post(title="consectetur", content="Non veniam officia mollit excepteur amet aliqua ullamco commodo officia occaecat esse eu aliqua laborum nostrud. Elit reprehenderit cupidatat velit eu est. Id dolor ea duis voluptate tempor. Sunt nostrud ut aliquip anim culpa esse quis.")

db.session.add_all([post1, post2, post3])

db.session.commit()