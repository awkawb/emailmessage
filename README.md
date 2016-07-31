Description
===========
This package is a simple way to create and send email messages.

API Usage
=========
    >>> from emailmessage import EmailMessage
    >>> mesg = EmailMessage("sender@mail.com", "receiver@mail.com",
    ...     "Subject Line", "Email Body", "gmail")
    >>> mesg.login("mypassword")
    >>> mesg.send()
