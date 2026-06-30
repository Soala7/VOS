from kernel.kernel import Kernel


def boot_system():
    kernel = Kernel()
    kernel.boot()