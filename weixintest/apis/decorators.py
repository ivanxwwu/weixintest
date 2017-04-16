# -*- coding: utf-8 -*-
from functools import wraps
import hashlib
from flask import abort, g, request
from ..core import exceptions, config, constants

def check_weixin_sig(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        tmp = request.args
        signature = tmp.get('signature', None)
        timestamp = tmp.get('timestamp', None)
        nonce = tmp.get('nonce', None)
        if not signature or not timestamp or not nonce:
            raise exceptions.CheckException, "check weixin sig error"
        l = [constants.token, timestamp, nonce]
        l.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, l)
        hcode = sha1.hexdigest()
        if hcode != signature:
            raise exceptions.CheckException, "check weixin sig error"
        return f(*args, **kwargs)
    return wrapper