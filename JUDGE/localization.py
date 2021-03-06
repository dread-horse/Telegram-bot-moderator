from configurator import config
import re
import requests
from bs4 import BeautifulSoup

def anekdot():
    s = requests.get('http://anekdotme.ru/random')
    b = BeautifulSoup(s.text, "html.parser")
    p = b.select('.anekdot_text')
    s = (p[0].getText().strip())
    reg = re.compile('[^a-zA-ZŠ°-ŃŠ-Ń ^0-1-2-3-4-5-6-7-8-9:.,!?-]')
    s = reg.sub('', s)
    return s



strings = {
    "en": {
        "error_no_reply": "This command must be sent as a reply to one's message!",
        "error_report_admin": "Whoa! Don't report admins š",
        "error_restrict_admin": "You cannot restrict an admin.",
        "error_wrong_time_format": "Wrong time forman. Use a number + symbols 'h', 'm' or 'd'. F.ex. 4h",
        "error_message_too_short": "Please avoid short useless greetings. "
                                   "If you have a question or some information, put it in one message. Thanks in "
                                   "advance! š¤",

        "report_date_format": "%d.%m.%Y at %H:%M (server time)",
        "report_message": 'š Sent {date}\n'
                          '<a href="https://t.me/c/{chat_id}/{msg_id}">Go to message</a>',
        "report_note": "\n\nNote:{note}",
        "report_delivered": "<i>Report sent</i>",

        "action_del_msg": "Delete message",
        "action_del_and_ban": "Delete and ban",
        "action_del_and_readonly": "Set user readonly for 24 hours",
        "action_del_and_readonly2": "Set user readonly for 7 days",

        "action_deleted": "\n\nš <b>Deleted</b>",
        "action_deleted_banned": "\n\nšā <b>Deleted, user banned</b>",
        "action_deleted_readonly": "\n\nšš <b>Deleted, set readonly for 2 hours</b>",
        "action_deleted_readonly2": "\n\nšš <b>Deleted, set readonly for 2 hours</b>",

        "resolved_readonly": "<i>User set to read-only mode ({restriction_time})</i>",
        "resolved_nomedia": "<i>User set to text-only mode ({restriction_time})</i>",

        "restriction_forever": "forever",
        "need_admins_attention": 'Dear admins, your presence in chat is needed!\n\n'
                                 '<a href="https://t.me/c/{chat_id}/{msg_id}">Go to message</a>',

        "greetings_words": ("hi", "q", "hello", "hey")  # Bot will react to short messages with these words
    },
    "ru": {
        "error_no_reply": "Š­ŃŠ° ŠŗŠ¾Š¼Š°Š½Š“Š° Š“Š¾Š»Š¶Š½Š° Š±ŃŃŃ Š¾ŃŠ²ŠµŃŠ¾Š¼ Š½Š° ŠŗŠ°ŠŗŠ¾Šµ-Š»ŠøŠ±Š¾ ŃŠ¾Š¾Š±ŃŠµŠ½ŠøŠµ!",
        "error_report_admin": "ŠŠ“Š¼ŠøŠ½Š¾Š² ŃŠµŠæŠ¾ŃŃŠøŃŃ? ŠŠ¹-Š°Š¹-Š°Š¹ š",
        "error_report_self": "ŠŠµŠ»ŃŠ·Ń ŃŠµŠæŠ¾ŃŃŠøŃŃ ŃŠ°Š¼Š¾Š³Š¾ ŃŠµŠ±Ń š¤Ŗ",
        "error_restrict_admin": "ŠŠµŠ²Š¾Š·Š¼Š¾Š¶Š½Š¾ Š¾Š³ŃŠ°Š½ŠøŃŠøŃŃ Š°Š“Š¼ŠøŠ½ŠøŃŃŃŠ°ŃŠ¾ŃŠ°.",
        "error_wrong_time_format": "ŠŠµŠæŃŠ°Š²ŠøŠ»ŃŠ½ŃŠ¹ ŃŠ¾ŃŠ¼Š°Ń Š²ŃŠµŠ¼ŠµŠ½Šø. ŠŃŠæŠ¾Š»ŃŠ·ŃŠ¹ŃŠµ ŃŠøŃŠ»Š¾ + ŃŠøŠ¼Š²Š¾Š» h, m ŠøŠ»Šø d. ŠŠ°ŠæŃŠøŠ¼ŠµŃ, 4h",
        "error_message_too_short": "ŠŠ¾Š¶Š°Š»ŃŠ¹ŃŃŠ°, ŠøŠ·Š±ŠµŠ³Š°Š¹ŃŠµ Š±ŠµŃŃŠ¼ŃŃŠ»ŠµŠ½Š½ŃŃ ŠŗŠ¾ŃŠ¾ŃŠŗŠøŃ ŠæŃŠøŠ²ŠµŃŃŃŠ²ŠøŠ¹. "
                                   "ŠŃŠ»Šø Ń ŠŠ°Ń ŠµŃŃŃ Š²Š¾ŠæŃŠ¾Ń ŠøŠ»Šø ŠøŠ½ŃŠ¾ŃŠ¼Š°ŃŠøŃ, Š½Š°ŠæŠøŃŠøŃŠµ Š²ŃŃ Š² Š¾Š“Š½Š¾Š¼ ŃŠ¾Š¾Š±ŃŠµŠ½ŠøŠø. ŠŠ°ŃŠ°Š½ŠµŠµ "
                                   "ŃŠæŠ°ŃŠøŠ±Š¾! š¤",

        "report_date_format": "%d.%m.%Y Š² %H:%M (Š²ŃŠµŠ¼Ń ŃŠµŃŠ²ŠµŃŠ°)",
        "report_message": 'š ŠŃŠæŃŠ°Š²Š»ŠµŠ½Š¾ {date}\n'
                          '<a href="https://t.me/c/{chat_id}/{msg_id}">ŠŠµŃŠµŠ¹ŃŠø Šŗ ŃŠ¾Š¾Š±ŃŠµŠ½ŠøŃ</a>',
        "report_note": "\n\nŠŃŠøŠ¼ŠµŃŠ°Š½ŠøŠµ:{note}",
        "report_delivered": "<i>Š ŠµŠæŠ¾ŃŃ Š¾ŃŠæŃŠ°Š²Š»ŠµŠ½.</i>",

        "action_del_msg": "š Š£Š“Š°Š»ŠøŃŃ ŃŠ¾Š¾Š±ŃŠµŠ½ŠøŠµ",
        "action_del_and_ban": "š Š£Š“Š°Š»ŠøŃŃ + ā Š±Š°Š½ Š½Š°Š²ŃŠµŠ³Š“Š°",
        "action_del_and_readonly": "š Š£Š“Š°Š»ŠøŃŃ + š Š¼ŃŃ Š½Š° Š“ŠµŠ½Ń",
        "action_del_and_readonly2": "š Š£Š“Š°Š»ŠøŃŃ + š Š¼ŃŃ Š½Š° Š½ŠµŠ“ŠµŠ»Ń",

        "action_false_alarm": "ā ŠŠ°ŃŃŃŠµŠ½ŠøŠ¹ Š½ŠµŃ",
        "action_false_alarm_2": "ā ŠŠ°ŃŃŃŠµŠ½ŠøŠ¹ Š½ŠµŃ (š Š¼Š°Ń ŃŠµŠæŠ¾ŃŃŠµŃŠ° Š½Š° Š“ŠµŠ½Ń)",
        "action_false_alarm_3": "ā ŠŠ°ŃŃŃŠµŠ½ŠøŠ¹ Š½ŠµŃ (š Š¼Š°Ń ŃŠµŠæŠ¾ŃŃŠµŃŠ° Š½Š° Š½ŠµŠ“ŠµŠ»Ń)",
        "action_false_alarm_4": "ā ŠŠ°ŃŃŃŠµŠ½ŠøŠ¹ Š½ŠµŃ (ā Š±Š°Š½ ŃŠµŠæŠ¾ŃŃŠµŃŠ°)",
 
        "action_deleted": "\n\nš <b>Š£Š“Š°Š»ŠµŠ½Š¾</b>",
        "action_deleted_banned": "\n\nšā <b>Š£Š“Š°Š»ŠµŠ½Š¾, ŃŠ·ŠµŃ Š·Š°Š±Š°Š½ŠµŠ½</b>",
        "action_deleted_readonly": "\n\nšš <b>Š£Š“Š°Š»ŠµŠ½Š¾, + Š²ŃŠ“Š°Š½ Š¼ŃŃ Š½Š° Š“ŠµŠ½Ń.</b>",
        "action_deleted_readonly2": "\n\nšš <b>Š£Š“Š°Š»ŠµŠ½Š¾, + Š²ŃŠ“Š°Š½ Š¼ŃŃ Š½Š° Š½ŠµŠ“ŠµŠ»Ń.</b>",

        "action_dismissed": "\n\nā <b>ŠŠ°ŃŃŃŠµŠ½ŠøŠ¹ Š½Šµ Š¾Š±Š½Š°ŃŃŠ¶ŠµŠ½Š¾.</b>",
        "action_deleted_dismissed2": "\n\nā <b>ŠŠ°ŃŃŃŠµŠ½ŠøŠ¹ Š½Šµ Š¾Š±Š½Š°ŃŃŠ¶ŠµŠ½Š¾ (š ŃŠµŠæŠ¾ŃŃŠµŃŃ Š²ŃŠ“Š°Š½ Š¼ŃŃ Š½Š° 1 Š“ŠµŠ½Ń).</b>",
        "action_deleted_dismissed3": "\n\nā <b>ŠŠ°ŃŃŃŠµŠ½ŠøŠ¹ Š½Šµ Š¾Š±Š½Š°ŃŃŠ¶ŠµŠ½Š¾ (š ŃŠµŠæŠ¾ŃŃŠµŃŃ Š²ŃŠ“Š°Š½ Š¼ŃŃ Š½Š° 7 Š“Š½ŠµŠ¹).</b>",
        "action_deleted_dismissed4": "\n\nā <b>ŠŠ°ŃŃŃŠµŠ½ŠøŠ¹ Š½Šµ Š¾Š±Š½Š°ŃŃŠ¶ŠµŠ½Š¾ (ā ŃŠµŠæŠ¾ŃŃŠµŃ Š·Š°Š±Š°Š½ŠµŠ½).</b>",

        "resolved_readonly": "<i>ŠŃŠ“Š°Š½ Š¼ŃŃ Š½Š° ({restriction_time})</i>",
        "resolved_nomedia": "<i>ŠŠ°ŠæŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ Š¼ŠµŠ“ŠøŠ° Š½Š° ({restriction_time})</i>",
        "resolved_nomedia_forever": "<i>ŠŠ°ŠæŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ Š¼ŠµŠ“ŠøŠ° Š½Š°Š²ŃŠµŠ³Š“Š°.</i>",

        "resolved_givemedia": "<i>Š Š°Š·ŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ Š¼ŠµŠ“ŠøŠ° Š½Š° ({restriction_time})</i>",
        "resolved_givemedia_forever": "<i>Š Š°Š·ŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ Š¼ŠµŠ“ŠøŠ° Š½Š°Š²ŃŠµŠ³Š“Š°.</i>",
        "error_givemedia_admin": "<i>ŠŠ“Š¼ŠøŠ½Š°Š¼ ŠøŃŠ°Šŗ ŃŠ°Š·ŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ Š¼ŠµŠ“ŠøŠ°!</i>",

        "resolved_givestickers": "<i>Š Š°Š·ŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ ŃŃŠøŠŗŠµŃŃ Š½Š° ({restriction_time})</i>",
        "resolved_givestickers_forever": "<i>Š Š°Š·ŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ ŃŃŠøŠŗŠµŃŃ Š½Š°Š²ŃŠµŠ³Š“Š°.</i>",
        "error_givestickers_admin": "<i>ŠŠ“Š¼ŠøŠ½Š°Š¼ ŠøŃŠ°Šŗ ŃŠ°Š·ŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ ŃŃŠøŠŗŠµŃŃ!</i>",

        "resolved_revokestickers": "<i>ŠŠ°ŠæŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ ŃŃŠøŠŗŠµŃŃ Š½Š° ({restriction_time})</i>",
        "resolved_revokestickers_forever": "<i>ŠŠ°ŠæŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ ŃŃŠøŠŗŠµŃŃ Š½Š°Š²ŃŠµŠ³Š“Š°.</i>",
        "error_givestickers_admin": "<i>ŠŠ“Š¼ŠøŠ½Š°Š¼ ŠøŃŠ°Šŗ ŃŠ°Š·ŃŠµŃŠµŠ½Š¾ Š¾ŃŠæŃŠ°Š²Š»ŃŃŃ ŃŃŠøŠŗŠµŃŃ!</i>",

        "user_unmuted": "<i>ŠŃŃ ŃŠ½ŃŃ.</i>",

        "restriction_forever": "<i>ŠŃŠ“Š°Š½ Š¼ŃŃ Š½Š°Š²ŃŠµŠ³Š“Š°.</i>",
        "need_admins_attention": 'Š¢Š¾Š²Š°ŃŠøŃŠø Š°Š“Š¼ŠøŠ½Ń, Š² ŃŠ°ŃŠµ Š½ŃŠ¶Š½Š¾ Š²Š°ŃŠµ ŠæŃŠøŃŃŃŃŃŠ²ŠøŠµ!\n\n'
                                 '<a href="https://t.me/c/{chat_id}/{msg_id}">ŠŠµŃŠµŠ¹ŃŠø Šŗ ŃŠ¾Š¾Š±ŃŠµŠ½ŠøŃ</a>',

        "resolved_ban": "<i>Š£ŃŠ°ŃŃŠ½ŠøŠŗ Š·Š°Š±Š»Š¾ŠŗŠøŃŠ¾Š²Š°Š½.</i>",
        "resolved_unban": "<i>Š£ŃŠ°ŃŃŠ½ŠøŠŗ ŃŠ°Š·Š±Š»Š¾ŠŗŠøŃŠ¾Š²Š°Š½.</i>",

        "error_checkperms_admin": "ā Š£ Š°Š“Š¼ŠøŠ½Š¾Š² Š½ŠµŃ Š½ŠøŠŗŠ°ŠŗŠøŃ Š¾Š³ŃŠ°Š½ŠøŃŠµŠ½ŠøŠ¹.",
        "error_ban_admin": "š” Š¢Ń ŃŃ, ŠæŃŃ? ŠŠ“Š¼ŠøŠ½Š° Š½ŠµŠ»ŃŠ·Ń Š·Š°Š±Š°Š½ŠøŃŃ!",

        "enabled_ro": "<i>Š ŠµŠ¶ŠøŠ¼ Ā«ŃŠ¾Š»ŃŠŗŠ¾-ŃŃŠµŠ½ŠøŠµĀ» Š²ŠŗŠ»ŃŃŠµŠ½.</i>",
        "disabled_ro": "<i>Š ŠµŠ¶ŠøŠ¼ Ā«ŃŠ¾Š»ŃŠŗŠ¾-ŃŃŠµŠ½ŠøŠµĀ» Š¾ŃŠŗŠ»ŃŃŠµŠ½.</i>",

        "profanity_user_kicked": "ŠŠ°ŃŠµ ŠøŠ¼Ń Š² Telegram ŃŠ¾Š“ŠµŃŠ¶ŠøŃ Š½ŠµŠ½Š¾ŃŠ¼Š°ŃŠøŠ²Š½ŃŃ Š»ŠµŠŗŃŠøŠŗŃ.\nŠŠ¾ ŃŃŠ¾Š¹ ŠæŃŠøŃŠøŠ½Šµ Š²Ń Š±ŃŠ»Šø ŠŗŠøŠŗŠ½ŃŃŃ ŠøŠ· ŃŠ°ŃŠ°.\n\nŠŠ¾Š¶Š°Š»ŃŠ¹ŃŃŠ°, Š¾ŃŃŠµŠ“Š°ŠŗŃŠøŃŃŠ¹ŃŠµ Š¾ŃŠ¾Š±ŃŠ°Š¶Š°ŠµŠ¼Š¾Šµ ŠøŠ¼Ń Šø ŠæŠ¾ŠæŃŠ¾Š±ŃŠ¹ŃŠµ Š·Š°Š½Š¾Š²Š¾.\nŠŠ°ŃŃŃŠµŠ½ŠøŠµ Š½Š°Š¹Š“ŠµŠ½Š¾ Š² ŃŠ»Š¾Š²Šµ: <u>{word}</u>",

        "voice_message_reaction": "ŃŃ! Š¤Š£ ŠÆ Š”ŠŠŠŠŠ, ŠŠŠŠ¬ŠŠÆ. ŠŠ ŠŠ”Š¬ ŠŠŠŠ£. ŠŠŠØŠ Š¢ŠŠŠ”Š¢ŠŠ.",

        "greetings_words": ("ŠæŃŠøŠ²ŠµŃ", "ŃŠ°Š¹", "ŠŗŃ", "Š·Š“Š°ŃŠ¾Š²Š°"),  # ŠŠ¾Ń ŃŃŠµŠ°Š³ŠøŃŃŠµŃ Š½Š° ŠŗŠ¾ŃŠ¾ŃŠŗŠøŠµ ŃŠ¾Š¾Š±ŃŠµŠ½ŠøŃ Ń ŃŃŠøŠ¼Šø ŃŠ»Š¾Š²Š°Š¼Šø

        "announcements" : (
            {
                "message" : "š Š£ŃŠ°ŃŃŠ½ŠøŠŗŠø ŃŠ°ŃŠ°, Š½Šµ Š·Š°Š±ŃŠ²Š°Š¹ŃŠµ ŠæŃŠ¾ ŠŗŠ¾Š¼Š°Š½Š“Ń <b>!report</b> Š±Š»Š°Š³Š¾Š“Š°ŃŃ ŠŗŠ¾ŃŠ¾ŃŠ¾Š¹ ŠŃ Š¼Š¾Š¶ŠµŃŠµ Š¾Š±ŃŠ°ŃŠøŃŃ Š²Š½ŠøŠ¼Š°Š½ŠøŠµ Š°Š“Š¼ŠøŠ½ŠøŃŃŃŠ°ŃŠøŠø Š½Š° Š½Š°ŃŃŃŠøŃŠµŠ»Ń Š² ŃŠ°ŃŠµ.\n<i>Š”ŠæŠ°Š¼ Š“Š°Š½Š½Š¾Š¹ ŠŗŠ¾Š¼Š°Š½Š“Š¾Š¹ ŠŗŠ°ŃŠ°ŠµŃŃŃ Š²ŠµŃŠ½ŃŠ¼ Š±Š°Š½Š¾Š¼.</i>",
                "every" : 43200
            },
            {
                "message" : "<b>ŠŠ±ŃŠ°ŠµŠ¼ŃŃ Š½Š° ŃŠµŠ¼Ń ŠæŃŠ¾Š³ŃŠ°Š¼Š¼ŠøŃŠ¾Š²Š°Š½ŠøŃ Šø Š²ŃŠµŠ³Š¾ ŃŃŠ¾ Ń Š½ŠøŠ¼ ŃŠ²ŃŠ·Š°Š½Š¾ š</b>\n\nš ŠŃŠµ ŃŃŠøŠŗŠµŃŃ Šø Š¼ŠµŠ“ŠøŠ° Š²ŃŠµŠ¼ŠµŠ½Š½Š¾ Š·Š°ŠæŃŠµŃŠµŠ½Ń\nš¤¬ ŠŠµŠ½Š¾ŃŠ¼Š°ŃŠøŠ²Š½Š°Ń Š»ŠµŠŗŃŠøŠŗŠ° Š·Š°ŠæŃŠµŃŠµŠ½Š°\nš½ ŠŃŃŃŠ¾Šæ Š½Š°ŠŗŠ°Š·ŃŠ²Š°ŠµŃŃŃ Š¼ŃŃŠ°Š¼Šø\n\n<b>ŠŃŠøŃŃŠ½Š¾Š³Š¾ Š¾Š±ŃŠµŠ½ŠøŃ š„°</b>",
                "every" : 43200
            },
            {
                "message" : "<b>#Š¾ŃŃŠ°Š²Š°Š¹ŃŠµŃŃŠ“Š¾Š¼Š° š¾ ŠøŠ³ŃŠ°Š¹ŃŠµ Š² ŠøŠ³ŃŃ, š½ ŃŠ¼Š¾ŃŃŠøŃŠµ ŃŠøŠ»ŃŠ¼Ń, š“ Š±Š¾Š»ŃŃŠµ Š¾ŃŠ“ŃŃŠ°Š¹ŃŠµ.</b>\n\nāļø ŠŃŠ“ŃŃŠµ Š·Š“Š¾ŃŠ¾Š²Ń\nšŠŃŠµŠ¼ Š¼ŠøŃŠ½Š¾Š³Š¾ Š½ŠµŠ±Š° Š½Š°Š“ Š³Š¾Š»Š¾Š²Š¾Š¹\nšÆŠ¢Š°Šŗ Š¶Šµ Š½Šµ Š·Š°Š±ŃŠ²Š°Š¹ŃŠµ ŠæŃŠ¾ Š½Š°Ń Discord ŃŠµŃŠ²ŠµŃ! https://discord.gg/q3bFjft2Hm",
                "every" : 43200
            },
            {
                "message" : lambda: anekdot(),
                "every" : 3600
            }

        )
    },
}




def get_string(key):
    """
    Get localized string. First, try language as set in config. Then, try English locale. Else - raise an exception.

    :param key: string name
    :return: localized string
    """
    localization_strings = strings.get(config.bot.language, strings.get('en'))

    if localization_strings is None:
        raise KeyError(f'Neither "{config.bot.language}" nor "en" locales found')

    try:
        return localization_strings[key]
    except KeyError:
        raise


