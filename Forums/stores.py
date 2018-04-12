#entity_exists
#اكتب الدالة delete.


class Member_store:
    members = []
    last_id = 1



    def Add(self, member):
        member.id = Member_store.last_id
        if self.entity_exists(member):
            self.delete(member.id)
        Member_store.members.append(member)
        Member_store.last_id += 1




    def get_All(self):
        for member in Member_store.members:
            print("name is: {}\nage is: {}\nid is: {}\n{}".format(member.name, member.age, member.id, ("="*50)))



    def getById(self, id):
        all_members = Member_store.members
        result = None
        for member in all_members:
            if member.id == id:
                result = member
        return result



    def entity_exists(self, member):
        result = False
        if self.getById(member.id):
            result = True
        return result



    def delete(self, id):
        member= self.getById(id)
        Member_store.members.remove(member)




class Post_store:
    Posts = []
    last_id = 1

    def Add(self, post):
        post.id = Post_store.last_id
        if self.entity_exists(post):
            self.delete(post.id)
        Post_store.Posts.append(post)
        Post_store.last_id += 1


    def get_All(self):
        for post in Post_store.Posts:
            print(post.title, post.content, post.id)


    def getById(self, id):
        all_posts = Post_store.Posts
        result = None
        for post in all_posts:
            if post.id == id:
                result = post
        return result



    def entity_exists(self, post):
        result = False
        if self.getById(post.id):
            result = True
        return result



    def delete(self, id):
        post = self.getById(id)
        Post_store.Posts.remove(post)