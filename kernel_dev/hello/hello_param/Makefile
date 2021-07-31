# kernel source
KERNEL_SRC=/usr/src/linux-headers-$(shell uname -r)

#current directory
PWD = $(shell pwd)

#kernel module
obj-m += hello_param.o

all:
	make -C $(KERNEL_SRC) M=$(PWD) modules

clean:
	rm -rf *.ko *.o *.symvers *.cmd *.cmd.o *.mod.* *.mod *.order
