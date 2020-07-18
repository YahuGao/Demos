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
  (add-to-list 'package-archives (cons "melpa" (concat proto "://melpa.org/packages/")) t)
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
	monokai-theme       	;; --- Themes ---
	solarized-theme
        markdown-mode
        grip-mode
	elpy                    ;; Emacs Lisp Python Environment
	flycheck                ;; On the fly syntax checking
	py-autopep8             ;; Run autopep8 on save
	jupyter
	magit                   ;; Git integration
	auctex                  ;; Write and formate tex files
	reftex                  ;; Help inserting labels, references and citations of tex
	ivy-bibtex              ;; Help insert citations
	pdf-tools               ;; Viewing and interacting with pdf within emacs
        ein
        websocket
        request
        auto-complete
        smartrep
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

(require 'config-packages)
;; 文件末尾
(provide 'init-packages)
