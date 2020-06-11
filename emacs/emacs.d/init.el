;; 修改配置文件后，需要重启编辑器或者重新加载配置文件
;; 重新加载配置文件 M-x load-file Enter Enter or M-x eval-buffer
;; 关闭工具栏，tool-bar-mode 即为一个 Minor Mode
(tool-bar-mode -1)

;; 关闭文件滑动控件
(scroll-bar-mode -1)

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
(setq make-bakeup-files nil)

;; 使用下面的配置文件将删除功能配置成与其他图形界面的编辑器相同
;; 即当你选中一段文字 之后输入一个字符会替换掉你选中部分的文字。
(delete-selection-mode 1)

;; https://melpa.org/#/getting-started
;; Install MELPA
(require 'package)
(let* ((no-ssl (and (memq system-type '(windows-nt ms-dos))
                    (not (gnutls-available-p))))
       (proto (if no-ssl "http" "https")))
  (when no-ssl (warn "\
Your version of Emacs does not support SSL connections,
which is unsafe because it allows man-in-the-middle attacks.
There are two things you can do about this warning:
1. Install an Emacs version that does support SSL and be safe.
2. Remove this warning from your init file so you won't see it again."))
  ;; (add-to-list 'package-archives (cons "melpa" (concat proto "://melpa.org/packages/")) t)
  ;; Comment/uncomment this line to enable MELPA Stable if desired.  See `package-archive-priorities`
  ;; and `package-pinned-packages`. Most users will not need or want to do this.
  (add-to-list 'package-archives (cons "melpa-stable" (concat proto "://stable.melpa.org/packages/")) t)
  )
(package-initialize)

;; M-x package-refresh-contents or M-x package-list-packages to ensure that Emacs has fetched the MELPA package list
;; cl - Common Lisp Extension
(require 'cl)

;; Add Packages
(defvar my/packages '(
	;; --- Auto-completion ---
	company
	;; --- Better Editor ---
	hungry-delete
	swiper
	counsel
	smartparens
	;; --- Themes ---
	monokai-theme
	;; solarized-theme
	) "Default packages")

(setq package-selected-packages my/packages)

(defun my/packages-installed-p ()
    (loop for pkg in my/packages
	   when (not (package-installed-p pkg)) do (return nil)
	   finally (return t)))

(unless (my/packages-installed-p)
     (message "%s" "Refreshing package database...")
     (package-refresh-contents)
     (dolist (pkg my/packages)
       (when (not (package-installed-p pkg))
	 (package-install pkg))))

;; Find Executable Path on OS X
(when (memq window-system '(mac ns))
   (exec-path-from-shell-initialize))

;; 自动括号匹配
(add-hook 'emacs-lisp-mode-hook 'show-paren-mode)

;; 高亮当前行 void function
;; (global-h1-line-mode 1)

(load-theme 'monokai 1)
(add-to-list 'load-path "~/emacs-application-framework")
(require 'eaf)
