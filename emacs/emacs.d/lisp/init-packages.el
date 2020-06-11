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

;; 文件末尾
（provide 'init-packages)
