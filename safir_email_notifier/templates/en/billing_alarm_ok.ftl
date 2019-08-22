<!DOCTYPE html>
<html>
<head lang="tr">
    <meta charset="UTF-8">
    <title>Safir Cloud Alarm Notification</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,700,900" rel="stylesheet">
</head>
<body style="margin: 0;">

<div class="wrapper">
    <table cellpadding="0" cellspacing="0"
           style="width: 640px; height: 100%; border: 0; margin: 0 auto; background-color: #f5f5f5;">
        <tbody>
        <tr>
            <td>
                <table style="width: 100%; height: 100%; text-align: center; padding: 5px;">
                    <tbody>
                    <tr>
                        <td>
                            <table cellpadding="0" cellspacing="0" width="100%" style="height: 100%; padding: 40px;">
                                <tbody>
                                <tr>
                                    <td align="center">
                                        <table cellpadding="0" cellspacing="0" width="100%" height="60" bgcolor="#fff">
                                            <tbody>
                                            <tr>
                                                <td>&nbsp;</td>
                                                <td bgcolor="#007500"
                                                    style="padding: 2px 68px 2px 68px;-webkit-border-radius: 6px;border-radius: 6px;border: 0;">
                                                    <p style="margin-top: 20px; color: #ffffff; font-size: 20px; font-family: 'Roboto', helvetica, arial, sans-serif; font-weight: 600;">
                                                        Safir Cloud Credit Alarm State Change</p>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td><p>&nbsp;</p></td>
                                            </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <table cellpadding="0" cellspacing="0" width="100%"
                                               style="height: 100%; text-align: left; background-color: #fff; padding: 0 60px;">
                                            <tbody>
                                            <tr>
                                                <td>
                                                    <p style="margin-top: 0; margin-bottom: 15px; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 400;">
                                                        Hi {{ name }}</p>
                                                    <p style="margin-top: 0; margin-bottom: 15px; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 400;">
                                                        The instance {{ instance_name }} of your account was giving credit alarm but it's state is now <b>back to normal</b></p>


<p style="margin-top: 0; margin-bottom: 20px; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 400;">
                                                        Alarm Resource: {{ instance_name }}</p><br>
                                                    <p style="margin-top: 0; margin-bottom: 0; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 400;">
                                                        Last Credit Load Time: {{ last_credit_load_time }}</p><br>
                                                    <p style="margin-top: 0; margin-bottom: 0; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 400;">
                                                        Credit: {{ credit }}</p><br>
                                                    <p style="margin-top: 0; margin-bottom: 20px; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 400;">
                                                        Action: <b>{{ action_type }}</b></p><br>

                                                    <p style="margin-top: 0; margin-bottom: 0; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 600;">
                                                        Defined Limites</p><br>

                                                    <p style="margin-top: 0; margin-bottom: 0; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 400;">
                                                        Warn Treshold Value: {{ warning_threshold }}</p>
                                                    <p style="margin-top: 0; margin-bottom: 0; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 400;">
                                                        Suspension Treshold Value: {{ suspension_threshold }}</p>
                                                    <p style="margin-top: 0; margin-bottom: 0; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 400;">
                                                        Termination Treshold Value: {{ termination_threshold }}</p><br>

                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0"
                                                           style="border: 0;">
                                                        <tbody>
                                                        <tr>
                                                            <td style="border: 0;">
                                                                <table border="0" cellspacing="0" cellpadding="0"
                                                                       style="border: 0;">
                                                                    <tbody>
                                                                    <tr>
                                                                        <td bgcolor="#357eaa"
                                                                            style="padding: 12px 68px 12px 68px;-webkit-border-radius: 6px;border-radius: 6px;border: 0;"
                                                                            align="center"><a href="{{ link }}"
                                                                                              target="_blank"
                                                                                              style="font-size: 16px; font-family: 'Roboto', helvetica, arial, sans-serif; font-weight: normal; color: #ffffff; text-decoration: none; display: inline-block;font-weight: 900;">
                                                                                              Safir Cloud Control Page</a></td>
                                                                    </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        </tbody>
                                                    </table>

                                                    <p>&nbsp;</p>

                                                    <p style="margin-top: 0; margin-bottom: 0; font-size: 14px; font-family: 'Roboto', helvetica, arial, sans-serif; color: #383838; font-weight: 300;">
                                                        Safir Cloud Team</p>
                                                    <div style="width: 100%; height: 1px; background-color: #f5f5f5; margin-top: 40px;"></div>
                                                </td>
                                            </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        </tbody>
    </table>
</div>

</body>
</html>
