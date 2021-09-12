print('''
███████╗██╗░░░░░░█████╗░███╗░░░███╗███████╗░██████╗    ,d88b.d88b,
██╔════╝██║░░░░░██╔══██╗████╗░████║██╔════╝██╔════╝    88888888888
█████╗░░██║░░░░░███████║██╔████╔██║█████╗░░╚█████╗░    `Y8888888Y'
██╔══╝░░██║░░░░░██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗      `Y888Y'
██║░░░░░███████╗██║░░██║██║░╚═╝░██║███████╗██████╔╝        `Y'
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░    
''')
# Author = coderatul
user = input("enter your name :").casefold()
anotherperson = input("enter another person's name :").casefold()
a = (len(user)+len(anotherperson) - len(set(user)&set(anotherperson)) * 2 )
flames = {1:"siblings",2:"enemies",3:"enemies",4:"enemies",5:"friends",6:"going to marry each other",
         7:"enemies",8:"in affection",9:"enemies",10:"in Love",11:"going to marry each other",12:"in affection",
         13:"siblings",14:"friends",15:"going to marry each other",16:"friends",17:"siblings",
         18:"friends",19:"siblings",20:"enemies"}
print("according to FLAMES you and",anotherperson,"are:",flames[a])
