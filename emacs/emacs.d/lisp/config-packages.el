
;; load theme
(load-theme 'monokai 1)
;; >>> Configuration of MARKDOWN >>>
(require 'markdown-mode)
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
;; <<< Configuration of MARKDOWN <<<

;; >>> Configuration of python IDE >>>
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
;; <<< Configuration of python IDE <<<

;; >>> configuration of TEX >>>
;; <<< configuration of TEX <<<
(provide 'config-packages)
