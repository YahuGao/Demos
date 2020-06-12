(add-to-list 'load-path "~/.emacs.d/lisp/")
(require 'init-melpa)
(require 'init-packages)
(load-theme 'monokai 1)

(add-to-list 'load-path "~/emacs-application-framework")
(require 'eaf)

;; 修改配置文件后，需要重启编辑器或者重新加载配置文件
;; 重新加载配置文件 M-x load-file Enter Enter or M-x eval-buffer
;; 显示行号
(global-linum-mode 1)
;; 更改光标的样式（不能生效，解决方案见第二集）
;; (setq cursor-type 'bar)
;; setq 设置当前缓冲区（Buffer）中的变量值， setq-default 设 置的为全局的变量的值
(setq-default cursor-type 'bar)
;; 关闭启动帮助画面
(setq inhibit-splash-screen 1)
;; 关闭缩进 (第二天中被去除)
;; 自动缩进存在不理想的缩进效果，可使用;;双分号避免，故取消关闭
;; (electric-indent-mode -1)
;; 更改显示字体大小 16pt
;; http://stackoverflow.com/questions/294664/how-to-set-the-font-size-in-emacs
(set-face-attribute 'default nil :height 160)
;; 快速打开配置文件
(defun open-init-file()
  (interactive)
  (find-file "~/.emacs.d/init.el"))
;; 这一行代码，将函数 open-init-file 绑定到 <f2> 键上
(global-set-key (kbd "<f2>") 'open-init-file)
;; 开启全局 Company 补全, uninstalled Company
;; (global-company-mode 1)
;; 关闭自动备份
(setq make-bakeup-files 0)
;; 关闭自动保存
(setq auto-save-default 0)
;; 使用下面的配置文件将删除功能配置成与其他图形界面的编辑器相同
;; 即当你选中一段文字 之后输入一个字符会替换掉你选中部分的文字。
(delete-selection-mode 1)
;; 自动括号匹配
(add-hook 'emacs-lisp-mode-hook 'show-paren-mode)
;; 高亮当前行 void function
(global-hl-line-mode 1)
;; 简化yes or no 为y or n
(fset 'yes-or-no-p 'y-or-n-p)
;; 缩写补全
(setq-default abbrev-mode t)
(define-abbrev-table 'global-abbrev-table '(
					    ("8yh" "Yahu Gao")
					    ("8yh@" "yahu.gao@outlook.com")
					    ))
;; C-w 向后删除一个单词
(global-set-key (kbd "C-w") 'backward-kill-word)
;; 显示时间
(display-time-mode 1)
(setq display-time-24hr-format t)
;; (setq display-time-day-and-date t)
;; 隐藏工具栏菜单栏和滚动条
(tool-bar-mode 0)
(menu-bar-mode 0)
(scroll-bar-mode 0)
