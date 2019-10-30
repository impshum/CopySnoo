## CopySnoo

Copies submissions from chosen subreddit to another, approves it and applies flair text and css.

![](https://github.com/impshum/CopySnoo/blob/master/ss1.1.jpg?raw=true)

### Instructions

- Install requirements ```pip install -r requirements.txt```
- Create Reddit (script) app at https://www.reddit.com/prefs/apps/ and get your id, tokens etc
- Edit conf.ini with your details
- Run it ```python run.py```

#### Info

- If ```future_only``` is turned on the bot will only get posts from when it was started. If not it will get the last 100 posts.
- If ```min_score``` is more than 0 it will only get posts with a higher score given.
- If ```min_comments``` is more than 0 it will only get posts with a higher amount of comments given.


