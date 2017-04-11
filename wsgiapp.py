#coding:utf8
"""
Created on Jun 18, 2014

@author: ilcwd
"""
import logging.config
import logging
import os

import yaml

from weixintest.core import application, misc
_parent = os.path.join(os.path.dirname(__file__), 'deployment')
logging_config_path = os.path.join(_parent, 'logging.yaml')
app_config_path = os.path.join(_parent, 'config.json')

# register APIs after `C.load_config()`
from weixintest.views import default
from weixintest.apis import weixintest
application.register_blueprint(weixintest.app, url_prefix='/weixintest')

if __name__ != '__main__':
    with open(logging_config_path, 'r') as f:
        logging.config.dictConfig(yaml.load(f))

def main():
    """Debug Mode"""
    import sys
    _logger = logging.getLogger()
    _logger.setLevel(logging.DEBUG)
    _logger.addHandler(logging.StreamHandler(stream=sys.stdout))

    host, port = '0.0.0.0', 8080
    application.run(host, port, debug=True, use_reloader=False)


if __name__ == '__main__':
    main()
