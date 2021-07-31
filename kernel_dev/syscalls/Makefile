KERNEL_SRC=/usr/src/linux-headers-$(shell uname -r)

PWD=$(shell pwd)

obj-m += my_syscall.o

all:
	make -C $(KERNEL_SRC) M=$(PWD) modules

