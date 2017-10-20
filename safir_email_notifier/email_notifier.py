# Copyright 2017 TUBITAK B3LAB
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailNotifier:

    def __init__(self, smtp_server, smtp_port,
                 login_addr, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.login_addr = login_addr
        self.password = password

    def connect(self):
        self.mailserver = smtplib.SMTP(self.smtp_server, self.smtp_port)
        # identify ourselves to smtp client
        self.mailserver.ehlo()
        # secure our email with tls encryption
        self.mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        self.mailserver.ehlo()
        self.mailserver.login(self.login_addr, self.password)

    def disconnect(self):
        self.mailserver.quit()

    def send_mail(self, to_list, subject, text, html, files=None):

        try:
            self.connect()
            msg = MIMEMultipart('alternative')
            msg['From'] = self.login_addr
            msg['To'] = to_list
            msg['Subject'] = subject

            textpart = MIMEText(text, 'plain', 'utf-8')
            htmlpart = MIMEText(html, 'html', 'utf-8')

            msg.attach(textpart)
            msg.attach(htmlpart)

            for f in files or []:
                with open(f, "rb") as fil:
                    part = MIMEApplication(
                            fil.read(),
                            Name=basename(f)
                    )
                    part['Content-Disposition'] = \
                        'attachment; filename="%s"' % basename(f)
                    msg.attach(part)

            self.mailserver.sendmail(self.login_addr,
                                     to_list,
                                     msg.as_string())
        except Exception as ex:
            print('ERROR: Email notification not sent. ' + ex.message)
        finally:
            self.disconnect()
