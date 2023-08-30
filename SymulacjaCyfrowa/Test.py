from GenerateEvent import GenerateEvent
from Network import Network 
from sortedcontainers import SortedList
from RandomNumberGenerator import RandomNumberGenerator 
from statistics import mean 
import pandas

data = {'Operator':[],
        'Data':[]}

dataframe = pandas.DataFrame(data)

for i in range(5):
    new_row = {'Operator': i, 'Data':i * 4 + 2}
    # new_row = {'Operator': i, 'Data':i * 4 + 2}
    dataframe = dataframe._append(new_row, ignore_index=True)

dataframe.to_excel("test.xlsx", sheet_name="Sheet #", startrow=0, startcol=0)
print(dataframe)

# _lambda = 1.5
# generator = RandomNumberGenerator(_lambda)

# v = []
# s1 = []
# tau = []
# maxUsersNumber = 400
# n = 60

# seed = 100000 * maxUsersNumber

# for i in range(maxUsersNumber + n):
#     tau.append(generator.randExp2(seed))
#     seed = seed + 50000
#     v.append(0.005 + 0.045 * generator.rand(seed)) # [5,50]m/s
#     seed = seed + 50000
#     s1.append(generator.randGauss(0, 4))
    
# #print(tau)
# print(mean(tau))
# print(mean(v))
# print(mean(s1))


# # x=2999
# # l=5000

# # powerBS1 = 4.56 - 22 * math.log10(x)
# # powerBS2 = 4.56 - 22 * math.log10(l - x)

# # print(powerBS1)
# # print(powerBS2)
# # print(math.log10(x))
# # print(math.log10(l - x))
# # print(powerBS2 - powerBS1)

# # powerBS1 = 4.56 - 22 * math.log10(x) - 8.5
# # powerBS2 = 4.56 - 22 * math.log10(l - x) + 8.5

# # print(powerBS1)
# # print(powerBS2)
# # print(powerBS2 - powerBS1)



                  