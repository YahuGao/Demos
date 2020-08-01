(require 'conda)
;; if you want interactive shell support, include:
(conda-env-initialize-interactive-shells)
;; if you want eshell support, include:
(conda-env-initialize-eshell)
;; if you want auto-activation (see below for details), include:
(conda-env-autoactivate-mode t)
(custom-set-variables
 '(conda-anaconda-home "/home/yahu/anaconda3/"))
(setq conda-env-home-directory (expand-file-name "~/anaconda3/"))
;; End of file
(provide 'config-conda)
