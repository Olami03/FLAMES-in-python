#printing banner
print('''
███████╗██╗                 █████╗   ███╗         ███╗███████╗███████╗
██╔════╝██║              ██╔══██╗████╗   ████║██╔════╝██╔════╝
█████╗      ██║              ███████║██╔████╔██║█████╗     ███████╗
██╔══╝      ██║              ██╔══██║██║╚██╔╝██║██╔══╝     ╚════██║
██║              ███████╗██║      ██║██║ ╚═╝     ██║███████╗███████║
╚═╝             ╚══════╝╚═╝      ╚═╝╚═╝               ╚═╝╚══════╝╚══════╝
''')
user = input("Enter your name :").casefold().replace(" ", "")
anotherperson = input("Enter another person's name :").casefold().replace(" ", "")
assert user.isalpha(),"------name should only contain alphabets------"
assert anotherperson.isalpha(),"------name should only contain alphabets------"
#logic to get len of common chr as per flames need
common_chr_len = (len(user)+len(anotherperson) - len(set(user)&set(anotherperson)) * 2 )
#finding relation
if common_chr_len>0:
  relations = ["Friends","Lovers","in Affection","going to Marry eachother","Enemies","siblings"]
  while len(relations)>1:
    index = common_chr_len%len(relations) -1
    if index >=0:
      l = relations[:index]
      r = relations[index+1:]
      relations = r+l
    else:
      relations = relations[:len(relations)-1]
  print(user,"and",anotherperson,"are",relations[0])
else:
  print("may be you are a tester or your's and his/her name is same")
