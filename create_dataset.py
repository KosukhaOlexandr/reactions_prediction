#!/usr/bin/python
# -*- coding: utf-8 -*-
import asyncio
import json
import pathlib
from pyrogram import Client
import datetime
import login

def dict_to_prim(dct):
    """
    Converts dictionary of pyrogram types to dictionary of primitive types
    Inplace operation
    :param dct: dictionary to change
    :return: dictionary of primitive types
    """

    for key, item in dct.items():
        if key in attributes_skip:
            dct[key] = None
            continue
        if key == 'caption' or key == 'text':
            if item is None:
                dct[key] = None
            else:
                dct[key] = str(item)
        elif type(item) == str:
            dct[key] = str(item)
        else:
            if key == 'reactions' and item is not None:
                reactions = [v.__dict__ for v in item]
                for idx, a in enumerate(reactions):
                    a['_client'] = None
                    dct[key][idx] = a
            else:
                if isinstance(item, pathlib.PurePath):
                    dct[key] = str(item)
                else:
                    if type(item) == list:
                        for idx, it in enumerate(item):
                            if type(it) == str:
                                item[idx] = str(it)
                            else:
                                try:
                                    it = it.__dict__
                                    item[idx] = dict_to_prim(it)
                                except AttributeError:
                                    item[idx] = str(it)
                    else:
                        if type(item) not in [dict, int, list, str, int, float, bool] and item is not None:
                            try:
                                item = item.__dict__
                                dct[key] = dict_to_prim(item)
                            except AttributeError:
                                dct[key] = str(item)

    return dct


attributes_skip = ['chat', '_client']

api_id = login.API_ID
api_hash = login.API_HASH


start_date = datetime.datetime(2022, 3, 9)

tsn_id = -1001305722586


async def main():
    n = 0
    with open("bigchat.json", "w+", encoding="utf-8") as output:
        output.write('[')
        async with Client('my_account', api_id, api_hash) as app:
            async for message in app.iter_history(tsn_id):
                mesdict = message.__dict__
                mesdict['date'] = datetime.datetime.fromtimestamp(mesdict.get('date'))
                if mesdict['date'] >= start_date:
                    if n > 0:
                        output.write(',\n')
                    #print(dict_to_prim(mesdict))
                    json.dump(dict_to_prim(mesdict), output, indent=2, ensure_ascii=False)
                    n = n + 1
                    print(n)
            output.write(']')
            print(n)


asyncio.run(main())
