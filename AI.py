import requests
import time
b=0
def classify(text):
    

    key = "a8eb5ae0-abf0-11ec-a84c-156df83a040c01ab5984-358e-4c44-a123-fd51c08d6e9d"

    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"

    response = requests.get(url, params={"data": text})

    for x in response.json():


        label=x["class_name"]

        confidence=x["confidence"]

        print(str(label) + " with " + str(confidence) + "% confidence")


i=str(input("What do you see around you?     "))
b=time.time()
print("")
classify(i)


e=time.time()
print("")
print("The programe took "+str(e-b)+" Seconds")
