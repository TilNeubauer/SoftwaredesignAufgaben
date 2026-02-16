from pathlib import Path
import pandas as pd
from datetime import datetime
import copy

csv_path = Path.cwd() / "src" / "D_ScientificComputing" /  "death_valley_2014.csv" 
df = pd.read_csv(csv_path)

def str2date(date_str):
    #print(el)
    date_format = '%Y-%m-%d'
    date_obj = datetime.strptime(date_str, date_format)

    return date_obj

def date2month(date):
    return date.month

def f2c(f):
    c = (f - 32) * 5/9
    return c


def bigger180(df):
    return df.loc[df[' WindDirDegrees'] > 180].copy()

def newAngle(df):
    df.loc[:, ' WindDirDegrees'] = 180 - df[' WindDirDegrees']
    return df


def fill_missing_from_original(df, df_orig):
    return df.combine_first(df_orig)

def filterMonth(df, m):
    return df.loc[df["Month"] == m].copy()

def minusMean(df):
    df.loc[:, ' Mean Humidity'] = df[' Mean Humidity'] / df[' Mean Humidity'].mean()
    return df


if __name__ == "__main__":

    
    #--------------- PST 2 DateTime -------------------------
    newPST = df["PST"].apply(str2date)
    df["PST"] = newPST
    #print(f"{type(df["PST"][1])}")

    #----------------------- new col Month ---------------------------
    m = df["PST"].apply(date2month)
    df['Month'] = m
    #----------------------
    #print(f"{df[' Mean Humidity'] = }")

    df_newHum = df.copy()

    for mo in range(1,13):
        df_newHum = (df
                     .pipe(filterMonth,m=mo)
                     .pipe(minusMean)
                     .pipe(fill_missing_from_original,df_orig=df))
                 
    

    print(f"Mean Humidity:{df[' Mean Humidity'].mean()}")
    print(f"{df_newHum[' Mean Humidity'] = }")
    print(f"{df[' Mean Humidity'] = }")


    print(f"df31:{df[' Mean Humidity'][3]}")
    print(f"df43:{df[' Mean Humidity'][4]}")
#
    print(f"df_newHum31:{df_newHum[' Mean Humidity'][3]}")
    print(f"df_newHum43:{df_newHum[' Mean Humidity'][4]}")


    #--------------- .pipe Wind -------------------------
    

    

    #df_Wind = (df
    #           .pipe(bigger180)
    #           .pipe(newAngle)
    #           .pipe(fill_missing_from_original,df_orig=df))
                

    #print(f"{df[' Mean Humidity'] = }")

    #print(df[' Mean Humidity'].mean)

    #--------------- create DF with C° -------------------------
    dfC = pd.DataFrame({"Max TemperatureC": df["Max TemperatureF"], "Mean TemperatureC": df["Mean TemperatureF"], "Min TemperatureC": df["Min TemperatureF"],})
    dfC["Max TemperatureC"] = dfC["Max TemperatureC"].apply(f2c)
    dfC["Mean TemperatureC"] =dfC["Mean TemperatureC"].apply(f2c)
    dfC["Min TemperatureC"] = dfC["Min TemperatureC"].apply(f2c)


    #--------------- Merge DFs -------------------------
    df["Max TemperatureF"]  = dfC["Max TemperatureC"] 
    df["Mean TemperatureF"] = dfC["Mean TemperatureC"]
    df["Min TemperatureF"]  = dfC["Min TemperatureC"] 

    df = df.rename(columns={"Max TemperatureF": "Max TemperatureC", "Mean TemperatureF": "Mean TemperatureC", "Min TemperatureF" : "Min TemperatureC"})


    #print(f"Before correction in January: {df = }")

    #--------------- correct January for 1% -------------------------
    newMaxTempC = []
    newMeanTempC = []
    newMinTempC = []
    for i, e in enumerate(df["PST"]):
        if e.month == 1:
            newMaxTempC.append(df["Max TemperatureC"][i] * 1.01)
            newMeanTempC.append(df["Mean TemperatureC"][i] * 1.01)
            newMinTempC.append(df["Min TemperatureC"][i] * 1.01)


    #df["Max TemperatureC"].update(newMaxTempC)
    #df["Mean TemperatureC"].update(newMeanTempC)
    #df["Min TemperatureC"].update(newMinTempC) 

    #print(f"After correction in January:{df = }")

    