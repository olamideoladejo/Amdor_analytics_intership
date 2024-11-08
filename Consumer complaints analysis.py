#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import neccesarry libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#load dataset
df = pd.read_excel('Consumer_Complaints.xlsx')


# In[3]:


#display the first five rows
df.head()


# In[3]:


#display column names
df.columns


# In[4]:


#display the shape of the dataframe
df.shape


# In[6]:


#display columns datatype
df.dtypes


# In[5]:


#check for columns with null values
df.isnull().sum()


# In[7]:


#handle missing data
#drop rows with missing values in Sub-product
df_Subproduct = df.dropna(subset = ["Sub-product"], inplace = True)


# In[8]:


#fill missing values in Sub-issue with not specified
df["Sub-issue"].fillna('Not specified', inplace = True)


# In[9]:


#fill missing values in Company public response not with in progress
df["Company public response"].fillna('N/A', inplace = True)


# In[10]:


#fill missing values in Timely response? with unknown 
df["Timely response?"].fillna('Unknown', inplace = True)


# In[11]:


#confirm if null values have been replaced
df.isnull().sum()


# In[12]:


#display unique values in the state column
df['State' ].unique()


# In[13]:


#create a dictionary with state codes and state names
state_names = {
    'NY': 'New York', 'FL': 'Florida', 'CA': 'California', 'VA': 'Virginia', 'TX': 'Texas', 
    'KS': 'Kansas', 'GA': 'Georgia', 'CT': 'Connecticut', 'OH': 'Ohio', 'NJ': 'New Jersey', 
    'IL': 'Illinois', 'MI': 'Michigan', 'NC': 'North Carolina', 'PA': 'Pennsylvania', 'WA': 'Washington', 
    'IN': 'Indiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'NV': 'Nevada', 'TN': 'Tennessee', 
    'AZ': 'Arizona', 'MO': 'Missouri', 'DC': 'District of Columbia', 'ID': 'Idaho', 'MS': 'Mississippi', 
    'CO': 'Colorado', 'OR': 'Oregon', 'MN': 'Minnesota', 'KY': 'Kentucky', 'AR': 'Arkansas', 
    'NH': 'New Hampshire', 'NM': 'New Mexico', 'UT': 'Utah', 'SC': 'South Carolina', 'AL': 'Alabama', 
    'DE': 'Delaware', 'OK': 'Oklahoma', 'LA': 'Louisiana', 'RI': 'Rhode Island', 'WI': 'Wisconsin', 
    'IA': 'Iowa', 'ME': 'Maine', 'WV': 'West Virginia', 'VT': 'Vermont', 'NE': 'Nebraska', 
    'SD': 'South Dakota', 'HI': 'Hawaii', 'AK': 'Alaska', 'MT': 'Montana', 'ND': 'North Dakota', 
    'WY': 'Wyoming'
}


# In[14]:


#replace stae codes with names
df['State'] = df['State'].map(state_names)


# In[15]:


#check if changes have been made
df['State' ].unique()


# In[17]:


#extract year,month from date submitted
df['Year'] = df['Date submitted'].dt.year
df['Month'] = df['Date submitted'].dt.month_name()


# In[38]:


#check if changes have been made
df.head()


# In[39]:


#top 3 submission channels
T3_submission_channels = df['Submitted via' ].value_counts().nlargest(3)

plt.figure(figsize =(10,6))
sns.barplot(x = T3_submission_channels.index, y = T3_submission_channels.values, palette = 'magma')
plt.title('Top 3 Submission Channels')
plt.xlabel('Submission Channel')
plt.ylabel('Count')
plt.show()


# In[18]:


#complaints over years
complaints_by_year = df.groupby('Year').size()#.plot(kind ='line')

plt.figure(figsize = (10,6))
sns.lineplot(x = complaints_by_year.index, y = complaints_by_year.values, marker = 'o', color = 'm')
plt.title('Compliants Over Years')
plt.xlabel('Year')
plt.ylabel('Total Compaints')
plt.show()



# In[21]:


#complaint by product
complaints_by_product = df.groupby('Product').size()


plt.figure(figsize = (10,6))
sns.barplot(x = complaints_by_product.values, y = complaints_by_product.index, palette = 'magma')
plt.title('Product Complaints')
plt.xlabel('Total Complaints')
plt.ylabel('Product')
plt.show()


# In[24]:


df['Product'].value_counts()


# In[25]:


#product by year
product_by_year = df.groupby(['Year', 'Product']).size().unstack()


product_by_year.plot(kind='bar', stacked=False, figsize=(12, 6), colormap='magma', width=0.8)
plt.title('Product Complaint  Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Complaints')
plt.legend(title='Complaint Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# In[26]:


#top 10 states
Top_states = df['State' ].value_counts().nlargest(10)

#plat top 10 states by complaints
plt.figure(figsize = (12,6))
sns.barplot(x = Top_states.index, y = Top_states.values, palette = 'magma')

#add titles and labels
plt.title('Top 10 States by Complaints')
plt.xlabel('State')
plt.ylabel('Total Complaints')
plt.show()


# In[27]:


df['State' ].value_counts()#.nlargest(10)


# In[28]:


# response timeliness count
response_timeliness = df['Timely response?'].value_counts()

# Plot response timeliness
plt.figure(figsize=(8, 5))
sns.countplot(x='Timely response?', data=df, palette='magma')

#add titles and labels
plt.title('Timeliness of Responses')
plt.xlabel('Timely Response')
plt.ylabel('Total Response')
plt.show()


# In[41]:


#Top ten issues ecountered by customers
top_issues = df['Issue'].value_counts().nlargest(10)

#plot issues by count
plt.figure(figsize = (10,6))
sns.barplot(x = top_issues.values, y = top_issues.index, palette = 'magma')

#add titles ana labels
plt.title('Top Issues')
plt.xlabel('Count')
plt.ylabel('Issues')
plt.show()


# In[53]:


#response to customer
private_response = df.groupby('Company response to consumer').size()

#plot company responses  to consumer by count
plt.figure(figsize = (12,6))
sns.barplot(x = private_response.values, y = private_response.index, palette = 'magma')

#add titles and labels
plt.title('Company  Response to Consumer')
plt.xlabel('Total')
plt.ylabel('Response')
plt.show()


# In[52]:


#public responses
public_response = df.groupby('Company public response').size()

#plot company public responses by count
plt.figure(figsize = (10,6))
sns.barplot(x = public_response.values, y = public_response.index, palette = 'magma')

#add titles and labels
plt.title('Company Public Response')
plt.xlabel('Total')
plt.ylabel('Response')
plt.show()


# In[42]:


#create list of months
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# define month column as an orderd categorical variable
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

#group complaints by months
complaints_by_month = df.groupby('Month').size()

#plot year by complaints
plt.figure(figsize = (12,6))
sns.barplot(x = complaints_by_month.index, y = complaints_by_month.values, palette = 'magma')

#add titles and labels
plt.title('Trends in Complaints over months')
plt.xlabel('Month')
plt.ylabel('Count')
plt.show()


# In[17]:


#Effectiveness of response over years
Yearly_timely_response = df.groupby(['Year', 'Timely response?']).size().unstack()

#plot yearly timely response
Yearly_timely_response.plot(kind='bar', stacked=False, figsize=(10, 6), colormap='magma', width=0.8)

#add titles and labels
plt.title('Trends in Response over the Years')
plt.xlabel('Year')
plt.ylabel('Number of REsponse')
plt.legend(title='Timely response?', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# In[54]:


df.to_excel('CleanedConsumerComplaints.xlsx', index=False)


# In[ ]:




