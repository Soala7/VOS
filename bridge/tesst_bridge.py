import sys
import os


# Add VOS root directory to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from shell_bridge import ShellBridge
from bridge.vos_api import vos_api
from filesystem.filesystem import FileSystem


# Create VOS filesystem
filesystem = FileSystem()


# Connect filesystem to VOS API
vos_api.register_filesystem(
    filesystem
)


# Start shell bridge
shell = ShellBridge()


print("\n--- PWD TEST ---")
print(shell.execute("pwd"))


print("\n--- LS TEST ---")
print(shell.execute("ls"))


print("\n--- CD TEST ---")
print(shell.execute("cd home"))


print("\n--- PWD AFTER CD ---")
print(shell.execute("pwd"))


print("\n--- MKDIR TEST ---")
print(shell.execute("mkdir test"))


print("\n--- LS AFTER MKDIR ---")
print(shell.execute("ls"))


print("\n--- TOUCH TEST ---")
print(shell.execute("touch hello.txt"))


print("\n--- FINAL LS ---")
print(shell.execute("ls"))


shell.shutdown()