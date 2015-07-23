import subprocess
import yaml
import binascii
import os

from Crypto.Random import get_random_bytes
from django.core.management.base import BaseCommand, CommandError

KEY = binascii.hexlify(get_random_bytes(32))
IV = binascii.hexlify(get_random_bytes(16))


class Command(BaseCommand):

    help = 'Encrypts a file and uploads its secure keys to Travis and Heroku.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):

        file_path = options['file_path']

        if not os.path.isfile(file_path):
            raise CommandError('File <%s> does not exist or is not a file.' % file_path)

        subprocess.call(['travis', 'encrypt', 'DJANGO_KEY=%s' % KEY, '--add'])
        subprocess.call(['travis', 'encrypt', 'DJANGO_IV=%s' % IV, '--add'])
        subprocess.call(['heroku', 'config:set', 'DJANGO_KEY=%s' % KEY])
        subprocess.call(['heroku', 'config:set', 'DJANGO_IV=%s' % IV])

        subprocess.call(['openssl', 'aes-256-cbc', '-K', KEY, '-iv', IV, '-in', file_path, '-out', '%s.enc' % file_path, '-e'])

        with open('.travis.yml', 'r+') as f:
            travis_yml = yaml.load(f)

            travis_yml['before_install'] = 'openssl aes-256-cbc -K $DJANGO_KEY -iv $DJANGO_IV -in %s.enc -out %s -d' % (file_path, file_path)

            f.seek(0)
            yaml.dump(travis_yml, f)
