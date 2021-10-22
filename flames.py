print('''
███████╗██╗░░░░░░█████╗░███╗░░░███╗███████╗░██████╗    ,d88b.d88b,
██╔════╝██║░░░░░██╔══██╗████╗░████║██╔════╝██╔════╝    88888888888
█████╗░░██║░░░░░███████║██╔████╔██║█████╗░░╚█████╗░    `Y8888888Y'
██╔══╝░░██║░░░░░██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗      `Y888Y'
██║░░░░░███████╗██║░░██║██║░╚═╝░██║███████╗██████╔╝        `Y'
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░    
''')
# Author = coderatul
# Taking names as input from user
user = input("Enter your name :").casefold().strip()
anotherperson = input("Enter another person's name :").casefold().strip()
assert user.isalpha(),"Excuse me : ------name should only contain alphabets------"
assert anotherperson.isalpha(),"Excuse me :  ------name should only contain alphabets------"
if user == anotherperson:
  print("You are already in love with your self")
else:
  a = (len(user)+len(anotherperson) - len(set(user)&set(anotherperson)) * 2 )
  flames = {1:"Siblings",2:"Enemies",3:"Enemies",4:"Enemies",5:"Friends",
            6:"Going to marry each other",7:"Enemies",8:"In affection",9:"Enemies",
            10:"In Love",11:"Going to marry each other",12:"In affection",
            13:"Siblings",14:"Friends",15:"Going to marry each other",16:"Friends",
            17:"Siblings",18:"Friends",19:"Siblings",20:"Enemies"}
  print("According to FLAMES you and",anotherperson,"are:",flames[a])
