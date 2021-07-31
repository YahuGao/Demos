/*
 * =====================================================================================
 *
 *       Filename:  sum_test.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2021年07月07日 09时16分55秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Yahu Gao (fl), gao_yahu.com
 *        Company:  Demo
 *
 * =====================================================================================
 */

#include<linux/init.h>
#include<linux/module.h>

extern int yahu_sum(int, int);

static int sum_test_init(void)
{
  printk("sum_test_init loaded!\n");
  printk("yahu_sum(3, 4) is %d\n", yahu_sum(3, 4));
  return 0;
}

static void sum_test_exit(void)
{
  printk("sum_test_init removed\n");
}

module_init(sum_test_init);
module_exit(sum_test_exit);


MODULE_LICENSE("GPL");
MODULE_AUTHOR("yahu");
MODULE_DESCRIPTION("sum test");
