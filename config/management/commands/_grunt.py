import os
import subprocess
import atexit
import signal

from django.conf import settings


def start_grunt(command):
    """
    Starts grunt processes
    Based on https://lincolnloop.com/blog/simplifying-your-django-frontend-tasks-grunt/
    """

    command.stdout.write('>>> Starting grunt')
    command.grunt_process = subprocess.Popen(
        ['grunt --gruntfile={0}/Gruntfile.js --base=.'.format(settings.PROJECT_PATH)],
        shell=True,
        stdin=subprocess.PIPE,
        stdout=command.stdout,
        stderr=command.stderr,
    )

    command.stdout.write('>>> Grunt process on pid {0}'.format(command.grunt_process.pid))

    def kill_grunt_process(pid):
        command.stdout.write('>>> Closing grunt process')
        os.kill(pid, signal.SIGTERM)

    atexit.register(kill_grunt_process, command.grunt_process.pid)