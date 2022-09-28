from ast import For
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv, pandas as pd

# Use a service account.
cred = credentials.Certificate('your_firebase_admin_key_file.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

group_a_ref = db.collection(u'firestore_collection').document(u'firestore_document')
docs = group_a_ref.collection(u'firestore_sub_collection').stream()

collection_list = []

for doc in docs:
    collection_list.append(doc.to_dict())

collection_df = pd.DataFrame(collection_list)
collection_df.index += 1

for i in range(1,len(collection_df)):
    if type(collection_df['dataframe_column_name'][i]) == list:
        for column in collection_df['dataframe_column_name'][i]:  
            column_index = collection_df['dataframe_column_name'][i].index(column)
            if column == "Au5xR4YD8mfoMLsZO6it":
                collection_df['dataframe_column_name'][i][column_index] = collection_df['duties'][i][column_index].replace("Au5xR4YD8mfoMLsZO6it", "ディレクター")
            elif column == "EmHW1I8aOJv3ef5l9Why":
                collection_df['dataframe_column_name'][i][column_index] = collection_df['duties'][i][column_index].replace("EmHW1I8aOJv3ef5l9Why", "ドメイン")
            elif column == "NTHF1EzrIjY348IUWD7d":
                collection_df['dataframe_column_name'][i][column_index] = collection_df['duties'][i][column_index].replace("NTHF1EzrIjY348IUWD7d", "オンサイト")
            elif column == "OGSxCCJNITucPPEcZzjn":
                collection_df['dataframe_column_name'][i][column_index] = collection_df['duties'][i][column_index].replace("OGSxCCJNITucPPEcZzjn", "エンジニア")
            elif column == "phfRDnUwo2ohlQs6vRbg":
                collection_df['dataframe_column_name'][i][column_index] = collection_df['duties'][i][column_index].replace("phfRDnUwo2ohlQs6vRbg", "その他サービ")
            elif column == "zG7xjdK2GvyMuhJSlNEL":
                collection_df['dataframe_column_name'][i][column_index] = collection_df['duties'][i][column_index].replace("zG7xjdK2GvyMuhJSlNEL", "デザイナー")
            elif column == "zwAyUruge91v7lS1GPjB":
                collection_df['dataframe_column_name'][i][column_index] = collection_df['duties'][i][column_index].replace("zwAyUruge91v7lS1GPjB", "サーバー")

collection_df.to_csv('mycsvfile.csv', encoding='utf-8')
