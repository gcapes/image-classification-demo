theme=mywhite
reveal=reveal.js-master
theme_css=${reveal}/dist/theme/${theme}.css
previous_theme=$(shell ack -o ${theme_css} index.html)

.PHONY: all
all: slides show

.PHONY: slides
slides: index.html

.PHONY: switch_theme
switch_theme:
ifneq (${previous_theme}, ${theme_css})
	touch ${theme_css}
endif

index.html: slides.md Makefile ${theme_css} switch_theme
	pandoc -t revealjs -s -o $@ $< -V revealjs-url=./${reveal} -V theme=${theme}

.PHONY: show
show: index.html
	google-chrome $<
