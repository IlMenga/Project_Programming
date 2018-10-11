# Housekeeping
args <- commandArgs(trailingOnly = TRUE)
in_path <- 'Code/Latex.Rmd'
in_wd <- substr(in_path,1,5)
out_path <- 'Results/Latex.pdf'
out_path <- substr(out_path,1,8)
ifelse(!dir.exists(out_path), dir.create(out_path), FALSE)

# Change directory
setwd(in_wd)

# Load packages
require(knitr)
require(markdown)

# Create .md, .html, and .pdf files
knit('Latex.Rmd')
markdownToHTML('Latex.md', 'Latex.html', options=c("use_xhml"))
system('pandoc -s Latex.html -o ../Results/Latex.pdf')

setwd('../')

