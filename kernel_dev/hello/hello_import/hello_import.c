/*
 * =====================================================================================
 *
 *       Filename:  hello_world.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2021年07月05日 21时50分02秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  first_name last_name (fl), fl@my-company.com
 *        Company:  my-company
 *
 * =====================================================================================
 */

#include <linux/init.h>
#include <linux/module.h>

extern int param_ex;

static int hello_import_init(void)
{
  printk("Hello, World! param_import %d\n", param_ex);
  return 0;
}

static void hello_import_exit(void)
{
  printk("Bye!\n");
}

module_init(hello_import_init);
module_exit(hello_import_exit);

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Hello Module");
MODULE_AUTHOR("gao_yahu@163.com");
