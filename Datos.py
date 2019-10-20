import requests
import json
temp=[]
cloud=[]
humidity=[]
res=[]
for i in range(-90,90,10):
    for j in range(-180,180,10):
        response = requests.get("http://api.weatherstack.com/current?access_key=4dd1a884407a4df6d2a4ba2af6a40019&query="+str(i)+","+str(j))
        print(response.status_code)
        x = response.json()
        print(x)
        temp.append(x['current']['temperature'])
        cloud.append(x['current']["cloudcover"])
        humidity.append(x['current']["humidity"])

#print(temp)
#print(cloud)
#print(humidity)

shading1=[100,100,90,80,70,60,50,40,40,30,30,30,20,20,20,10],[100,90,80,70,60,60,50,40,40,30,30,20,20,20,10,10],[100,90,80,70,60,50,50,40,30,30,30,20,20,20,10,10],[100,90,80,70,60,50,40,40,30,30,20,20,20,20,10,10],[100,80,70,60,60,50,40,40,30,30,20,20,20,10,10,10],[90,80,70,60,50,50,40,30,30,30,20,20,20,10,10,10],[90,80,70,60,50,40,40,30,30,20,20,20,10,10,10,10],[90,80,70,60,50,40,40,30,30,20,20,20,10,10,10,10],[90,70,60,60,50,40,40,30,30,20,20,20,10,10,10,10]
shading2=[100,100,80,70,60,60,50,40,40,30,30,20,20,20,20,10],[100,90,80,70,60,50,50,40,40,30,30,20,20,20,10,10],[100,90,80,70,60,50,40,40,30,30,30,20,20,20,10,10],[100,90,80,70,60,50,40,40,30,30,20,20,20,10,10,10],[100,80,70,60,50,50,40,40,30,30,20,20,20,10,10,10],[90,80,70,60,50,50,40,30,30,20,20,20,20,10,10,10],[90,80,70,60,50,40,40,30,30,20,20,20,10,10,10,10],[90,80,70,60,50,40,40,30,30,20,20,20,10,10,10,10],[80,70,60,50,50,40,30,30,20,20,20,10,10,10,10,10]
shading3=[100,90,80,70,60,50,50,40,40,30,30,20,20,20,10,10],[100,90,80,70,60,50,50,40,30,30,30,20,20,20,10,10],[100,80,80,70,60,50,40,40,30,30,20,20,20,10,10,10],[100,80,70,60,60,50,40,40,30,30,20,20,20,10,10,10],[90,80,70,60,50,50,40,30,30,30,20,20,20,10,10,10],[90,80,70,60,50,40,40,30,30,20,20,20,10,10,10,10],[90,80,70,6,50,40,40,30,30,20,20,20,10,10,10,10],[90,70,60,50,50,40,30,30,30,20,20,20,10,10,10,10],[80,70,60,50,50,40,30,30,20,20,20,10,10,10,10,10]
shading4=[100,90,80,70,60,50,50,40,30,30,30,20,20,20,10,10],[100,90,80,70,60,50,40,40,30,30,20,20,20,20,10,10],[100,80,70,60,60,50,40,40,30,30,20,20,20,10,10,10],[100,80,70,60,60,50,40,30,30,30,20,20,20,10,10,10],[90,80,70,60,50,40,40,30,30,20,20,20,10,10,10,10],[90,80,70,60,50,40,40,30,30,20,20,20,10,10,10,10],[90,70,60,60,50,40,40,30,30,20,20,20,10,10,10,10],[90,70,60,50,50,40,30,30,20,20,20,10,10,10,10,10],[80,70,60,50,40,40,30,30,20,20,20,10,10,10,10,10]

for k in range(0,len(cloud)):
    if (cloud[k]==0 and humidity[k]==0 and temp[k]==0):
        res.append(0)
    elif cloud[k]<=10:
        if temp[k]>=((110-32)/1.8):
            if round(humidity[k]*17/100)<2:
                res.append=shading1[0][0]
            else:
                w = round(humidity[k]*17/100)
                res.append(shading1[0][w-2])
        elif (temp[k]<=((109-32)/1.8) and temp[k]>=((100-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading1[1][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading1[1][w-2])
                print(4)
        elif (temp[k]<=((99-32)/1.8) and temp[k]>=((90-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading1[2][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading1[2][w-2])
                print(6)
        elif (temp[k]<=((89-32)/1.8) and temp[k]>=((80-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading1[3][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading1[3][w-2])
        elif (temp[k]<=((79-32)/1.8) and temp[k]>=((70-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading1[4][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading1[4][w-2])
        elif (temp[k]<=((69-32)/1.8) and temp[k]>=((60-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading1[5][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading1[5][w-2])
        elif (temp[k]<=((59-32)/1.8) and temp[k]>=((50-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading1[6][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading1[6][w-2])
        elif (temp[k]<=((49-32)/1.8) and temp[k]>=((40-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading1[7][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading1[7][w-2])
        elif (temp[k]<=((39-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading1[8][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading1[8][w-2])
    elif cloud[k]>10 and cloud[k]<=50:
        if temp[k]>=((110-32)/1.8):
            if round(humidity[k]*17/100)<2:
                res.append(shading2[0][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading2[0][w-2])
        elif (temp[k]<=((109-32)/1.8) and temp[k]>=((100-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading2[1][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading2[1][w-2])
        elif (temp[k]<=((99-32)/1.8) and temp[k]>=((90-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading2[2][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading2[2][w-2])
        elif (temp[k]<=((89-32)/1.8) and temp[k]>=((80-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading2[3][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading2[3][w-2])
        elif (temp[k]<=((79-32)/1.8) and temp[k]>=((70-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading2[4][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading2[4][w-2])
        elif (temp[k]<=((69-32)/1.8) and temp[k]>=((60-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading2[5][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading2[5][w-2])
        elif (temp[k]<=((59-32)/1.8) and temp[k]>=((50-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading2[6][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading2[6][w-2])
        elif (temp[k]<=((49-32)/1.8) and temp[k]>=((40-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading2[7][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading2[7][w-2])
        elif (temp[k]<=((39-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading2[8][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading2[8][w-2])
    elif cloud[k]>50 and cloud[k]<=90:
        if temp[k]>=((110-32)/1.8):
            if round(humidity[k]*17/100)<2:
                res.append(shading3[0][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading3[0][w-2])
        elif (temp[k]<=((109-32)/1.8) and temp[k]>=((100-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading3[1][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading3[1][w-2])
        elif (temp[k]<=((99-32)/1.8) and temp[k]>=((90-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading3[2][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading3[2][w-2])
        elif (temp[k]<=((89-32)/1.8) and temp[k]>=((80-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading3[3][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading3[3][w-2])
        elif (temp[k]<=((79-32)/1.8) and temp[k]>=((70-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading3[4][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading3[4][w-2])
        elif (temp[k]<=((69-32)/1.8) and temp[k]>=((60-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading3[5][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading3[5][w-2])
        elif (temp[k]<=((59-32)/1.8) and temp[k]>=((50-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading3[6][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading3[6][w-2])
        elif (temp[k]<=((49-32)/1.8) and temp[k]>=((40-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading3[7][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading3[7][w-2])
        elif (temp[k]<=((39-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading3[8][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading3[8][w-2])
    elif cloud[k]>90:
        if temp[k]>=((110-32)/1.8):
            if round(humidity[k]*17/100)<2:
                res.append(shading4[0][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading4[0][w-2])
        elif (temp[k]<=((109-32)/1.8) and temp[k]>=((100-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading4[1][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading4[1][w-2])
        elif (temp[k]<=((99-32)/1.8) and temp[k]>=((90-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading4[2][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading4[2][w-2])
        elif (temp[k]<=((89-32)/1.8) and temp[k]>=((80-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading4[3][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading4[3][w-2])
        elif (temp[k]<=((79-32)/1.8) and temp[k]>=((70-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading4[4][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading4[4][w-2])
        elif (temp[k]<=((69-32)/1.8) and temp[k]>=((60-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading4[5][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading4[5][w-2])
        elif (temp[k]<=((59-32)/1.8) and temp[k]>=((50-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading4[6][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading4[6][w-2])
        elif (temp[k]<=((49-32)/1.8) and temp[k]>=((40-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading4[7][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading4[7][w-2])
        elif (temp[k]<=((39-32)/1.8)):
            if round(humidity[k]*17/100)<2:
                res.append(shading4[8][0])
            else:
                w = round(humidity[k]*17/100)
                res.append(shading4[8][w-2])
print(res)