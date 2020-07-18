;; ====================================
;; Development Setup
;; ====================================
;; Enable elpy
(elpy-enable)
;; Enable Flycheck
(when (require 'flycheck nil t)
  (setq elpy-modules (delq 'elpy-module-flymake elpy-modules))
  (add-hook 'elpy-mode-hook 'flycheck-mode))
;; Enable autopep8
(require 'py-autopep8)
(add-hook 'elpy-mode-hook 'py-autopep8-enable-on-save)
;; Enable anaconda-mode
;; (add-hook 'python-mode-hook 'anaconda-mode)
;; End of file
(provide 'config-python)
