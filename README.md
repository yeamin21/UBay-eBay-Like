# ubayy/UBay 

## an ebay like ecommerce site where users can post items and other users can bid on the item. If the auction time expired the maximum bid wins the auction.
## live demo: https://ubayy.herokuapp.com/

## admin dashboard: https://ubayy.herokuapp.com/admin/

#### admin email: ```admin@mail.com```
#### admin password: ```root```
### Homepage

![product page](https://github.com/yeamin21/ubayy/blob/main/docs/Screenshot%202021-05-29%20093842.png?raw=true)

### Admin Bidding Management Page

![admin page](https://github.com/yeamin21/ubayy/blob/main/docs/Screenshot%202021-05-29%20093814.png?raw=true_)


### Activity Diagram 


![admin page](https://github.com/yeamin21/ubayy/blob/main/docs/Blank%20diagram.png?raw=true)


## Development Steps and challenges:

#### Step 1: Creating basic user authentication

user logs in using his/her email only. If no existing user then the system creates new user automatically and redirects the user to the home page.

#### Step 2: User Creates new item

logged in user can create new auction post which contains product name, description, minmum bid and auction end time. user cant bid on his own item. Newly listed items and all items show in the users listing panel.

#### Step 3:

Users can place bid on items posted by others. The bid can be placed if its more than the last bid. Bid placed show in a table containing list of bids. If the user has existing bid on a specific item any new bid updates the previous bid.

#### Step 4:

If auction time ends the item detail page shows the winner of the bid.


#### Step 5:

Admin shows number of bid placed and number of product added by date in a bar chart. It also shows total active bid amount. 

##### Challenges:
  * making chart
  * writing complex query - 
##### Solution: 
  * used chart.js and custom template to show bar chart on admin page.
  * followed djnago official documentation to write complex queries.
  
  
#### Step 6: 

##### Challenges:
  * Making everything preety
##### Solution:
  * Used html, css to make the webapp preety
#### Problems not yet fixed:
  * Not responsive

#### Step 7: deploying in heroku

##### Challenges:
  * Deploying the webapp in heroku
 
##### Solution:
  * Used heroku CLI to deploy the app in heroku
  * ran python commands using 'heroku run -a ubayy python manage.py *.....*'

#### Problem not yet fixed:
  * chart and admin panel edits not added to  heroku

#### Step 8:

##### Challenges:
  * writing README.md
  
##### Solution:
  * used git readme editor
  


