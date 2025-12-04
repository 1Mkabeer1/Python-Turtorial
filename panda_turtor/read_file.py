# with open("demofile.txt") as file:
#   print(file.read())

# with open("demofile.txt", "a") as f:
#   f.write("Now the file has more content!")

# #open and read the file after the appending:
# with open("demofile.txt") as f:
#   print(f.read())
import pandas as pd

datas = pd.read_csv("new.csv", sep=';')
# print(datas['name'])
data_dict = datas.to_dict()

# print(datas[datas.s_no == 5])
# print(datas[datas.s_no == datas.s_no.max()])

max_data = datas[datas.s_no == datas.s_no.max()]

print(max_data.name)

# list_acct = datas['acct_no'].to_list()
# print(len(list_acct))

# for data in datas:
#     print(f'my {data.bank_name} is {data.acct_no} ')