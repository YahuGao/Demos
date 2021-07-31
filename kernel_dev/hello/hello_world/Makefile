# kernel source
KERNEL_SRC=/usr/src/linux-headers-5.8.0-55-generic

#current directory
PWD = $(shell pwd)

#kernel module
obj-m += hello_world.o

all:
	make -C $(KERNEL_SRC) M=$(PWD) modules

clean:
	rm -rf *.ko *.o *.symvers *.cmd *.cmd.o *.mod.* *.mod *.order
