from ast import For
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv, pandas as pd

# Use a service account.
cred = credentials.Certificate('kostritzer-10dce-915ac49343a8.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

group_a_ref = db.collection(u'groups').document(u'81T1vrpykrEBZlO9zPcl')
docs = group_a_ref.collection(u'members').stream()

collection_list = []

for doc in docs:
    collection_list.append(doc.to_dict())

collection_df = pd.DataFrame(collection_list)
collection_df.index += 1
# if collection_df['duties'][1][0] == "OGSxCCJNITucPPEcZzjn":
#     collection_df['duties'][1][0] = collection_df['duties'][1][0].replace("OGSxCCJNITucPPEcZzjn", "エンジニア")

# if docs.exists:
    # with open('mycsvfile.csv', 'w', encoding="utf-8") as f: 
    #     w = csv.DictWriter(f, my_dict.keys())
    #     w.writeheader()
    #     w.writerow(my_dict)
# else:
    # print(u'No such document!')

for i in range(1,len(collection_df)):
    if type(collection_df['duties'][i]) == list:
        for column in collection_df['duties'][i]:  
            column_index = collection_df['duties'][i].index(column)
            if column == "Au5xR4YD8mfoMLsZO6it":
                collection_df['duties'][i][column_index] = collection_df['duties'][i][column_index].replace("Au5xR4YD8mfoMLsZO6it", "ディレクター")
            elif column == "EmHW1I8aOJv3ef5l9Why":
                collection_df['duties'][i][column_index] = collection_df['duties'][i][column_index].replace("EmHW1I8aOJv3ef5l9Why", "ドメイン")
            elif column == "NTHF1EzrIjY348IUWD7d":
                collection_df['duties'][i][column_index] = collection_df['duties'][i][column_index].replace("NTHF1EzrIjY348IUWD7d", "オンサイト")
            elif column == "OGSxCCJNITucPPEcZzjn":
                collection_df['duties'][i][column_index] = collection_df['duties'][i][column_index].replace("OGSxCCJNITucPPEcZzjn", "エンジニア")
            elif column == "phfRDnUwo2ohlQs6vRbg":
                collection_df['duties'][i][column_index] = collection_df['duties'][i][column_index].replace("phfRDnUwo2ohlQs6vRbg", "その他サービ")
            elif column == "zG7xjdK2GvyMuhJSlNEL":
                collection_df['duties'][i][column_index] = collection_df['duties'][i][column_index].replace("zG7xjdK2GvyMuhJSlNEL", "デザイナー")
            elif column == "zwAyUruge91v7lS1GPjB":
                collection_df['duties'][i][column_index] = collection_df['duties'][i][column_index].replace("zwAyUruge91v7lS1GPjB", "サーバー")

# collection_df.to_csv('mydutiescsvfile.csv', encoding='utf-8')
collection_df.to_csv('mycsvfile.csv', encoding='utf-8')