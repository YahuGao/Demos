KERNEL_SRC=/usr/src/linux-headers-5.8.0-59-generic

PWD = $(shell pwd)

obj-m := sum_test.o

all:
	make -C $(KERNEL_SRC) M=$(PWD) modules

clean:
	rm -rf *.ko *.o *.symvers *.cmd *.cmd.o *.mod.* *.mod *.order
