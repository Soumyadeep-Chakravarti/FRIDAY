import speech_recognition as s_r

list1 = s_r.Microphone.list_microphone_names()#print all the microphones connected to your machine

print(list1)
print("done")