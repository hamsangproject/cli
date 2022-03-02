#!/usr/bin/python3

from sys import argv
from core.dbmanager import get_meaning
from pprint import pprint


def stylize_dict(dictext):
    text = ""
    # pprint(dictext)

    for entry in dictext:
        # print(entry)
        text += f"""
🔆{entry['dict_name']} """
        for res in entry['result']:
            text += f"""🍊 {res['word']}
            """
            text += f"""
{res['definition']}
            """
    return text

word = argv[1]
definition = get_meaning(word, database='*', json_out=False)
outtext = stylize_dict(definition)
# سمبل‌کاری برای پایانه‌هایی که از نیم‌فاصله پشتیبانی نمی‌کنند.
# راهکار درست: مشکل پایانه را برطرف کنید و خط زیر را بردارید
# outtext = outtext.replace('‌', '-')
print(outtext)

