

class Member_store:
    members = []

    def Add(self, member):
        self.members.append(member)

    def get_All(self):
        for member in self.members:
            print(member.name, member.age)


class Post_store:
    Posts = []

    def Add(self, post):
        self.Posts.append(post)

    def get_All(self):
        for post in self.Posts:
            print(post.title, post.content)