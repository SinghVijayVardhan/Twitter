import os


users=[]

class CreatePost:
	def __init__(self,post,user,name):
		self.user=user
		self.post=post
		self.tag=set()
		self.like=set()
		self.comment=[]
		self.name=name
		self.share=set()
	def Like(self,name):
		self.like.add(name)
	def Comment(self,name,cmnt):
		di={name:cmnt}
		self.comment.append(di)
	def show(self):
		for i in range(len(self.comment)):
			for j in self.comment[i]:
				print("\t\t\t\t",j,"\t",self.comment[i].get(j))
	def display(self,name):
		print("\t\t\t",self.name,"\n\t\t\t ",self.post)
		print("\t\t\t1.Like",len(self.like),"\t2.Comment",len(self.comment),"\t3.Share",len(self.share),"\t4.Next Post")
		self.show()
		choice=int(input("Enter Choice : "))
		if choice==1:
			self.Like(name)
		elif choice==2:
			cmnt=input("Comments: ")
			self.Comment(name,cmnt)
		elif choice==3:
			for i in range(len(users)):
				print(i+1," ",users[i].name,end=" ")
			print()
			active=int(input("Enter Choice : "))-1
			if active<len(users) and users[active].name!=name:
					self.share.add(users[active].name)
					users[active].SeePost.append(self)
				
				
class NewsFeed(CreatePost):
	def Upload(self):
		post=input("Write Here : ")
		self.Post.append(CreatePost(post,self.user,self.name))
		active=len(self.Post)-1
		choice=int(input("Enter 1 To Tag Users : "))
		if choice==1:
			num=int(input("\t\tEnter Numbers of Users to Tag : "))
			for i in range(len(users)):
				print(i+1," ",users[i].name,end=" ")
			print()
			li=[int(input())-1 for i in range(num)]
			for i in li:
				if i<len(users) and users[i]!=self.name:
					self.Post[active].tag.add(users[i].user)
			self.SeePost.append(self.Post[active])
			lis=list(set(li))
			for i in lis:
				if i<len(users) and users[i].user!=self.user:
					users[i].SeePost.append(self.Post[active])
	def Newsfeed(self):
		print("\t\t===============================================")
		for i in range(len(self.SeePost)):
			self.SeePost[i].display(self.user)	
			print("\t\t--------------------------------------------")
		print("\t\tNo More Posts")
		print("\t\t================================================")

class FollowOther:
	def follow(self):
		for i in range(len(users)):
			print(i+1," ",users[i].name)
			if users[i].name!=self.user:
				print("\tMutual Friends : ",end=" ")
				li=list(users[i].following&self.following)
				for i in li:
					print(i,end=" ")
				print()
		choice=int(input("Enter Choice : "))
		if users[choice-1].user != self.user:
			self.following.add(users[choice-1].name)
			users[choice-1].follower.add(self.name)
			if len(users[choice-1].follower)==10 and not users[choice-1].name.endswith('*'):
				users[choice-1].name=users[choice-1].name+'*'
		else:
			print("Invalid Choice")

class account(FollowOther,NewsFeed):
	def __init__(self,username,password):
		self.user=username
		self.name=username
		self.password=password
		self.follower=set()
		self.following=set()
		self.SeePost=[]
		self.Post=[]
	def login(self):
		print("\t\t******Welcome ",self.user,"********")
		log=1
		while(log!=6):
			print("\t\tPress 1 Following",end="")
			print("\tPress 2 Followers",end="")
			print("\tPress 3 To Follow",end="")
			print("\tPress 4 To Post\t\tPress 5 To See Post",end="")
			print("\tPress 6 To logout ")
			log=int(input("\t\tEnter : "))
			if log==1:
				for i in self.following:
					print(i,end=" ")
				print()
			elif log==2:
				for i in self.follower:
					print(i,end=" ")
				print()
			elif log==3:
				self.follow()
			elif log==4:
				self.Upload()
			elif log==5:
				self.Newsfeed()
			elif log==6:
				os.system('clear')
				
choice=0
while(choice!=3):
	print("\n\t\tPress 1 Sign up",end="")
	print("\t\tPress 2 Sign in",end="")
	print("\t\tPress 3 Exit",end="  ")
	choice=int(input("\tEnter : "))
	os.system('clear')
	if choice==1:
		flag=1
		first=input("Enter your first name :")
		last=input("Enter your last name :")
		username='@'+first.capitalize()+last.capitalize()
		for i in users:
			if i.user==username:
				flag=0
				break
		if flag==1:
			pa=True
			while pa!=False:
				pa=False
				print("\t\t***Username :",username,"****")
				pas=input("Enter Password :")
				for i in range(0,len(pas)):
					if pas[0].isalpha()==False:
						flag=0
						print("\t\tFirst letter of password must be an alphabet")
						pa=True
						break
					elif len(pas)<8:
						print("\t\tpassword must have atleast 8 characters")
						flag=0
						pa=True
						break
					elif pas[i].isalpha()==True or pas[i].isnumeric()==True or pas[i]=='_':
						flag=1
					else :
						print("\t\tpassword can have only alphabet, number or '_' only")
						flag=0
						pa=True
						break
		else:
			print("\t\tUsername is already taken")
		if flag==1:
			print("\tUsername: ",username)
			print("\tPassword: ",pas)
			users.append(account(username,pas))
			print("\t\t**Wel Come**")
	elif choice==2:
		mark=0
		u=input("\t\tUsername :")
		p=input("\t\tPassword :")
		for i in range(len(users)):
			if users[i].user==u and users[i].password==p:
				mark=1
				active=i
				break
		if mark==1:
			users[i].login()
		else:
			print("\t\tWrong Credential !!!")
