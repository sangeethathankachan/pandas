import pandas as pd
sal=pd.read_csv("Salaries.zip")
print(sal)
sal_head=sal.head(14865)
print sal_head
print("info :",sal.info())
print("avg :",sal_head['BasePay'].mean())

print("max :",sal_head['OvertimePay'].max())

print("min :",sal_head['OvertimePay'].min())

sal_head.loc[sal_head["EmployeeName"]=="JOSEPH DRISCOLL","JobTitle"]
print("JOSEPH DRISCOLL :",sal_head.loc[sal_head["EmployeeName"]=="JOSEPH DRISCOLL","JobTitle"].iloc[0])

sal_head.loc[sal_head["EmployeeName"]=="JOSEPH DRISCOLL","TotalPay"]
print("he makes :",sal.loc[sal["EmployeeName"]=="JOSEPH DRISCOLL","TotalPayBenefits"].iloc[0])

sal_high=sal["TotalPayBenefits"].max()
print("high sal :",sal_high)
print("highest_paid_person :",sal.loc[sal["TotalPayBenefits"]==sal_high,"EmployeeName"].iloc[0])

sal_low=sal["TotalPayBenefits"].min()
print("low sal :",sal_low)
print("lowest_paid_person :",sal.loc[sal["TotalPayBenefits"]==sal_low,"EmployeeName"].iloc[0])

sal_avg=sal_head["BasePay"].mean()
print "avg_sal :",sal_avg
#print("avg_sal_in_20111 :",sal_head.loc[sal_head["Year"]==2012,sal_avg].iloc[0])
#print("avg_per_year :",sal_head.groupby("Year").mean() ["BasePay"])
#print(sal_head[sal_head["Year"]==2011][sal_avg])


print("No_Job_Titles :",sal["JobTitle"].nunique())
print("Job_Titles :",sal["JobTitle"].value_counts().head(5))

print("value :",sal["JobTitle"].value_counts())
