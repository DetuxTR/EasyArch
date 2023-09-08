import subprocess

def run_cmd(pkg_args):
    res = subprocess.run(pkg_args,capture_output=True,text=True)
    return res