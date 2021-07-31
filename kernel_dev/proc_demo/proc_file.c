#include<linux/init.h>
#include<linux/module.h>
#include<linux/proc_fs.h>

static char kbuf[128] = {0};

int my_proc_open(struct inode *my_proc_inode, struct file *my_proc_file)
{
  printk("my_proc_open!\n");
  return 0;
}

ssize_t my_proc_read(struct file *my_proc_file, char __user *buf, size_t size, loff_t *offset)
{
  printk("my_proc_read!\n");
  copy_to_user(buf, kbuf, strlen(kbuf));
  return strlen(buf);
}

ssize_t my_proc_write(struct file *my_proc_file, const char __user *buf, size_t size, loff_t *offset)
{
  printk("my_proc_write!\n");
  copy_from_user(kbuf, buf, strlen(buf));
  return strlen(buf);
}

int my_proc_release(struct inode *my_proc_inode, struct file *my_proc_file)
{
  printk("my_proc_release!\n");
  return 0;
}

const struct proc_ops my_proc_file_ops = {
					       .proc_open = my_proc_open,
					       .proc_read = my_proc_read,
					       .proc_write = my_proc_write,
					       .proc_release = my_proc_release,
};


struct proc_dir_entry *pde = NULL;

static int my_proc_init(void)
{
  printk("hello, proc!\n");
  pde =  proc_mkdir_data("my_proc_dir", 0775, NULL, NULL);
  proc_create_data("my_proc_file", 0664, pde,
		   &my_proc_file_ops, NULL);
  return 0;
}

static void my_proc_exit(void)
{
  remove_proc_entry("my_proc_file", pde);
  remove_proc_entry("my_proc_dir", NULL);
  printk("Bye!\n");
}


module_init(my_proc_init);
module_exit(my_proc_exit);

MODULE_LICENSE("GPL");
