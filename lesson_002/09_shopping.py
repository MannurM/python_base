#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
        {'shops': 'пятерочка', 'price': 9.99},
        {'shops': 'ашан', 'price': 10.99}
    ],
    'пирожное': [
        {'shops': 'магнит', 'price': 62.99},
        {'shops': 'пятерочка', 'price': 59.99}

    ],
    'конфеты': [
        {'shops': 'магнит', 'price': 30.99},
        {'shops': 'пятерочка', 'price': 32.99}
    ],
    'карамель': [
        {'shops': 'магнит', 'price': 41.99},
        {'shops': 'ашан', 'price': 45.99}
    ]
}

# Указать надо только по 2 магазина с минимальными ценами

print(sweets)

# Зачёт!
