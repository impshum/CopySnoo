import praw
import configparser
import pickledb
import time


class C:
    W, G, R, P, Y, C = '\033[0m', '\033[92m', '\033[91m', '\033[95m', '\033[93m', '\033[36m'


def main():
    posts_db = pickledb.load('data/posts.db', False)
    config = configparser.ConfigParser()
    config.read('conf.ini')
    reddit_user = config['REDDIT']['reddit_user']
    reddit_pass = config['REDDIT']['reddit_pass']
    client_id = config['REDDIT']['client_id']
    client_secret = config['REDDIT']['client_secret']
    copy_from_subreddit = config['REDDIT']['copy_from_subreddit']
    copy_to_subreddit = config['REDDIT']['copy_to_subreddit']
    future_only = int(config['REDDIT']['future_only'])
    test_mode = int(config['REDDIT']['test_mode'])
    flair_css_class = config['REDDIT']['flair_css_class']
    flair_text = config['REDDIT']['flair_text']

    reddit = praw.Reddit(
        username=reddit_user,
        password=reddit_pass,
        client_id=client_id,
        client_secret=client_secret,
        user_agent='CopySnoo (by u/impshum)'
    )

    if test_mode:
        t = f'{C.R}TEST MODE{C.Y}'
    else:
        t = ''

    print(f"""{C.Y}
╔═╗╔═╗╔═╗╦ ╦╔═╗╔╗╔╔═╗╔═╗
║  ║ ║╠═╝╚╦╝╚═╗║║║║ ║║ ║  {t}
╚═╝╚═╝╩   ╩ ╚═╝╝╚╝╚═╝╚═╝  {C.C}v1.0{C.W}
    """)

    c = len(posts_db.getall())
    start_time = time.time()

    for submission in reddit.subreddit(copy_from_subreddit).stream.submissions():
        if future_only:
            if submission.created_utc >= start_time:
                go = True
            else:
                go = False
        else:
            go = True

        if go:
            id = submission.id
            title = submission.title
            body = submission.selftext

            if not posts_db.exists(id):
                if not test_mode:
                    posts_db.set(id, 0)
                    posts_db.dump()
                    new_id = reddit.subreddit(copy_to_subreddit).submit(
                        title=title, selftext=body)
                    new_submission = reddit.submission(id=new_id)
                    new_submission.mod.approve()
                    new_submission.mod.flair(text=flair_text, css_class=flair_css_class)
                c += 1
                print(f'{C.G}{c}: {id}{C.W}')
            else:
                print(f'{C.P}{id}{C.W}')


if __name__ == '__main__':
    main()
