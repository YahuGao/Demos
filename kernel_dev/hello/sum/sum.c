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

int yahu_sum(int a, int b)
{
  return a + b;
}
EXPORT_SYMBOL(yahu_sum);

static int sum_init(void)
{
  printk("sum, enabled!\n");
  return 0;
}

static void sum_exit(void)
{
  printk("Bye, sum!\n");
}

module_init(sum_init);
module_exit(sum_exit);

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("sum Module");
MODULE_AUTHOR("gao_yahu@163.com");
