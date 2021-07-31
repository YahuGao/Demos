#include<sys/syscall.h>
#include<fcntl.h>
#include<stdio.h>

int main(void){
  int fd = open("/proc/my_proc_dir/my_proc_file", O_RDWR);
  close(fd);
  return 0;
}
