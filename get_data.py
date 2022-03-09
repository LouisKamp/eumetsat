# %%
import re
import shutil
import eumdac
import datetime
from dotenv import load_dotenv
import os
# %%
load_dotenv()

# %%
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")

credentials = (consumer_key, consumer_secret)

token = eumdac.AccessToken(credentials)

# %%
datastore = eumdac.DataStore(token)
selected_collection = datastore.get_collection("EO:EUM:DAT:MSG:HRSEVIRI")

# datastore.collections
# selected_collection.search_options

# %%

start = datetime.datetime(2022, 2, 9, 10, 0)
end = datetime.datetime(2022, 2, 9, 15, 0)

products = selected_collection.search(dtstart=start, dtend=end)

# %%

for product in products:
    files = list(product.entries)

    r = re.compile(".*\.nat")
    selected_product = list(filter(r.match, files))

    for file_to_download in selected_product:
        print(f"Downloading '{file_to_download}'")
        with product.open(entry=file_to_download) as source, open(f"./data/{source.name}", mode="wb") as destination:
            shutil.copyfileobj(source, destination)
            print("Download complete")

    # %%
