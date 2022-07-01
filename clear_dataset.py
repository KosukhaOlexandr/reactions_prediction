#!/usr/bin/python
# -*- coding: utf-8 -*-
import ijson
import json
import datetime

attr_to_keep = ['message_id', 'date', 'text', 'caption', 'views']

TSN_ID = -1001305722586


def clear_message_dict(message_dict):
    new_comment = dict()
    to_write = True
    is_none_text = False
    is_none_caption = False
    for key, val in message_dict.items():
        if key in attr_to_keep:
            if key == 'text':
                if val is None:
                    is_none_text = True
                else:
                    new_comment['msg_text'] = val
            elif key == 'caption':
                if val is None:
                    is_none_caption = True
                else:
                    new_comment['msg_text'] = val
            else:
                new_comment[key] = val

    if is_none_text and is_none_caption:
        to_write = False
    return new_comment, to_write


with open('bigchat.json', 'r', encoding = 'utf-8') as source:
    with open('clear_dataset.json', 'w+', encoding = 'utf-8') as res:
        write_count = 0
        res.write('[')

        objects = ijson.items(source, 'item')
        for obj in objects:
            cleared_msg, to_write = clear_message_dict(obj)

            if to_write:
                if write_count > 0:
                    res.write(',\n')
                json.dump(cleared_msg, res, indent=2, ensure_ascii=False)
                write_count += 1
                print(write_count)

        res.write(']')