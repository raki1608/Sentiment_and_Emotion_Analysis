from textblob import TextBlob
t=input("enter the sentence ")
a=TextBlob(t)
print(a.tags)
print(a.words)
a.sentiment