import imapclient
connect = imapclient.IMAPClient('imap.gmail.com', ssl=True)
connect.login('rushilpajni2@gmail.com', 'srtxyyvhdkliyosy')
connect.select_folder('INBOX', readonly=False)
a = connect.list_folders()
UIDs = connect.search(['ON' ,'28-JUL-2021'])
print(UIDs)
#connect.delete_messages([691]) #that deletes messages