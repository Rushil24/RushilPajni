import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('rushilpajni2@gmail.com', 'srtxyyvhdkliyosy')
conn.sendmail('rushilpajni2@gmail.com', 'rp2testserver@gmail.com', 'Subject: So Long.....\n\nDear Rushil,\nSo Long No See\nHope Everything Is Fine\n\n\n-Pappu Shetty')
conn.quit()