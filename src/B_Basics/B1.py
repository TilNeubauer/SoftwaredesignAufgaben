band_members = ["Peter", "Bjorn", "John"]

# 1. 
for member in band_members:
    print(member)

#prints every name of band_members 


# 2.
for member in band_members:
    print(f"{member} played great in this song.")
print(f"I can not wait to hear {member} play in the next song.")

# mks evers print statment in the for loop
# after the for loop variabl <member> still has the last value of <band_members>


# 3.
for member in band_members:
    print(f"{member} played great in this song.")
    print(f"I can not wait to hear {member} play in the next song.")

    print(f"I can not wait to hear all of you at the next gig.")

# mks all the print statmaents for every <band_member>


# 4. 
band_members = ["Peter", "Bjorn", "John"]

for member in band_members:
    print(f"{member} played great in this song.")
    print(f"I can not wait to hear {member} play in the next song.")

print(f"I can not wait to hear all of you at the next gig.")

# mks all the print statmants in the for loop for every <member> in <band_members> 
# after the for loop mks the last print statment 

