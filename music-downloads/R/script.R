library(ggplot2)
library(gridExtra)

million <- function(x) {
	x / 1000000
}

df <- read.csv("digital-sells.csv")

df$Label <- df$Total.Digital.Downloads / 1000000

df$Label <- paste(as.character(df$Label), " Mi")

p <- ggplot(data=df, aes(x=reorder(Music.Artist, Total.Digital.Downloads), y=Total.Digital.Downloads))

p <- p + geom_bar(stat="identity", fill="#FF6666")

p <- p + geom_text(aes(label=Label), position="stack", hjust = -0.25, size = 4)

title <- "Total Music Downloads of Various Artists"

p <- p + labs(x="Music Artist", y="Total Downloads in Millions", title=title)

p <- p + coord_flip()

p <- p + ylim(0, 160000000)

p <- p + scale_y_continuous(labels=million, limits=c(0,150000000))

p <- p + theme(plot.title = element_text(size=32))

p <- p + theme(plot.margin = unit(c(1,1,1,1), "cm"))

p <- p + theme(plot.title = element_text(vjust=10))

p <- p + theme(plot.title = element_text(hjust=1))

ggsave(file="final_plot.png", plot=p, width=10, height=15)