#!/usr/bin/python3
"""
Fabric script
"""
from datetime import datetime
from fabric.api import *


env.user = 'ubuntu'
env.hosts = ['35.196.6.135', '52.23.205.208']


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


def do_deploy(archive_path):
    """
    function that distributes an archive to own web servers
    """
    if (archive_path):
        print("Executing task 'do_deploy'")
        path_remote_tmp = "/tmp/"
        path_tgz_file = "{}{}".format(path_remote_tmp, archive_path[9:])
        path_web_static = "/data/web_static/releases/{}/".format(
            archive_path[9:-4])
        path_symbolic_link = "/data/web_static/current"
        try:
            # Send the local archive to a remote host
            put(archive_path, path_remote_tmp)
            # Create web_static directory and uncompress the .tgz
            run("mkdir -p {}".format(path_web_static))
            run("tar -xzf {} -C {}".format(path_tgz_file, path_web_static))
            # Remove the .tgz
            run("rm {}".format(path_tgz_file))
            # Move data to web_static_DATE dir and remove the dir web_static
            run("mv {}web_static/* {}".format(path_web_static,
                path_web_static))
            run("rm -rf {}web_static".format(path_web_static))
            # Remove symbolic link and create again
            run("rm -rf {}".format(path_symbolic_link))
            run("ln -s {} {}".format(path_web_static, path_symbolic_link))
            print("New version deployed!")
            return True
        except Exception:
            return False
    else:
        return False
