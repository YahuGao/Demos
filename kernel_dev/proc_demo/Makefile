KERNEL_SRC = /usr/src/linux-headers-$(shell uname -r)

PWD = $(shell pwd)

obj-m += proc_file.o

all:
	make -C $(KERNEL_SRC) M=$(PWD) modules

clean:
	rm -rf *.ko *.o *.symvers .*.cmd *.mod* *.order
