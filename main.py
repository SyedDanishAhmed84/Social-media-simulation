class User:
  def __init__(self,name,email,password):
    self.name=name
    self.email=email
    self.__password=password

    def set_password(self,password):
      self.__password=password

    def get_password(self,password):
        self.__password=password


class Post:
  def __init__(self,content,user):
    self.content=content
    self.user=user
    self.likes=0
    self.comments=[]

  def add_comment(self,comment):
    self.comments.append(comment)       

  def add_like(self):
   self.likes=self.likes+1

class Notification:
  def __init__(self,user):
    self.user=user

  def send_notification(self,notification):
    if notification == "post":
      print(f"{self.user.name} got a new post")
    elif notification == "like":
      print(f"{self.user.name} got a new like")
    elif notification == "comment":
      print(f"{self.user.name} got a new comment")


user1=User("Danish","daniahmed755@gmail.com",1234)
user2=User("Shadman","shadman12@gmail.com",2356)

post1=Post("My first post",user1)
post1.add_comment("Heyy")
post1.add_like()

notif=Notification(user1)
notif.send_notification("post")
notif.send_notification("like")

notif=Notification(user2)
notif.send_notification("comment")
notif.send_notification("like")