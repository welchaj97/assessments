import json, requests, traceback
from json_data import JsonPlaceholderData, JsonCommentData


class JsonPlaceholderSearch:
    
    # for the instantiation of the class, I set the URLS for the various API endpoints for ease of access/use
    def __init__(self):
        self.BASE_URL = "https://jsonplaceholder.typicode.com"
        self.POSTS_URL = self.BASE_URL + "/posts"
        self.COMMENTS_URL = self.BASE_URL + "/comments"
        self.USERS_URL = self.BASE_URL + "/users"
     
    # created an all_posts method using the base url and returned the data 
    def get_all_posts(self):
        response = requests.get(self.POSTS_URL)
        response.raise_for_status()
        data = response.json()
        return data
    
    # created a single post method with the post number as an input value
    def get_single_post(self, num_post):
        # using try/except in case of error or incorrect/not found post number 
        try:
            response = requests.get(self.POSTS_URL + '/' + str(num_post))
            response.raise_for_status()
            post_json = response.json() if response and response.status_code == 200 else None
            # setting header and encoding so that it can be displayed to meet success criteria posted
            headers = response.headers
            encoding = response.encoding
            # setting the post data so that it can be used for the JsonPlaceholderData class that I created
            userId = post_json['userId']
            id = post_json ['id']
            title = post_json['title']
            body = post_json['body']
            # decided to use a data class here to hold all the information and make it easier to access, and it was not defined in
            # the success criteria what needed to be used specifically 
            single_post = JsonPlaceholderData(headers, encoding, userId, id, title, body)
            return single_post
        # trying to catch any potential errors and then raise the error back if it passed through 
        except (KeyError, AttributeError):
            print(f"Post {num_post} does not exist!")
        except Exception:
            raise
  
        
    def get_post_by_user(self, userId):
        # trying to make a GET request for a specific users posts that will be passed into the method
        try:
            user_posts = requests.get(self.USERS_URL + f'/{userId}/posts')
            user_posts.raise_for_status()
            post_data = user_posts.json()
            return post_data
        # trying to catch any potential errors and then raise the error back if it passed through 
        except (KeyError, AttributeError): 
            print(f"No posts for user {userId} or the user does not exist!")
        except Exception:
            raise
            
    def get_comments_by_user(self, userId):
        try:
            response = requests.get(self.COMMENTS_URL + f'/{userId}')
            response.raise_for_status()
            json_data = response.json() if response and response.status_code == 200 else None
            return json_data
        # trying to catch any potential errors and then raise the error back if it passed through 
        except (KeyError, AttributeError):
            print(f"No comment(s) for {userId} or the user does not exist, please try again")
        except Exception:
            raise
        