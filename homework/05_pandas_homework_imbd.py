'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies

movies = pd.read_csv("imdb_1000.csv")

# check the number of rows and columns

movies.shape

# check the data type of each column

movies.dtypes

# calculate the average movie duration

movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies

movies.sort('duration').head(1) 
movies.sort('duration').tail(1) 

# create a histogram of duration, choosing an "appropriate" number of bins

movies.duration.hist(bins=6)

# use a box plot to display that same data

movies.duration.plot(kind="box")

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings

movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels

movies.content_rating.value_counts().plot(kind="bar", title="title")
plt.xlabel("Content Rating")
plt.ylabel("Frequency")

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP

movies.content_rating.replace(["NOT RATED", "APPROVED", "PASSED", "GP"], "UNRATED", inplace=True)

# convert the following content ratings to "NC-17": X, TV-MA

movies.content_rating.replace(["X", "TV-MA"], "NC-17", inplace=True)

# count the number of missing values in each column

movies.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values

movies[movies.content_rating.isnull()]
movies.content_rating.fillna("UNRATED", inplace=True)

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours

movies[movies.duration>=120].star_rating.mean()

movies[movies.duration<120].star_rating.mean()

# use a visualization to detect whether there is a relationship between duration and star rating

movies.plot(kind="scatter",x="duration", y="star_rating")

# calculate the average duration for each genre

movies.groupby("genre").duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration

movies.groupby("content_rating").duration.mean().plot(kind="bar")

# determine the top rated movie (by star rating) for each genre

movies.sort("star_rating", ascending=False).groupby("genre").first()

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates

#there are four titles that are duplicated
movies.title.duplicated().sum()
#these are they
movies[movies.title.duplicated()]
#you can check each and see that they are not duplicates (easiest to look at actor list)
movies[movies.title == "The Girl with the Dragon Tattoo"]
#this shows that no rows are fully duplicated
movies.duplicated().sum()

# calculate the average star rating for each genre, but only include genres with at least 10 movies

movies.groupby('genre').filter(lambda x: len(x) >= 10 ).groupby("genre").star_rating.mean()

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
