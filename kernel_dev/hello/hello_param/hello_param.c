/*
 * =====================================================================================
 *
 *       Filename:  hello_param.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2021年07月05日 22时44分36秒
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

static int param = 10;

static int hello_init(void)
{
  printk("Hello, World! param is %d\n", param);
  return 0;
}

static void hello_exit(void)
{
  printk("Bye! param is %d\n", param);
}

module_init(hello_init);
module_exit(hello_exit);
// module_param 中的权限不能是writable
module_param(param, int, S_IRUGO);

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Hello, Module");
