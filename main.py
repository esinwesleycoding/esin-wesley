import os
import platform


def shutdown():
    system_type = platform.system()
    if system_type == "Windows":
        os.system("shutdown /s /t 1")
    elif system_type == "Linux" or system_type == "Darwin":
        #Darwin = macOS
        os.system("sudo hutdown -h now")
    else:
        print("Unsupported operating system for shutdown.")

    #Use with extreme aution
    shutdown()