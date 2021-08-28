import imapclient
connect = imapclient.IMAPClient('imap.gmail.com', ssl = True)
#ssl allows for the authentication, encryption and decryption of data sent over the Internet 
connect.login('rushilpajni2@gmail.com', 'srtxyyvhdkliyosy')
connect.select_folder('INBOX',readonly=True)
select_info = connect.select_folder('INBOX')
#print('%d messages in INBOX' % select_info[b'EXISTS'])
#a = connect.search(['SINCE','20-AUG-2020'])
rawMessage = connect.fetch([690], ['BODY[]','FLAGS'])
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[690][b'BODY[]'])
b = message.get_subject() #subject will be printed
c = message.get_addresses('from') #this will print who sent the mail
d = message.get_addresses('to') #this will print who was mail sent to
e = message.get_addresses('bcc') #this will print who was in the bcc 
f = message.text_part.get_payload().decode('UTF-8') #this will print the body of the mail
#print(a)
#print(b)
#print(c)
#print(d)
#print(e)
print(f)

