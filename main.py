#automated using task scheduler
from misskey import Misskey;

instance = Misskey("misskey.io", i="REPLACE WITH PERSONAL MISSKEY ACCESS TOKEN")


#post yayo note
yayo_Id = ["9o1viev5ntmd001b"] #replace with file id from misskey drive (differs per account)
new_note = instance.notes_create(file_ids=yayo_Id)
print(new_note["createdNote"]["id"]) #print note id

#file information - used to get file id
#getFile = instance.drive_files_show(url="IN MISSKEY, GO TO 'DRIVE', AND FIND FILE TO BE USED")
#print(getFile)
