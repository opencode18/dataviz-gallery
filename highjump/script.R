library(ggplot2)

df = read.csv("high-jump.csv")

p = ggplot(df, aes(x=Year, y=Height))+ ylim(1.5, 3) + geom_linerange(aes(x=Year,ymin=1.5, ymax=Height, color=Country),size=2, show.legend=TRUE) + geom_text(aes(label=Height,angle=45),vjust = -0.4, hjust=-0.1)

ggsave("final_plot.png", plot = p, dpi = 400, width = 12, height = 5)
