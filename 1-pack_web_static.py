#!/usr/bin/python3
"""
Fabric script
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    function that generates .tgz with the web_static content
    """
    path_versions = "versions"
    path_web_static = "web_static"
    path_file_tgz = "{}/{}_{}.tgz".\
        format(path_versions,
               path_web_static,
               datetime.now().strftime("%Y%m%d%H%M%S"))

    print("Packing {} to {}".format(path_web_static, path_file_tgz))

    local("mkdir -p {}".format(path_versions), capture=True)

    status_file_tgz = local("tar -cvzf {} {} ".format(
        path_file_tgz,
        path_web_static)
    )

    return path_file_tgz if status_file_tgz.succeeded else None
