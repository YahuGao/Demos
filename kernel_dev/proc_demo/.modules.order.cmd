cmd_/home/yahu/kernel_dev_demo/proc_demo/modules.order := {   echo /home/yahu/kernel_dev_demo/proc_demo/proc_file.ko; :; } | awk '!x[$$0]++' - > /home/yahu/kernel_dev_demo/proc_demo/modules.order
