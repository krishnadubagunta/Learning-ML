# Importing Datasets
dataset = read.csv('datasets/Data.csv')

# Splitting the dataset into Train set and Test set
# install.packages('caTools') to install any tools in R

set.seed(123);
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
train_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# # Feature Scaling
# train_set[,2:3] = scale(train_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])