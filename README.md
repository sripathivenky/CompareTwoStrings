# CompareTwoStrings
#### Find similarities between given strings.

How to run the code:
___
#### Requirements:
* Python 3.8
* pip3 
 
````
$bash> git clone https://github.com/sripathivenky/CompareTwoStrings.git
$bash> cd CompareTwoStrings
$bash CompareTwoStrings> pip3 install pipenv
$bash CompareTwoStrings> pipenv install 
$bash CompareTwoStrings> python code/app.py
````

#### Once the server is started:
``````
curl --location --request POST 'http://localhost:9090/v1/compare-two-strings' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text_one": "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'\''ll get points based on the cost of the products. You don'\''t need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'\''ll find the savings for you.",
    "text_two": "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'\''ll get points based on the cost of the products. You don'\''t need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'\''ll find the savings for me."
}'
``````

### Running from docker:
```
docker pull  sripathivenky/mywork:stringcompare

docker run -itd -p 9090:9090  sripathivenky/mywork:stringcompare

```


### Bonus:
 I have also added new API v2 that will do similarity comparison based on Cosin Similarity algorithm.

