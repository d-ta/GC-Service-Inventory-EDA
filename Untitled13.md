```
d = read.csv("https://open.canada.ca/data/dataset/3ac0d080-6149-499a-8b06-7ce5f00ec56c/resource/3acf79c0-a5f5-4d9a-a30d-fb5ceba4b60a/download/service_inventory.csv")

```


```
install -c r rpy2
install.packages("tidyverse")
library(tidyverse)
library(ggplot2)
```


```
########## This part code from DANYI #################

d[which(d$fiscal_yr=d$fiscal_yr[1])]
data1=unique(d[which(d$fiscal_yr==d$fiscal_yr[1]),]$department_name_en)
data2=unique(d[which(d$fiscal_yr==d$fiscal_yr[2]),]$department_name_en)
data3=unique(d[which(d$fiscal_yr==d$fiscal_yr[3]),]$department_name_en)

inter=intersect(data1,data2)
dep=intersect(inter,data3)
dep
```


```
d2 = d[,-c(2:4,6:22,29:37)]%>% as_tibble()%>%  #### convert to tbl clss
  mutate(across(online_applications:other_applications, as.numeric))%>% #### convert charistice to numeric 
  group_by(department_name_en, fiscal_yr)%>%  #### group by depar name & fiscal year
  summarise(across(online_applications:other_applications, ~sum(., na.rm = T)))%>% #### summarize the applications
  ungroup%>% 
  mutate(across(online_applications:other_applications, ~./1000 )) %>% #### data scale by 1000 
  mutate(across(fiscal_yr, as.factor))%>%
  filter( department_name_en %in% dep)

```


```
d3 = pivot_longer(d2, -c( "department_name_en", "fiscal_yr"), names_to = "application", values_to = "val") 

ggplot(d3, aes(x = fiscal_yr, y = val, group = department_name_en, color = department_name_en   ))+ 
  geom_line()+
  geom_point()+
  facet_wrap(~ application ) #### multi-panel plots


```


```

```


```

```
