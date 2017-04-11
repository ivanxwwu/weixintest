# coding: utf8
#
# weixintest - version
# 
# Author: ilcwd 
# Create: 14/11/12
#

import flask

from ..core import success_response

app = flask.Blueprint('version', __name__)

VERSION = r"${VERSION}"
GIT_COMMIT = r"${GIT_COMMIT}"
GIT_BRANCH = r"${GIT_BRANCH}"
BUILD_TIME = r"${BUILD_TIME}"
SERVICE = r"weixintest"


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def version():
    info = dict(
        version=VERSION,
        git_commit=GIT_COMMIT,
        git_branch=GIT_BRANCH,
        build_time=BUILD_TIME,
        service=SERVICE,
    )
    return success_response(info)