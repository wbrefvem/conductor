from fabric.api import run, env
from fabric.contrib.files import exists


def clone_repo(url=''):

    env.user = 'ec2-user'

    repo = url.split('/')
    repo = repo[-1].split('.')[0]

    if not exists(repo):
        run('git clone %s' % url)
    else:
        run('git pull')
