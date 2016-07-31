#!/usr/bin/env python3

class EmailMessage:
    """ Configure an email message/server to send an email.

    Usage
    =====
        mesg = EmailMessage("sender@mail.com", "receiver@mail.com",
            "Subject Line", "Email Body", "gmail")
        mesg.login("mypassword")
        mesg.send()
    """

    def __init__(self, from_addr="", to_addr="", subj="", body="",
            service="gmail"):
        """ Configure an email message/server to send an email. """
        mesg_header = {}
        mesg_header["To"] = to_addr
        mesg_header["From"] = from_addr
        mesg_header["Subject"] = subj

        self.email_mesg = self._get_email_mesg(mesg_header, body)

        self.server = self._get_server(service)

    def _get_email_mesg(self, header, body):
        """ Return an email message.

        Create an email message object from the provided header and body
        and return the email message object.

        Params
        ======
            header: Dictionary contain email message header contents.
            body: Either a string or a file containing the body of the message.

        Return
        ======
            A valid email message object ready to send via SMTP.
        """
        from email.message import Message

        mesg = Message()
        for h,v in self.mesg_header.items():
            mesg.add_header(h, v)

        mesg.set_payload(self.mesg_body)

        return mesg

    def _get_server(self, service):
        """ Return a email server object.

        Provided a service, create an email server object and return the object
        to the caller. The server object is returned in a state which is ready
        for the user to login to the server.

        Params
        ======
            service: A string representing the service to send the email with.
                The current valid services this module supports are:
                    * "gmail": Google's mail service

        Return
        ======
            An email server object ready for the user to login to.
        """
        if service == "gmail":
            server_addr = "smtp.gmail.com"
            server_port = 587

            import smtplib
            server = smtplib.SMTP(server_addr, server_port)

        return server

    def login(self, password):
        """ Login to the class server object.

        Params
        ======
            password: String with the users password to login to the server.
        """
        self.server.starttls()
        self.server.login(self.email_mesg.get("From"), password)

    def send(self):
        """ Send the email message using the setup server object.

        After an email message object and email server object have been
        instantiated, use this method to send the email message using the
        configured email server.
        """
        self.server.sendmail(self.email_mesg.get("From"),
            self.email_mesg.get("To"),
            self.email_mesg.as_string())

