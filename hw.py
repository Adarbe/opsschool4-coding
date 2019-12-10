import json

sorted_buckets = {}
data_dict = {}
def get_sorted_range():
    return sorted(data_dict["buckets"])

with open("hw.json") as json_data:
    data_dict = json.load(json_data)
    print(data_dict)
    sorted_buckets = get_sorted_range()

def if_in_range(min_age, max_age, age):
    return min_age <= age <= max_age


for name, age in data_dict["ppl_ages"].items():
        for i in range(0,len(sorted_buckets)):
            if i = 0 and len



