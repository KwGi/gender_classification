# gender_classification_challenge-> Finished

##Overview

This is the code for the gender classification challenge for 'Learn Python for Data Science #1' by @Sirajology on [YouTube](https://youtu.be/T5pRlIbr6gg). The code uses the [scikit-learn](http://scikit-learn.org/) machine learning library to train a [decision tree](https://en.wikipedia.org/wiki/Decision_tree) on a small dataset of body metrics (height, width, and shoe size) labeled male or female. Then we can predict the gender of someone given a novel set of body metrics.

##Dependencies

* Scikit-learn (http://scikit-learn.org/stable/install.html)
* numpy (pip install numpy)
* scipy (pip install scipy)

Install missing dependencies using [pip](https://pip.pypa.io/en/stable/installing/)

##Usage

Once you have your dependencies installed via pip, run the script in terminal via

```
python gender_classification.py
```

##Challenge -> finished

Added : AdaBoostClassifier , GaussianNB and QuadraticDiscriminantAnalysis from the sci-kit learn [documentation](http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html) .I determine accuracy using accuracy score from (http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) .
And it calculates  probality  using predict_proba from (http://scikit-learn.org/stable/modules/generated/sklearn.svm.libsvm.predict_proba.html).  

##Credits

Credits for some of the code go to [chribsen](https://github.com/chribsen). I've merely created a wrapper to get people started easily.
