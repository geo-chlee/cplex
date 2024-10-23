import subprocess
import os
import glob
import shutil
import sys

def get_cos_archname(bindir, so):
    arch = [a for a in glob.glob("{}/**/{}".format(bindir, so), recursive=True)]
    if len(arch) == 0:
        return None
    elif len(arch) > 1:
        print("Error: multiple source files found: {}".format(arch))
        return None
    return os.path.basename(os.path.dirname(arch[0]))

def check_file(fname, write = False):
    if write:
        ok = os.access(fname, os.W_OK)
        if not ok:
            print("Error: {} should be present and writable but is not".format(fname))
    else:
        ok = os.access(fname, os.R_OK)
        if not ok:
            print("Error: {} should be present and readable but is not".format(fname))
    return ok


def get_shared_lib_extension():
    platform = sys.platform.lower()
    if "linux" in platform:
        return ".so"
    elif "win" in platform:
        return ".dll"
    elif "darwin" in platform:
        return ".dylib"
    else:
        return None  # Unknown platformllt


def get_cpo_name(version):
    return "cpoptimizer.exe" if sys.platform == "win32" else "cpoptimizer"


def get_so_name(version):
    ext = get_shared_lib_extension()
    prefix = "" if sys.platform == "win32" else "lib"
    return "{}cplex{}{}".format(prefix, version, ext)

cos=input("Type your CPLEX path (e.g., C:\Program Files\IBM\ILOG\CPLEX_Studio2211)\n >> ")

sub_program = """
try:
    import cplex
    print(cplex.__path__[0], cplex.__version__)
except ModuleNotFoundError as e:
    print('Error: could not import module \"cplex\"')

    """

    # This needs to be run as another process as there is no other
    # way of unloading the 'cplex' module and since we will copy
    # a new shared object over the already loaded one, leaving the
    # cplex module loaded can create a segmentation fault an program exit.
out = subprocess.run([sys.executable, "-c", sub_program], capture_output=True)
if out.returncode == 0:
    stdout = out.stdout.decode("utf-8").strip().rsplit(" ",1)

pcplex=stdout[0]
version=stdout[1]

pcplex = os.path.realpath(pcplex)
version_mneumonic = "".join(version.split(".")[:3])
so_name = get_so_name(version_mneumonic)
cpo_name = get_cpo_name(version_mneumonic)

target_bindir = os.path.dirname(sys.executable)
target_root = os.path.dirname(target_bindir)

so_targets = [ t for t in glob.glob("{}/**/{}".format(target_root, so_name), recursive=True) ]
cpo_targets = [ t for t in glob.glob("{}/**/{}".format(target_root, cpo_name), recursive=True) ]

if len(so_targets) == 0:
    print("Error: did not find shared object file {} in {}".format(so_name, target_root))
if len(cpo_targets) == 0:
    print("Error: did not find executeable file {} in {}".format(cpo_name, target_root))

bindir = os.path.join(cos, "cplex", "bin")
platform = get_cos_archname(bindir, so_name)
if platform is None:
    print("Error: unable to determine COS architecture mneumonic by searching for {} in {}. Please check you COS installation".format(so_name, bindir))

so_source = os.path.join(cos, "cplex", "bin", platform, so_name)
cpo_source = os.path.join(cos, "cpoptimizer", "bin", platform, cpo_name)

ok = check_file(so_source, False)
ok = check_file(cpo_source, False) and ok
for f in so_targets + cpo_targets:
    ok = check_file(f, True)

if not ok:
    print ("Not OK")

copies = tuple((so_source, t) for t in so_targets) + tuple((cpo_source, t) for t in cpo_targets)

print("Performing copies:")
code = 0
try:
    for s,t in copies:
        print("    {} -> {}".format(s, t))
        shutil.copyfile(s, t)
except Exception as e:
    print("Error: Something went wrong during copying: {}".format(e))
    code = 1


