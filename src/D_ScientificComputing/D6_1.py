import pandas as pd

data = pd.DataFrame({
    'Age': [11, 16, 30, 51]
})

def cat(age):
    
    #age = float(age)
    age = float(age.iloc[0])
    print(age)

    if age < 13:
        return "Child"
    elif age < 19:
        return "Teenager"
    else:
        return "Adult"
    


if __name__ == "__main__":
    
    new = data.apply(cat, axis=1)
    data["Category"] = new
    
    print(f"{data = }")
