# lec5_4_h.R

#install.packages("dplyr")
library(dplyr)

# maps : world map
#install.packages("maps")
library(maps)

# mapdata : more world map 
# install.packages("mapdata")
library(mapdata)

# mapproj : latitude and longitude
#install.packages("mapproj")
library(mapproj)

# ggplot2 : versatile graphics package
# install.packages("ggplot2")
library(ggplot2)

# ggmap : google maps
#install.packages("ggmap")
library(ggmap)

# set working directory
setwd("C:/Users/uvent/source/repos/hustarAI/r-programming/exercise")

# 1. Korea Map 
par(mfrow = c(1, 2),mar=c(2,2,2,2))
map(database = 'world', region = c('South Korea','North Korea'), col='green', fill = TRUE)
title("Korea")
# using mapdata package
map(database = 'worldHires', region = c('South Korea','North Korea'), col='green', fill = TRUE)
title("Korea")

map(database = 'worldHires', region = c('South Korea'), col=7, fill = TRUE)
title("Korea")

colors()


# 2.Italy 
par(mfrow = c(1, 1))
map(database = 'world', region = c('Spain'), col='coral', fill = TRUE)
title("Spain")

# 3. U.S.A using google map 
us.map <- map_data("state")

ggbox <- make_bbox(lon = us.map$long, lat = us.map$lat, f=.1)
us.map.google <- get_map(location = ggbox, maptype = "satellite", source = "google")
map <- ggmap(us.map.google) + 
  labs(title = "USA map")
print(map)

# 4. Korea using google map
# Korea map (kr.map)
world.map <- map_data("world")
kr.map <- world.map %>% filter(region == "South Korea")

ggbox <- make_bbox(lon = kr.map$long, lat = kr.map$lat, f=.1)
kr.map.google <- get_map(location = ggbox, maptype = "satellite", source = "google")
map <- ggmap(kr.map.google) + 
  labs(title = "south korea map")
print(map)

# 5. Dokdo using mapproj package
library(mapproj)
par(mfrow = c(1, 1),mar=c(2,2,2,2))
map('world', proj = 'azequalarea', orient = c(37.24223, 131.8643, 0))
map.grid(col = 2)
points(mapproject(list(y = 37.24223, x = 131.8643)), col = "blue", pch = "x", cex = 2)
title("Dokdo")
# for reading Korean : encoding to UTF-8 
# file menu: Tools_global options_code_saving

# 6. Airport & route data (source : https://www.data.go.kr/)
airport = read.csv("airport.csv")
route = read.csv("route.csv")
head(airport)
head(route)

head(route[order(route$id),])

par(mfrow = c(1, 1),mar=c(2,10,2,10))
# Korea map (kr.map)
world.map <- map_data("world")
kr.map <- world.map %>% filter(region == "South Korea")

# ------------------------------------ #
# Korea map using ggplot
# ------------------------------------ #
ggplot() + 
  geom_polygon(data=kr.map, aes(x=long, y=lat, group=group)) +
  geom_label(data=airport, aes(x = lon, y = lat, label=iata)) +
  labs(title = "south korea airports")

# 7. Domestic airport location : geom_point + geom_label
map + geom_point(data=airport, aes(x=lon, y=lat)) +
  geom_label(data=airport, aes(x = lon, y = lat, label=iata), size=3) +
  labs(title = "south korea airports")


# 8. Domestic airport route : geom_line
map + geom_point(data=airport, aes(x=lon, y=lat)) +
  geom_line(data=route, aes(x=lon, y=lat, group=id)) +
  geom_label(data=airport, aes(x = lon, y = lat, label=iata), size=3) +
  labs(title = "south korea airline routes")

# 9. Assault in US (1973)

# excluding Alaska, Hawaii 
sub.usa <- subset(USArrests,!rownames(USArrests) %in% c("Alaska", "Hawaii"))
# data with State name, Assult count
usa.data <- data.frame(states = rownames(sub.usa), Assault = sub.usa$Assault)

# legend
col.level <- cut(sub.usa[, 2], c(0, 100, 150, 200, 250, 300, 350))
legends <- levels(col.level)
# displaying color for the size  
levels(col.level) <- sort(heat.colors(6), decreasing = TRUE)
usa.data <- data.frame(usa.data, col.level = col.level)
# Map 
par(mfrow = c(1, 1), mar=c(1,1,1,1))
map('state', region = usa.data$states, fill = TRUE, col = as.character(usa.data$col.level))
title("USA Assault map")
legend(-77, 34, legends, fill = sort(heat.colors(6), decreasing = TRUE), cex = 0.7)

help(USArrests)
head(USArrests)



## up to here #####################################

## 10. Korea Public wifi location : stat_density_2d
## Public wifi location
# Public wifi data (source : http://www.ktoa.or.kr/)
wifi = read_csv("wifi.csv")
head(wifi)

# bar chart


ggbox <- make_bbox(lon = kr.map$long, lat = kr.map$lat, f=.1)
kr.map.google <- get_map(location = ggbox, maptype = "satellite", source = "google")
map <- ggmap(kr.map.google) + 
  labs(title = "south korea map")
print(map)

# 10. public wifi location 
map + geom_point(data=wifi, aes(x=lon, y=lat, color=company), size = 1) + 
  labs(title = "south korea public wifi")

# 11. contour line on map
map + stat_density_2d(data=wifi, aes(x=lon, y=lat)) + 
  labs(title = "south korea public wifi")

# gradient
map + stat_density_2d(data=wifi, aes(x=lon, y=lat, fill=..level.., alpha=..level..), 
                      geom='polygon', size=3, bins=50) + 
  scale_fill_gradient(low='white', high='darkblue') +
  scale_alpha(range=c(0.01, 0.8), guide=F) +
  labs(title = "south korea public wifi")


######################################################
# color
# 1 black   2 red   3 green   4 blue   5 cyan   6 magenta   7 yellow   8 gray
####################################################
par(mfrow=c(1, 1))
barplot(rep(1,8), yaxt="n", col=1:10)
# see all color (657 colors)
colors()
# see rgb values for 657 colors
col2rgb(colors()) 
# make table of colors and the corresponding RGB
cc1<-cbind(colors(), t(col2rgb(colors()))) 

# select colors including "cyan" 
colors()[grep("cyan", colors())]

colors()[grep("sky", colors())]

