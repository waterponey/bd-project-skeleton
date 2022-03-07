# Skeleton for the big data project

## Goal of the project

Wrangle data and train a model using different libraries like you're a real datascientist

## Steps

For this project, there will be no "walkthrough", you will be free to do your own machine learning, as long as you follow these guidelines:

1. Choose **any** dataset from [http://archive.ics.uci.edu/ml/index.php] or [kaggle datasets](https://www.kaggle.com/datasets) or [data.gouv](https://www.data.gouv.fr/fr/) or outside. I need to have access to the dataset to validate the project. It might not be public.
2. Download the dataset file and upload to Databricks. If you want to use another dataset, it's okay as long as I can access it.
3. Do a preliminary exploration using pandas on a sample of the dataset (optional but recommended)
    1. You might want to start making hypothesis.
    2. Please worry about the data quality and any kid of bias within
    3. PLEASE WORRY ABOUT BIAS IN DATA
    4. Make a **pretty** plot about any kind of intuition.
4. Explore it using Spark DataFrames, including **at least** the following steps:
    1. Reading the file into a DataFrame
    2. Running some aggregations and explorations using DataFrame functions
    3. The fancier, the better
5. Your solution notebook must have a part using MLlib, including **at least** the following steps:
    1. Converting into MLlib matrix
    2. Applying some statistics with the  MLlib's API
    3. Learning a classification or regression model
    4. Applying the model to the test data and computing the errors
6. You'll also train another model using Pipelines:
    1. Creating a pipeline with **at least** one feature extraction/manipulation and one model estimator
    2. Fitting the pipeline to the training data
    3. Applying the model to the test data and computing the errors
7. (OPTIONAL) Finally you will have to apply a model built with a third party ML library like tensorflow or pytorch. The endpoint here is to have you mix different framework on the same project. For instance you can call one framework from another like [tune scikit-learn meta-parameters using spark](https://docs.databricks.com/spark/latest/mllib/third-party-libraries.html#scikit-learn). Or do something different using tensorflow or pytorch. You can use different notebook provider (colab & databricks). When you do that, please prefix the name of your notebook by the name of the cloud provider.

8. No report needed !! Just add some comment as part of the Notebook. The notebook should be self-sufficient. I'm expecting a short written analysis (and you should know that "We found nothing after testing *this* and *that*" is already a valuable result), but also some plots. You can use any library (matplotlib, bokeh...). Just be sure to [watch this video first](https://www.youtube.com/watch?v=xAoljeRJ3lU)

## I CAN'T GRADE CODE THAT DOESN'T RUN !! So make SURE it runs

To grade this I will :

1. run the notebooks
2. run the other pieces of code
3. read the code (so you can add meaningfull comment even on part that are not running well)
4. grade the overall code quality as well as complexity
5. grade the overall presentation of the repository

If nothing is running, I'll stop at step 1 or 2. Which won't be good for you.

## Notes

- Don't forget to split your data into training and test (and validation if you want) sets
- Your code should be readable. **DO NO FORGET [PEP8](https://www.python.org/dev/peps/pep-0008/)**
- You can do this project in groups of **4 members**
- All submissions after the deadlines won't be considered
      - **It's much better to submit an incomplete solution than nothing at all!**
- If you have any question or problem, don't hesitate to send me an e-mail; I try to answer as quickly  possible (usually under 24h). If not you can ask me on gitter.
- If you want to use this project as a display of your skills, you can upload it on github when you're done. It's a good opportunity (and for some tech companies, a github can be better than a resume). If you're not sure how, let me know, I'll help you and give you advise on how to make it look pretty. **This could be really important for you if you're targeting tech jobs**
      - Even if it seems obvious, **do not cheat**. I won't be nice if I suspect it.
  
## Resources:

- [Spark MLlib guide](https://spark.apache.org/docs/latest/ml-guide.html)
- [Databricks MLlib guide](https://docs.databricks.com/spark/latest/mllib/index.html#)
- [pyspark MLlib RDD API docs](https://spark.apache.org/docs/latest/api/python/pyspark.mllib.html)
- [pyspark MLlib DataFrame API docs](https://spark.apache.org/docs/latest/api/python/pyspark.ml.html)
- [pyspark complete docs](https://spark.apache.org/docs/latest/api/python/)
- [Course Homepage](https://waterponey.github.io/SparkCourse/)
  
### May the force be with you
