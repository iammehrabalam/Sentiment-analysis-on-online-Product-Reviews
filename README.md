# Opinion or Sentiment analysis on online Product Reviews
Given opinionated reviews i.e, a set of reviews about a product classify it either positive or negative.
## Usages
```python
from sentiment import TrainingAndTesting 
'''
below used variables and info
---------
traning_data: your traning data (list or tuple of document)
traning_label: label of corresponding traning_data (list or tuple of lables)
testing_data: your traning data (list or tuple of document)
test_label: label of testing_data (list or tuple)
'''
train_and_test_object = TrainingAndTesting()
train_and_test_object.train_me(traning_data, traning_label)
test_result = train_and_test_object.test_me(testing_data)
print TrainingAndTesting.model_evaluation(test_result, test_label)

'''
output of model_evalution
{
    'Accuracy': some value in percentage,
    'Correcly predicted': some value,
    'Error rate': some value in percentage,
    'Recall': some value,
    'Total Test data:': total no of test data,
    'Wrong Predicted': some value,
    'f1 score': some value,
    'precision': some value 
}
'''
```
## Get reviews from amazon.com on given query for testing
##### inside config.py change
```
AMAZON_ACCESS_KEY_ID = "your amazon access key id"
AMAZON_ACCESS_SECRET_KEY = "your amazon secret key"
AMAZON_ASSOCIATE_TAG = "your amazon associate tag"
```
```python
from sentiment import TrainingAndTesting 
'''
below used variables and info
---------
query: get reviews related to this query eg. computer engineering books
total_reviews: total no of reviews you want to extract
reviews_rating: reviews_rating[0] is list conatin reviews and reviews_rating[1] is list contain rating of corresponding reviews in  reviews_rating[0]
'''
obj = TrainingAndTesting()
reviews_rating = obj.get_amazon_data( query='python books', total_reviews=100) 

```
## Accuracy on Amazon.com reviews (Avg)
- 85% accuracy on 5 star rating reviews
- 75% accuracy on 4 star rating reviews
- 70% accuracy on 3 star and 2 star rating reviews
- 85% accuracy on 1 star rating reviews
