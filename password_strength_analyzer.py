import re
import sys


#  Common password part :-

def is_common_password(password):
    
    with open("D:\\coding\\Python programming\\Cy_common_password.txt","r") as f1:
        common_password=f1.read().splitlines()
    return password.lower() in common_password  

password=input("Enter a password : ")

if is_common_password(password):
    print("WARNING ! THIS PASSWORD IS TO COMMON .")
    sys.exit()




# Score counting , strength checking and recommendation part :-

def score_counting(password):

    score=0
    recommendation_count=0 
    recommendations=[]

    if len(password)>=8:
        score+=20
    else :
        recommendations.append("-> Make Password of 8 characters.")
        recommendation_count+=1    
              

    if re.search(r"[a-z]",password):
        score+=20
    else :
       recommendations.append("-> Use lowercase characters.")
       recommendation_count+=1    


    if re.search(r"[A-Z]",password):
        score+=20  
    else :
       recommendations.append("-> Use uppercase characters.") 
       recommendation_count+=1        


    if re.search(r"[0-9]",password):
        score+=20  
    else :
        recommendations.append("-> Use digits.") 
        recommendation_count+=1            


    if re.search(r"[@!$%#&`()_~+*/?><,.|^]",password):
        score+=20    
    else :
       recommendations.append("-> Use special characters.")
       recommendation_count+=1       

    return score,recommendation_count,recommendations



score,recommendation_count,recommendations_list = score_counting(password)


with open("D:\\coding\\Python programming\\Cy_recommendation.txt","w") as f2:
    f2.write("\n".join(recommendations_list))


if score <= 40:
    strength ="Weak"

elif score <=70 :
    strength ="Medium"  

else :
    strength ="Strong" 




# Estimated time to crack the password :-

def estimated_crack_time(password):

    count=len(password)

    charset=0

    if re.search(r"[a-z]",password):
        charset+=26

    if re.search(r"[A-Z]",password):
        charset+=26    

    if re.search(r"[0-9]",password):
        charset+=10

    if re.search(r"[@!$%#&`()_~+*/?><,.|^]",password):
        charset+=21

    if charset ==0:
        print("* Inavlid symbol or blank space !\n")
    else:    
        no_of_combination=charset**count
        no_of_pass_guess_per_second=10**9  # Modern GPUs use tool like hashcat can guess 10^9 password per second.
        time=no_of_combination/no_of_pass_guess_per_second
    
        if 0<=time and time<60: 
            print(f"* Time required to crack the password: {time:.6f} seconds.\n")
            return 
    
        elif 60<=time and time<3600:
            time=time/60
            print(f"* Time required to crack the password: {time:.6f} minutes.\n")
            return 
    
        elif 3600<=time and time<86400:
            time=time/(60*60)
            print(f"* Time required to crack the password: {time:.6f} hours.\n")
            return 
    
        elif 86400<time and time<31536000:
            time=time/86400
            print(f"* Time required to crack the password: {time:.6f} days.\n")
            return 
    
        else:
            time=time/31536000
            print(f"* Time required to crack the password: {time:.6f} years.\n")
            return



print("\n")

print("Password Strenght report :-")
print(f"* Strength of the password is: {strength}.") 
print(f"* Score of the password: {score}/100.") 
estimated_crack_time(password)

if recommendation_count>0:

    print("Recommendation:-")
    with open("D:\\coding\\Python programming\\Cy_recommendation.txt","r") as f2:
        print(f2.read())