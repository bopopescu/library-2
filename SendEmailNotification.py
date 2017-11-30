import smtplib


def send_notification(resume, jobid):

    try:
        fromaddr = 'rezumai@gmail.com'
        toaddrs = 'resumes@konectin.com'
        msg = resume+" | "+jobid
        username = 'rezumai@gmail.com'
        password = 'Gt153328@'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        return True

    except Exception as e:
        print(e)
        return False
