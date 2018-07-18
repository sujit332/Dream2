
st_name= input("Enter State Name")

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                       'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                       'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

for x,y in state_dictionary.items():
    if x==st_name:
        print("Capital is:",y)
        break
    else:
        print(state_dictionary.get("Washing","Capital Not Found"))
        break
