P205 = int(input())
Ca = float(input())

# Cuando las categorías son iguales 

if P205 > 69 :
    if Ca >= 2 and Ca <= 4 : 
        print ("Sumamente apto")

if P205 > 58 and P205 <= 69 :
    if Ca > 4 and Ca <= 8 :
        print("Moderadamente apto")

if P205 > 46 and P205 < 57 : 
    if Ca > 8 and Ca <= 12 :
        print("Marginalmente apto")

if P205 < 46 :
    if Ca < 2 or Ca > 12 :
        print("No apto")

# Cuanto P205 es SUMAMENTE APTO y Ca tiene valores menores

if P205 > 69 :
    if Ca > 4 and Ca <= 8 :
        print ("Moderadamente apto")

if P205 > 69 :
    if Ca > 8 and Ca <= 12 :
        print ("Marginalmente apto")

if P205 > 69 :
    if Ca < 2 or Ca > 12 :
        print("No apto")

# Cuando P205 es MODERADAMENTE APTO y Ca tiene valores menores 

if P205 > 58 and P205 <= 69 :
    if Ca > 8 and Ca <= 12 :
        print ("marginalmente apto")

if P205 > 58 and P205 <= 69 :
    if Ca < 2 or Ca > 12 :
        print ("No apto")

# Cuando P205 es MARGINALMENTE APTO y Ca es NO APTO

if P205 > 46 and P205 < 57 : 
    if Ca < 2 or Ca > 12 : 
        print ("No apto")

# Cuando Ca es SUMAMENTE APTO y P205 tiene valores menores

if P205 > 58 and P205 <= 69 :
    if Ca >= 2 and Ca <= 4 : 
        print ("Moderadamente apto")

if P205 > 46 and P205 < 57 : 
    if Ca >= 2 and Ca <= 4 : 
        print ("Marginalmente apto")

if P205 < 46 :
    if Ca >= 2 and Ca <= 4 : 
        print ("No apto")

# Cuando Ca es MODERADAMENTE APTO Y P205 tiene valores menores

if P205 > 46 and P205 < 57 : 
    if Ca > 4 and Ca <= 8 :
        print ("Marginalmente apto")

if P205 < 46 :
    if Ca > 4 and Ca <= 8 :
        print ("No apto")

# Cuando Ca es MARGINALMENTE APTO y P205 es No Apto 

if P205 < 46 :
    if Ca > 8 and Ca <= 12 :
        print ("No apto")