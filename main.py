import json, requests
from json_search import JsonPlaceholderSearch

# instantiating a class object 
new_search = JsonPlaceholderSearch()

# success criteria #1 
# retrieving all posts and printing out the total
all_posts = new_search.get_all_posts()
print(len(all_posts))

# getting single post #10 and then using a dictionary to format the requested/required return data
# printing out the resulting data
single_post = new_search.get_single_post(10)
single_post_details = {
    "title" : single_post.title,
    "encoding" : single_post.encoding,
    "X-Powered-By" : single_post.headers['X-Powered-By']
}
print(single_post_details)

# getting posts by userId 7
# printing out the number of posts by user
user_posts = new_search.get_post_by_user(7)
print(len(user_posts))

# getting the comments for userId 8
user_comments = new_search.get_comments_by_user(8)
print(user_comments)
# swapping values for name and email
user_name = user_comments['name'] 
user_email = user_comments['email']
user_comments['name'] = user_email
user_comments['email'] = user_name
# showing the swap took place
print(user_comments)
# reformatting list to JSON
user_comments = json.dumps(user_comments)
# printing new JSON text 
print(user_comments)
# making update using PUT method
user8_comment_url = new_search.COMMENTS_URL + '/8'
data = user_comments
headers ={
    'Content-type': 'application/json; charset=UTF-8',
  }
try:
    r = requests.put(user8_comment_url, headers=headers, data=data)
    print(r.text)
except Exception:
    raise
# attempting to retrieve post 101 and print out title
post101 = new_search.get_single_post(101)
print(post101.title)
