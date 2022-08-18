import pickle                   #For interacting with counter list.

print(pickle.load(open("./lurien/upload_counter.pickle","rb")))  #Print contents
counters=pickle.load(open("./lurien/upload_counter.pickle","rb"))#Load the counters from where they were left off.
counters[len(counters)]=1                                        #Add new counter to the list (Starts at 1)
pickle.dump(counters,open("./lurien/upload_counter.pickle","wb"))#Save the updated counters.
print(pickle.load(open("./lurien/upload_counter.pickle","rb")))  #Print contents