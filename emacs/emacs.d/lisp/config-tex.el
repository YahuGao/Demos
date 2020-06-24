(setq TeX-parse-self t)
(setq-default TeX-master nil)
(add-hook 'LaTeX-mode-hook
	  (lambda ()
	    (add-to-list 'TeX-command-list '("XeLaTeX" "%`xelatex%(mode)%' %t" TeX-run-TeX nil t))
	    (add-to-list 'TeX-command-list '("HtLaTex" "%`htlatex%(mode)%' %t" TeX-run-TeX nil t))
	    (setq TeX-command-default "XeLaTeX")))

(defun my-LaTeX-mode()
  (add-to-list 'TeX-view-program-list '("firefox" "firefox --new-window %o" "firefox"))
  (setq TeX-view-program-selection '((output-pdf "firefox")))
  )
(add-hook 'LaTeX-mode-hook 'my-LaTeX-mode)

;; End of file
(provide 'config-tex)
