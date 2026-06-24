import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,root_mean_squared_error,mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import tree
house = pd.read_csv("house_price_practice_data.csv",sep=",")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(house)

print(house.shape)
#checking null values 
print(house.isnull().sum())
print(house[house["Income_Level"]=="?"])
print(house.duplicated().sum())

house["Square_Feet"] = house["Square_Feet"].fillna(0)
print(house.isnull().sum())

print(house.describe())
print(house.info())

house["Income_Level"] = house["Income_Level"].replace("?","Unknown")

print(house["Income_Level"])
house_norm = house["Income_Level"].value_counts(normalize=True)*100
plt.pie(house_norm.values,labels = house_norm.index,autopct="%.2f")
plt.title("Pie Chart of Income Level Distribution")
plt.show()


sns.countplot(house["Neighborhood"])
plt.xlabel("Counts")
plt.ylabel("Neighborhood")
plt.title("Neighborhood vs Counts")
plt.show()


plt.boxplot(x= house["Price"])
plt.title("Boxplot of Price")
plt.show()




house["Income_Level"] = house["Income_Level"].map({"Low":0,"Medium":1,"High":2,"Unknown":-1})


print(house.columns)
print(house.dtypes)

# 1. Convert the list to a string (Your idea!)
house['Neighborhood'] = house['Neighborhood'].astype(str)

# 2. Erase the left bracket [, the right bracket ], and the quotes '
house['Neighborhood'] = house['Neighborhood'].str.replace(r"[\[\]']", "", regex=True)
house= house[house["Price"]>=0]
x = house[["Square_Feet","Bedrooms","Bathrooms","Neighborhood","Year_Built","Income_Level"]]
y = house[["Price"]]
x = pd.get_dummies(x, columns=["Neighborhood"])
print(x.columns)
# scaler = StandardScaler()
# x_scaled = scaler.fit_transform(x)
# y_scaled = scaler.fit_transform(y)
# print(x_scaled)
# print(y_scaled)
lreg = LinearRegression()
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=42)
# x_train,x_test,y_train,y_test = train_test_split(x_scaled,y_scaled,test_size=0.30,random_state=42)

lreg.fit(x_train,y_train)
y_pred = lreg.predict(x_test)

print("MAE:",mean_absolute_error(y_pred,y_test))
print("MSE:",mean_squared_error(y_pred,y_test))
print("RMSE:",root_mean_squared_error(y_pred,y_test))
print("-----------")
print("R2 Score:",r2_score(y_pred,y_test))
r = Ridge(alpha=0.3,random_state=42)
r.fit(x_train,y_train)
y_pred_r = r.predict(x_test)
print("MAE:",mean_absolute_error(y_pred_r,y_test))
print("MSE:",mean_squared_error(y_pred_r,y_test))
print("RMSE:",root_mean_squared_error(y_pred_r,y_test))
print("-----------")
print("R2 Score:",r2_score(y_pred_r,y_test))

l = Lasso(alpha=0.7)
l.fit(x_train,y_train)
y_pred_l = l.predict(x_test)
print("MAE:",mean_absolute_error(y_pred_l,y_test))
print("MSE:",mean_squared_error(y_pred_l,y_test))
print("RMSE:",root_mean_squared_error(y_pred_l,y_test))
print("-----------")
print("R2 Score:",r2_score(y_pred_l,y_test))

dtr = DecisionTreeRegressor(max_depth=4,splitter="random",min_samples_split=4,random_state=42)

dtr.fit(x_train,y_train)
y_pred_dtr = dtr.predict(x_test)
print("MAE:",mean_absolute_error(y_pred_dtr,y_test))
print("MSE:",mean_squared_error(y_pred_dtr,y_test))
print("RMSE:",root_mean_squared_error(y_pred_dtr,y_test))
print("-----------")
print("R2 Score:",r2_score(y_pred_dtr,y_test))
plt.figure(figsize=(10,12))
tree.plot_tree(dtr)
plt.show()
#shgowing feature vs their values
features = dtr.feature_importances_
plt.figure(figsize=(10,18))
plt.bar(x.columns,features)
plt.xlabel("Features")
plt.ylabel("Values ")
plt.title("Features vs Values")
plt.show()
rfr = RandomForestRegressor(max_depth=4,n_estimators=600,min_samples_split=4,random_state=42)

rfr.fit(x_train,y_train)
y_pred_rfr = rfr.predict(x_test)
print("MAE:",mean_absolute_error(y_pred_rfr,y_test))
print("MSE:",mean_squared_error(y_pred_rfr,y_test))
print("RMSE:",root_mean_squared_error(y_pred_rfr,y_test))
print("-----------")
print("R2 Score:",r2_score(y_pred_rfr,y_test))

svm = SVR(C=0.4,max_iter=230,kernel="linear")

svm.fit(x_train,y_train)

y_pred_svm = svm.predict(x_test)
print("MAE:",mean_absolute_error(y_pred_svm,y_test))
print("MSE:",mean_squared_error(y_pred_svm,y_test))
print("RMSE:",root_mean_squared_error(y_pred_svm,y_test))
print("-----------")
print("R2 Score:",r2_score(y_pred_svm,y_test))



knr = KNeighborsRegressor(n_neighbors=3)

knr.fit(x_train,y_train)
y_pred_knr = knr.predict(x_test)

print("MAE:",mean_absolute_error(y_pred_knr,y_test))
print("MSE:",mean_squared_error(y_pred_knr,y_test))
print("RMSE:",root_mean_squared_error(y_pred_knr,y_test))
print("-----------")
print("R2 Score:",r2_score(y_pred_knr,y_test))


square_feet = float(input("Entyer Square Feet:-"))
bedrooms = int(input("Enter No of Bedrooms:-"))
bathroom = float(input("Enter Bathrooms:-"))
neighborhood = input("Enter Downtown/Rural/ Rural/Suburbs/downtown:-")
year_built = int(input("Enter Year:-"))
income_level = int(input("Enter 0 Low 1 for Medium 2 for High -1 for Unknown:-"))

user_df = pd.DataFrame({
    "square_feet":[square_feet],
    "bedroom":[bedrooms],
    "Bathroom":[bathroom],
    "neighbourshood":[neighborhood],
    "Year_Built":[year_built],
    "Income_Level":[income_level]
})
user_df = pd.get_dummies(user_df,columns=["neighbourshood"])
user_df = user_df.reindex(columns=x.columns, fill_value=0)

output = lreg.predict(user_df)
print(output)