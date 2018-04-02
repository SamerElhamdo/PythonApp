from models import Member, Post
from stores import Member_store, Post_store

member1 = Member("samer", 27)
member2 = Member("ahmed", 22)

post1 = Post("hi body1", "how are you1")
post2 = Post("hi body2", "how are you2")
post3 = Post("hi body3", "how are you3")

member_store = Member_store()
post_store = Post_store()

member_store.Add(member1)
member_store.Add(member2)
post_store.Add(post1)
post_store.Add(post2)
post_store.Add(post3)
member_store.get_All()
post_store.get_All()