sports_celebs_age = {
    "sachin":50,
    "nadal":40,
    "ronaldo":45,
    "dhoni":39
}

print({k:v for k,v in sorted(sports_celebs_age.items(),key=lambda x:x[1])})

