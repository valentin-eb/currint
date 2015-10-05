import os
import subprocess
import currint
from invoke import task


VERSION_FILE = os.path.join(os.path.dirname(currint.__file__), "__init__.py")


def _write_to_version_file(version):
    with open(VERSION_FILE, 'r') as version_read:
        output = []
        for line in version_read:
            if line.startswith('__version__'):
                output.append('__version__ = %r' % version)
            else:
                output.append(line.strip())

    with open(VERSION_FILE, 'w') as version_write:
        for line in output:
            version_write.write(line + '\n')


def _commit_and_tag(version):
    """Commit changes to version file and tag the release"""
    subprocess.check_call(
        ['git', 'add', VERSION_FILE],
    )
    subprocess.check_call(
        ['git', 'commit', '-m', "Releasing version %s" % version]
    )
    subprocess.check_call(
        ['git', 'tag', version]
    )


def _push_release_changes(version):
    push = raw_input('Push release changes to master? (y/n): ')
    if push == 'y':
        print subprocess.check_output(
            ['git', 'push', 'origin', 'master']
        )
        # push the release tag
        print subprocess.check_output(
            ['git', 'push', 'origin', version]
        )
    else:
        print 'Not pushing changes to master!'
        print 'Make sure you remember to explictily push the tag!'


@task
def release():
    # Prompt for version
    print "Current version: %s" % currint.__version__
    release_version = raw_input('Enter a new version (or "exit"): ')
    if not release_version or release_version == 'exit':
        print 'Cancelling release!'
        return

    _write_to_version_file(release_version)
    _commit_and_tag(release_version)
    _push_release_changes(release_version)
