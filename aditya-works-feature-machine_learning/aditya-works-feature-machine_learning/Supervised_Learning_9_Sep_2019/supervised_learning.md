
#### Broadly there are 3 Types of Machine Learning Algorithms
1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning \
There is also an algorithm called as semi-supervised Learning

#### 1. Supervised Learning 
In Supervised learning we are given a data set and already
know what our correct output should look like, having the idea
that there is a relationship between the input and the output.

* Supervised learning problems are categorized into "regression" and
"classification" problems. 
* In a regression problem we are trying to predict the results with 
a continuous output, meaning that we are trying to map input variable
to some continuous function.
* In a classification problem, we are instead trying to 
predict results in discrete output. In other word
we are trying to map input variables into discrete categories.

###### Example 1 :
[Supervised_Example](https://i.imgur.com/EsYWrER.png)

* Given data about size of houses on the real estate market, try to predict
their price. Price has a function of size which is a continuous 
output, so this i a regression problem.
* We could turn this example into a classification problem 
by instead making our output about whether the house "sells" for 
more or less than the asking price.


###### Example 2: 
* Regression- Given a picture of a person, we have to predict their age on the basis of the given picture.
* Classification - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign

#### Unsupervised Learning
It allows us to approach problem with little or no idea
what our results should look like. we can derive structure from 
where we don't necessarily know th effect of the variables.
* We can derive this structure by clustering the data based 
on the prediction results.

###### Example:
* Clustering : Take a collection of 1,000,000 different genes, and find a way to automatically group these 
genes into group that are somehow similar or related by different variables, such as lifespan, location, roles
and so on.\
[unsupervised_example](https://i.imgur.com/4yMS7t0.png)

#### Reinforcement Learning 
* Reinforcement learning is the training of machine learning models
to make sequence of decisions.
* In reinforcement learning an artificial intelligence faces a game-like
situation.
* The computer employs trial and error to come up with a soultion
to the problem. 
* To get the machine to do what the programmer wants, the artificial
intelligence gets either rewards or penalties for the action its performs
* Its goal is to maximize the total reward.

###### Example 
[Reinforcement](https://i.imgur.com/PPlmGiT.png)


#### Semi-Supervised Learning
* In this type of learning the algorithm is trained upon a combination
of learning, the algorithm is trained upon a combination of labeled
and unlabeled data.
* This combination will contain very small amount of labeled data and a 
very large amount of unlabeled data.

###### Example
[Semisupervised](https://i.imgur.com/1HtwgDm.png)

#### Difference Between Supervised , Unsupervised and Reinforcement
|  Parameter	| Supervised 	| Unsupervised 	| Reinforcement 	|
|---	|---	|---	|---	|
| Definition 	|  It is a method in which we teach the machine using labeled data	| In this machine is trained on unlabelled data without any guidance 	| In this type of learning the program learns from the feedback and rewards  	|
| Type of problem 	| Regression, Classification 	| Association, Classification 	| In this input itself depend on the action we take 	|
|  Type of data	| Labeled Data 	| UnLabeled Data 	| No predefined Data 	|
|  Training	| External Supervision 	| No Supervision 	| No Supervision 	|
| Aim 	| Forecast Outcome 	| Discover underlying Patterns 	| Learn Series of action  	|
|  Approach	| Map labeled input to know the output 	| Understands patterns and discover output  	| Follow Trail and Error Method 	|
| Output Feedback 	| Direct Feedback 	| No Feedback 	| Reward System 	|
| Popular Algorithm 	| Linear and LogisticReg, Support vector machine,K nearest neighbour,random forest 	| k-means, Apriori, C- Means 	| Q-Learning, SARSA 	|

#### Types of Supervised Algorithms
###### 1.Regression 

a. Linear Regression

b. Logistic Regression

##### 2. Classification

a. Two Class Classification

b. Multi Class Classification

##### Why do we use Regression Analysis ?
* Let's say, you want to estimate growth in sales of a company
based on current economic conditions.
* You have the recent company data which indicates that the growth in
sales is around two and a half times the growth in the economy.
* Using the insight, we can predict future sales of the company
based in current & past information

There are multiple benefits of using regression analysis.
They are as follows :
1. It indicates the significant relationship between dependent
variable and independent variable.
2. It indicates the strength of impact of multiple independent
variables on a dependent variable.

A. Linear Regression
* In this technique the dependent variable is a continuous,
independent variable can be continuous or discrete and nature 
of regression line is linear.
* Linear Regression establishes a relationship between
dependent variable(Y) and one or more independent variables
(X) using a best fit straight line(also know as regression line). 
* It is represented by an equation Y = a+b*X + e, where 
a is intercept, b is slope of the line and e is error term.
* This equation can be used to predict the value of target 
variable based on given predictor variable.
* The difference between simple linear regression and multiple 
linear regression is that, multiple linear regression has (>1) independent
variables whereas simple linear regression has only 1 independent variable.

B. Logistic Regression
* Logistic regression is used to find the probability of 
event = Success and event = Failure.
* We should use logistic regression when the dependent variable
is binary (0/1, True/False, Yes/ No) in nature.
* Here the value Y ranges from 0 to 1 and it can represented by
the following equation.
```
odds= p/ (1-p) = probability of event occurrence / probability of not event occurrence
ln(odds) = ln(p/(1-p))
logit(p) = ln(p/(1-p)) = b0+b1X1+b2X2+b3X3....+bkXk
```
Above, p is the probability of presence of characteristic of interest.
A equation that you should ask here is "Why have we used log in the 
equation ? 



#### Types of Unsupervised Algorithms

###### 1. Clustering :
* Clustering  is the task of dividing the population or data
points into a number of groups such that data points in the same 
groups are more similar to other data points in the same group and dissimilar
to the data points in other groups.
* It is basically a collection of objects on the basis of similarity 
and dissimilarity between them.

###### Clustering Methods : 
1. Density - Based Methods 
2. Hierarchical Based Methods
3. Partitioning Methods
4. Grid Based Methods

###### Clustering Algorithms
* K-means clustering algorithm - It is the simples unsupervised
learning algorithm that solves clustering problem K-means algorithm
partition n observations into k clusters where each observation belongs
to the cluster with the nearest mean serving as a prototype of 
the cluster. 


##### Working of Linear Regression and Logistic Regression


#### Difference Between Linear Regression and Logistic Regression
| Parameter 	| Linear Regression 	| Logistic Regression  	|
|---	|---	|---	|
|  Basic	| The data is modelled using  a staight line  |The probabiliy of some otained event is represented as a linear function  	| 
| Relationship Between Dependent and independent varaible 	| Is required  	| No required 	|
| The independent varaible  	| Could be correlated with each other 	| Should not be correalted with each other  	|

