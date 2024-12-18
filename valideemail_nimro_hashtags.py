import re

def valemail(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_pattern, email):
        return True
    else:
        return False
def valNuméro(numero):
   num=r'^[+213]+(6|7|5)+([0-9]{8})|[0](6|7|5)([0-9]{8})'
   if re.match(num, numero):
        return True
   else:
        return False
def extract_hashtags_from_file(file_path):
     hashtags=[]
     with open(file_path,'r') as file:
        for line in file:
            hashtags_in_tweet = re.findall(r'#\w+', line)
            hashtags.extend(hashtags_in_tweet)
     return hashtags
   

if __name__ == "__main__":
   email= input("Entrez une adresse e-mail à valider : ")
   nomero=input("Entrez une Numéro  à valider : ")
   if valemail(email):
     print("L'adresse e-mail ",email," est valide.")
   else:
    print("L'adresse e-mail ",email," n'est pas valide.")

   if valemail(nomero):
      print(" Numéro",nomero,"est valide")
   else:
      print(" Numéro",nomero," n'est pas valide")
file_path = "tweest.txt"
hashtags = extract_hashtags_from_file(file_path) 
print("Extracted Hashtags:", hashtags)