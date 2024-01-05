#automate using task scheduler
from misskey import Misskey;

instance = Misskey("misskey.io", i="sXqmDUjXOgGG2v8iilGNUASWK6V21CIj")


#post yayo note
yayo_Id = ["9o1viev5ntmd001b"] #replace with io file
new_note = instance.notes_create(file_ids=yayo_Id)
print(new_note["createdNote"]["id"]) #print note id

#file information
#getFile = instance.drive_files_show(url="https://media.misskeyusercontent.com/io/27b8d21f-30f6-4882-8616-f3e534ed8251.jpg")
#print(getFile)

#upload file
#with open("yayo.jpg", "rb") as f:
    #data = instance.drive_files_create(f)
#print(data["id"]) #print file id