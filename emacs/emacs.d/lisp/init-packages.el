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
	monokai-theme       	;; --- Themes ---
	solarized-theme
        markdown-mode
        grip-mode
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

;; load theme
(load-theme 'monokai 1)
(require 'markdown-mode)
;; -----------------------------Configuration of grip-mode-------------------------------------
;; Make a keybinding: `C-c C-c g'
(define-key markdown-mode-command-map (kbd "g") #'grip-mode)
;; Or start grip when opening a markdown/org buffer
(add-hook 'markdown-mode-hook #'grip-mode)
(add-hook 'org-mode-hook #'grip-mode)
;; Path to the grip binary
(setq grip-binary-path "/usr/bin/grip")
;; A GitHub username for API authentication
(setq grip-github-user "YahuGao")
;; A GitHub password or auth token for API auth
(setq grip-github-password "c08aea33e429699054142cf85bf8e0c0bc63bbb8")
;; When nil, update the preview after file saves only, instead of also
;; after every text change
(setq grip-update-after-change nil)
;; Use embedded webkit to previe
;; This requires GNU/Emacs version >= 26 and built with the `--with-xwidgets`
;; option.
(setq grip-preview-use-webkit t)
;; -----------------------------Configuration of grip-mode-------------------------------------

;; 文件末尾
(provide 'init-packages)
