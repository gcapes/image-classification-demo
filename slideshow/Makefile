theme=mywhite
reveal=reveal.js-master
theme_dir=${reveal}/dist/theme
theme_css=${theme_dir}/${theme}.css
theme_regex='${theme_dir}/.*\.css'
previous_theme=$(shell ack -o ${theme_regex} index.html)

.PHONY: all
all: slides show

.PHONY: slides
slides: index.html

.PHONY: switch_theme
switch_theme:
ifneq (${previous_theme}, ${theme_css})
	@echo previous_theme: ${previous_theme}
	@echo theme_css: ${theme_css}
	touch ${theme_css}
endif

${theme_css}: switch_theme

index.html: slides.md Makefile ${theme_css}
	pandoc -t revealjs -s -o $@ $< -V revealjs-url=./${reveal} -V theme=${theme}

.PHONY: show
show: index.html
	google-chrome $<
