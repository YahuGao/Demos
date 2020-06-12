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

;; 文件末尾
（provide 'init-packages)
