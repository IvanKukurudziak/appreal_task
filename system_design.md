# Design Task

### Description
Currently, we receive an entire customer catalog on an hourly basis. In each run, we scan
all products in the catalog. For every product, we process the image through our algorithm,
fetching the AI tags for the image. Then, we write the catalog data, with the newly
calculated AI tags, into the Elastic Search database. So, each run creates a new index,
which is a production index. We use this index to search for customers' products.

### Problem
The process described above is not ideal and undoubtedly not efficient. Usually, not all
products change from one indexing to another. Some stay the same, and some have small
changes—like changes in price and in_stock count. Other products have changes in the
images themselves. And, of course, new items are added, and some items no longer exist
in the catalog but did exist in the previous version.

### Your task
Please describe a flow that will make the whole process more efficient. For example - we
don’t want to process products we indexed before and didn’t change.
Please describe any tools, data structures, or other resources you think can help.
Remember that customers rely on the production index, so we should avoid modifying or
overloading it with read/write actions.



## Solution
Mitigate writes operation on prod existing index
1. Avoids unnecessary writes to Elasticsearch. Use cache approach
   On each run, can crate the unique document hash, based on the search fields, stored by the catalog document id, with TTL up to 1 hr or to the next day. 
   Check, incase the document hash is the same  in cache (Redis), don't update it to the Elasticsearch
2. Use bulk write operation, improves Elasticsearch performance instead of multiple single write operations.
3. Based on the stored cache info cache storage, will know the document need to be deleted (use bulk as well) 


#### Alternative
Use Elasticsearch index aliases, in case ALL the catalog data is updated on each run
1. Create a new index on each catalog process event.
2. Write all the data to new index, preform to using bulk operations
3. After data insert is done, swap the prod index with new one

