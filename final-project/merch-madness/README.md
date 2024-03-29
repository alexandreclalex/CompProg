# Merch Madness

## Problem Statement

### Problem Description

New York is full of high end stores and boutiques, that sell merchandise that goes for hundreds, or even thousands on the market. Often times, new product drops are accompanied by massive lines of customers, looking to become one of the first to get their hands on a new, limited-edition product when released.

Speaking of limited-edition, Apple has just announced the unveil of their new product, the Apple IPad Air Pro MAX Silver Edition, with limited quantities at their M stores located in the Manhattan area, each with N allocated stock of their new product.

With the news dropping of this new release, a total of P Apple fans randomly scattered around the Mahattan area rush to their nearest Apple store, franticly trying to get one of the newly released products. Each of these individuals is able to move towards their nearest store at the same speed as everyone else, travelling at one block per second. In addition, since the stores are located in the middle of the city, someone can only move either horizontally OR vertically at any point in time.

Employees know that stock is limited, and if people arrive to a store that is out of stock, they will refer the customers to the nearest store with remaining stock. If two stores are equi-distant, they will refer to the store with the lowest ID.

What is the time that it will take for everyone to get their product? 

### Input

The first line will consist of two integers, X and Y, consisting of the width and height of the city in blocks, respectively. Both values will be bounded by 20 <= X,Y <= 1000.

The second line will consist of an integer M, representing the number of stores within the city limits. This will be bounded by 1 <= M <= 100.

The next M lines will consist of four integers, W, X, Y, and N, which are the (X, Y) coordinate of the store with ID W in the city limits, and the capacity N for the total number of items at the store. The X and Y will be bounded within the city limits defined in the first line, and the capacity will be bounded by 0 <= N <= 25.

The next line will consist of an integer P specifying the number of people within the city, followed by P lines consisting of two integers, X and Y, for the (X, Y) coordinates of each person within the city. The X and Y will be bounded within the city limits defined in the first line, and P will be bounded by 1 <= P <= 1000.

### Output

For each test case, output the amount of time (as a whole number) that it will take for everyone to arrive to a store and get their product. 

If there is not enough stock for everyone, print "out of stock". 


## Testing Solutions
All code should be located within the `merch_madness.py` file, within the `execute()` function. Other functions can be called from within this function, but this is the main function to run for testing.

To run the tests, change directory into the `final-project/merch-madness` folder, and run the following:

```
python -m unittest discover
```

This will run all of the unit tests, all (except the last one currently) will fail if the solution is incorrect.