import os
import pandas as pd
import openai
data = pd.read_csv("dialogue.csv")
data
data.head(10)
data.dropna(inplace = True) 
data = data.drop_duplicates()
data
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stpwrds = set(stopwords.words('english'))
def clean_text(text):
  new_text = [word for word in text.split(" ") if word not in stpwrds]
  return " ".join(new_text)
import re
open("data.json", "w").close()
import json
test = []

old_id = 0

d= dict()
i = 0
with open("data.json", 'a') as f:
    while(i<=data.shape[0]):       
      new_id = data.loc[i]["ID"] 
      st = "{\"prompt\": \"" 
      new_data = data[data["ID"]==new_id]
      prom = clean_text(new_data["question"].values[0])
      st = "{\"prompt\": \"" + prom + "\\n\\n###\\n" 
      for ids in range(new_data.shape[0]): 
        if ids == 0:
          st+= "\\nCustomer: " + new_data.iloc[ids]["question"] +"\\nAgent: "
          st+="\""
          st+= ","+"\"completion\""+":"+"\" " +new_data.iloc[ids]["response"]+"\\n\""
          st+="}"
          st+="\n"
          f.write(st)
        else: 
          st = "{\"prompt\": \"" + prom + "\\n\\n###\\n" 
          for sub_ids in range(ids+1):
            if sub_ids==0:
              st += "\\nCustomer: " + new_data.iloc[sub_ids]["question"] +"\\nAgent: "+new_data.iloc[sub_ids]["response"]+"\\n" 
            elif sub_ids!=ids:
              st += "Customer: " + new_data.iloc[sub_ids]["question"] +"\\nAgent: "+new_data.iloc[sub_ids]["response"]+"\\n" 
            else:
              st+= "Customer: " + new_data.iloc[ids]["question"] +"\\nAgent: "
              st+="\""
              st+= ","+"\"completion\""+":"+"\" " +new_data.iloc[ids]["response"]+"\\n\""
              st+="}"
              st+="\n"
              f.write(st)

        i+=1 

openai.api_key = "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"
os.environ["OPENAI_API_KEY"] = "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"
completion = openai.Completion()
question = "can i preorder a playstation"
prom = f'\nCustomer: {question}\nAgent:' 
print(prom)
# print(prom)
response = completion.create( 
    model = <ID OF TRAINED MODEL>,
    prompt = prom,stop = ["\nCustomer"],temperature = 0.3,
      top_p =1,best_of=1,
      max_tokens=150
)
# print(response)
print(response.choices[0].text.strip()) 
