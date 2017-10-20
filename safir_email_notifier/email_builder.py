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

import gettext
from jinja2 import Environment, FileSystemLoader
import os

PATH = os.path.dirname(os.path.abspath(__file__))
localedir = os.path.join(PATH, 'locale')
DEFAULT_LANG = 'tr'

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(
            PATH,
            './templates/' + DEFAULT_LANG)),
        trim_blocks=False)

try:
    lang = gettext.translation('email_builder',
                               localedir=localedir,
                               languages=[DEFAULT_LANG])
except KeyError:
    lang = gettext.translation('email_builder',
                               localedir=localedir)

lang.install()
_ = lang.ugettext

MAIL_TEMPLATES = {
    'user_activation': {
        'template_file': 'cloud_user_activation.ftl',
        'subject': _('B3LAB Safir Cloud Account Activation Mail')
    },
    'reset_password': {
        'template_file': 'cloud_reset_password.ftl',
        'subject': _('B3LAB Safir Cloud Reset Password')
    },
    'alarm_alarm': {
        'template_file': 'cloud_alarm_alarm.ftl',
        'subject': _('B3LAB Safir Cloud Alarm Notification')
    },
    'alarm_ok': {
        'template_file': 'cloud_reset_password.ftl',
        'subject': _('B3LAB Safir Cloud Alarm State Change Notification')
    }
}


class EmailBuilder:
    def __init__(self, mail_subject):
        if mail_subject not in MAIL_TEMPLATES:
            raise
        self.mail_template = MAIL_TEMPLATES[mail_subject]

    def get_mail_content(self, data):
        """
        Prepares Email content
        :param data: Args dictionary

        Example usage:
        data = {
            'name': name,
            'link': link
        }
        :return: subject, text, html
        """
        subject = self.mail_template['subject']
        html = self.render_template(self.mail_template['template_file'],
                                    data)
        text = data['link']

        return subject, text, html

    @staticmethod
    def render_template(filename, context):
        return TEMPLATE_ENVIRONMENT.get_template(
            filename).render(context)
