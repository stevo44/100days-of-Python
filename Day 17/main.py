class User:
   def __init__(self, user_id, username, followers):
       self.id = user_id
       self.username = username
       self.followers = 0
       self.following = 0





user_1 = User("oo1", "Stevo", "stevo@gmail.com")
# adding attribute
# user_1.id = "001"
# user_1.name = "Stevo"
# user_1.email = "stephenngulle@gmail.com"

print(user_1.email)
print(user_1.username)
print(user_1.id)