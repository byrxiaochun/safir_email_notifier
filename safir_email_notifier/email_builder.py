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
        'template_file': 'cloud_alarm_ok.ftl',
        'subject': _('B3LAB Safir Cloud Alarm State Change Notification')
    },    
    'billing_alarm': {
        'template_file': 'billing_alarm_notification.ftl',
        'subject': _('B3LAB Safir Cloud Credit Alarm Notification')
    },
    'billing_alarm_ok': {
        'template_file': 'billing_alarm_ok.ftl',
        'subject': _('B3LAB Safir Cloud Credit Alarm State Change Notification')
    },
    'billing_suspension_alarm': {
        'template_file': 'billing_suspension_notification.ftl',
        'subject': _('B3LAB Safir Cloud Project Suspension Notification')
    },
    'billing_suspension_ok': {
        'template_file': 'billing_suspension_ok.ftl',
        'subject': _('B3LAB Safir Cloud Project Activation Notice')
    },
    'billing_termination_alarm': {
        'template_file': 'billing_termination_notification.ftl',
        'subject': _('B3LAB Safir Cloud Project Termination Notification')
    },
    'billing_termination_ok': {
        'template_file': 'billing_termination_ok.ftl',
        'subject': _('B3LAB Safir Cloud Project Re-activation Notification')
    },
    'billing_weekly_report': {
        'template_file': 'billing_weekly_report.ftl',
        'subject': _('B3LAB Safir Cloud Weekly Usage Report')
    },
    'error_notification': {
        'template_file': 'error_notification.ftl',
        'subject': _('B3LAB Safir Cloud Billing Operation Error')
    }
}


class EmailBuilder:
    def __init__(self, mail_subject):
        if mail_subject not in MAIL_TEMPLATES:

            error = mail_subject + ' is not in mail template list : '.join(MAIL_TEMPLATES)
            raise Exception(error)
        self.mail_template = MAIL_TEMPLATES[mail_subject]

    def get_mail_content(self, data):
        """
        Prepares Email content
        :param data: Args dictionary

        Example usage:
        data = {
            'name': name,
            'link': link,
            'instance_name':instance_name,
            'action_type':action_type,
            'last_credit_load_time':last_credit_load_time,
            'last_credit_update_time':last_credit_update_time,
            'credit':credit,
            'warning_threshold':warning_threshold,
            'suspension_threshold':suspension_threshold,
            'termination_threshold':termination_threshold,
            'reason':reason
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
