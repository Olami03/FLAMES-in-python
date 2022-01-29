print("""
(                               
 )\ )  (                         
(()/(  )\    )     )      (      
 /(_))((_)( /(    (      ))\ (   
(_))_| _  )(_))   )\  ' /((_))\  
| |_   | |((_)_  _((_)) (_)) ((_) 
| __| | | / _` | | '  \/  |/ -_) (_-< 
|_|    |_|\__,_||_|_|_| \___|/__/
linktr.ee/programmeratul
""")
user = input("Enter your name :").casefold().replace(" ", "")
anotherperson = input("Enter another person's name :").casefold().replace(" ", "")
assert user.isalpha(),"------name should only contain alphabets------"
assert anotherperson.isalpha(),"------name should only contain alphabets------"

#converting str to list
chrs_of_user,chrs_of_anotherperson=list(user),list(anotherperson)

#making copy of list(user) and list(anotherperson)
duplicate_list_user = chrs_of_user.copy()
duplicate_list_anotherperson = chrs_of_anotherperson.copy()

 #taling out common chr from another person's name 
for k in chrs_of_user:
  if k in chrs_of_anotherperson:
    chrs_of_anotherperson.remove(k)
    len_anotherperson = len(chrs_of_anotherperson)

 #taking out common chr from user's name   
for f in duplicate_list_anotherperson :
  if f in duplicate_list_user:
    duplicate_list_user.remove(f)
    len_user = len(duplicate_list_user)
common_chr_len = len_anotherperson + len_user

#getting relation b/w user and anotherperson 
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
  print("you naughty naughty !!!")

