# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 14:40 2023

@author: <jeyakumar.kasi@hyproid.com>
"""

import os
import pika
import ssl
import time

class log:
    @staticmethod
    def info(msg):
        print(msg)

    def warning(msg):
        print(f"[WARNING]: {msg}")


class cf:
    AMQP_SSL = 1
    AMQP_SSL_CIPHERS = 'ECDHE+AESGCM:!ECDSA'
    # AMQP_URL = 'https://mqdevstg.mpkkt.net'#:8080/'
    AMQP_URL = 'https://mqdevstg.mpokket.app/'
    AMQP_CREDENTIAL = 'amqp://stguser:stgpass@mqdevstg.mpokket.app:5671/stg'
    AMQP_DATA_BACKUP_FILE_NAME = 'publish_data_for_'
    AMQP_CONNECTION_RETRY_PERIOD = 5
    AMQP_MAX_CONNECTION_RETRY_TIMES = 3



class AmqClient(object):
    def __init__(self):

        self.params = pika.URLParameters(cf.AMQP_CREDENTIAL)

        if cf.AMQP_SSL == 1:
            # SSL Context for TLS configuration of Amazon MQ for RabbitMQ
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            ssl_context.set_ciphers(cf.AMQP_SSL_CIPHERS)
            self.params.ssl_options = pika.SSLOptions(context=ssl_context)

        self.conn = pika.BlockingConnection(self.params)
        self.max_retries = 0
        self.channel = self.conn.channel()

    def getChannel(self):
        if self.conn.is_open:
            assert isinstance(self.channel, pika.adapters.blocking_connection.BlockingChannel)
            if self.channel.is_open:
                return self.channel
            self.channel = self.conn.channel()
            return self.channel
        else:
            log.error('connection not found | %s', self.conn.is_open)
            if self.max_retries == 10:
                log.warning('max retries error')
                return
            ret = self.makeConnection()
            return self.getChannel() if ret else None

    def makeConnection(self):
        try:
            log.info('creating new connection')

            if cf.AMQP_SSL == 1:
                # SSL Context for TLS configuration of Amazon MQ for RabbitMQ
                ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
                ssl_context.set_ciphers(cf.AMQP_SSL_CIPHERS)
                self.params.ssl_options = pika.SSLOptions(context=ssl_context)

            self.conn = pika.BlockingConnection(self.params)
            self.max_retries = 0
            return True
        except Exception as e:
            log.info('error in creating connection | %s', e)
            if self.max_retries !=10:
                self.max_retries += 1
                self.makeConnection()
            else:
                return False


def init_amq():
    log.info('init_called')

amq_obj = AmqClient()

print(amq_obj.params)
print(amq_obj.conn)

print(amq_obj.getChannel())


