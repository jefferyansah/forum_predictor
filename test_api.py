import requests as r


question = 'How many days does it takes the earth to go around the sun?'

keys= {'question': question}


prediction = r.get("http://127.0.0.1:8000/predict-forum", params=keys)


results = prediction.json()

print(results)
# print(results["Prediction"])
# print(results["Probability"])