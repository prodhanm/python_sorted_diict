posts = {
    "2354": {
        "user": "Python51",
        "content": "I really like this",
        "likes": 35
    },
    "2355": {
        "user": "Loops55",
        "content": "Awesome",
        "likes": 123
    },
    "2356": {
        "user": "Coder58",
        "content": "This is really good",
        "likes": 27
    }
}

def get_likes(d):
    return d["likes"]

def main():
    for post in sorted(posts.values(), key=get_likes, reverse=True):
        print(post["content"])

if __name__ == "__main__":
    main()