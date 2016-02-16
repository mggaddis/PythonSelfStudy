
# coding: utf-8

# In[ ]:

import requests
import pandas as pd
import StringIO


# In[ ]:

r = requests.get("https://data.consumerfinance.gov/api/views/s6ew-h6mp/rows.csv?accessType=DOWNLOAD")


# In[ ]:

new_csv = "\n".join(r.content.split("\n")[1:1000])


# In[ ]:

df = pd.read_csv(StringIO.StringIO(new_csv))


# In[ ]:

df.describe


# In[ ]:



