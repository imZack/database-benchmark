#!/usr/bin/env python

from sys import stdin
import sqlite3
import msgpack

conn = sqlite3.connect('/mnt/data/output/sqlite3/tags.db')


def create_tbl(conn):
    conn.execute(
        'CREATE TABLE readings ('
        ' id          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
        ' equipment   VARCHAR(256) NOT NULL,'
        ' channel     VARCHAR(256) NOT NULL,'
        # ' time_ms     BIGINT NOT NULL,'
        # ' value_type  CHARACTER(3) NOT NULL,'
        ' value       VARCHAR(256) NOT NULL'
        # ' received_ms BIGINT'
        ');'
    )
    conn.execute('PRAGMA journal_mode = MEMORY')
    conn.commit()


def insert_tags(conn):
    objs = []
    unpacker = msgpack.Unpacker()
    for buff in stdin:
        unpacker.feed(buff)
        for o in unpacker:
            objs.append(o)

        if len(objs) > 200:
            conn.executemany(
                'INSERT INTO readings'
                ' (equipment, channel, value)'
                ' VALUES (:eqid, :tag, :value);',
                objs
            )
            conn.commit()
            objs = []

    if len(objs) > 0:
        conn.executemany(
            'INSERT INTO readings'
            ' (equipment, channel, value)'
            ' VALUES (:eqid, :tag, :value);',
            objs
        )
        conn.commit()
create_tbl(conn)
insert_tags(conn)
conn.close()
