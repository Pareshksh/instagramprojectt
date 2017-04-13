import requests

ACCESS_TOKEN='4991067857.0740b1d.9a87d2e500e7480c8249e0ab7ee39657'
B_URL = 'https://api.instagram.com/v1/'

#This function returns the details of the owner
def owner_info():
    url = B_URL + 'users/self/?access_token=' + ACCESS_TOKEN
    owner_info = requests.get(url).json()
    print ("The instagram owner id is:"+owner_info['data']['id'])
    print ("The instagram owner full name is:"+ owner_info['data']['full_name'])
    print("The instagram owner bio is:" + owner_info['data']['bio'])
    print("The instagram owner un is:" + owner_info['data']['un'])

#owner_info()
def get_user_by_un(i_user):
    url=B_URL + 'users/search?q=' + i_user +'&access_token=' + ACCESS_TOKEN
    u_info = requests.get(url).json()
    success = u_info['meta']['code']
    if success==200:
        print ("Sucessfully found user")
    else:
        print ("Unsucessful!! Cannot find user")
    return u_info['data'][0]['id']

#get_user_by_un('pareshkshatriya')
def user_post_id(un):
    uid = get_user_by_un(un)
    url_user = B_URL + "users/" + uid + "/media/recent/?access_token=" + ACCESS_TOKEN  
    rposts = requests.get(url_user).json()
    success = rposts["meta"]["code"]
    for pn in range(0,len(rposts["data"]),1):
        pn
    exact_posts=str(pn)
    print ('we have total '+exact_posts+'posts of :'+un+'\n which post you want to chose')
    pn=input()
    i=int(pn)
    if success == 200:
        print ("Successfully found user id and fetched user's post id ")
    else:
        print ("Unsucessfull!!! plz check user name again")
    return rposts["data"][i]['id']


#this funn is use to do like on users post_id which is getting from  funn <<<user_post_id>>>
def like_on_user_post_id(user_name):
    post_id = user_post_id(user_name)
    Access_token={'access_token':ACCESS_TOKEN}
    url_post_like= B_URL+"media/"+post_id+"/likes"
    like_result=requests.post(url_post_like,Access_token).json()
    success = like_result["meta"]["code"]
    if success == 200:  # checking url
        print ("successfully liked the pic ")
    else:
        print ("unsucessfull plz try again")

def comment_on_user_id(user_name):
    post_id = user_post_id(user_name)  # post_id which is getting from  funn <<<user_post_id>>>
    print ("write comment u want to write \n but rules are \n 1. The total length of the comment cannot exceed 300 characters.\n 2. The comment cannot contain more than 4 hashtags.\n 3. The comment cannot contain more than 1 URL.\n 4. The comment cannot consist of all capital letters.")
    entered_comment = input()
    entered_comment = str(entered_comment)
    url_post_comment = B_URL + "media/"+post_id+"/comments"
    Access_token_Plus_comment = {'access_token': ACCESS_TOKEN, 'text': entered_comment}
    comment_result = requests.post(url_post_comment, Access_token_Plus_comment).json()
    success = comment_result["meta"]["code"]
    if success == 200:  # checking url
        print ("successsfully commented on the pic ")
    else:
        print ("unsucessfull plz try again")


def search_comment_id(user_name):
    post_id=user_post_id(user_name)
    print ("type content related to comment")
    search=input()
    recent_comments=B_URL+"media/"+post_id+"/comments?access_token="+ACCESS_TOKEN
    recent_comments=requests.get(recent_comments).json()
    for i in range (0,len (recent_comments["data"]),1):
        if search in recent_comments['data'][i]['text']:
            print ("comment is found ::")
            print (recent_comments ['data'][i]['text'])
            return recent_comments['data'][i]['id'],post_id
    else:
        print ("comment is not found")
        return

def delete_comment(user_name,media_id):
        comment_id,media_id = search_comment_id(user_name)
        #https://api.instagram.com/v1/media/1486120579122616804_2338013941/comments/17876833795018201?access_token=1993495056.1b2b25a.bbdc1be8c2364ab181433835f5c37520
        success1 = B_URL+"media/"+media_id+"/comments/"+comment_id+"?access_token="+ACCESS_TOKEN
        success=requests.delete(success1)["meta"]["code"]

        if success == 200:  # checking url
            print ("successfully commented on the pic ")
        else:
            print ("Unsuccessful!!! plz try again")



v ="y"
while v =="y":
    owner_info()                                            # calling funn to print owner information
    print("hey type the un from following \n  amritbirsingh345  \n  yashika3990 ")
    user_name = input()
    print("WELCOME TO OUR PAGE \n Enter ch which you want to execute 1:like 2:comment 3:search 4:delete")
    ch=input()
    if ch=="1":
        like_on_user_post_id(user_name)
    elif ch=="2":
        comment_on_user_id(user_name)
    elif ch=="3":
        search_comment_id(user_name)
    elif ch== '4':
        media_id=user_post_id(user_name)
        delete_comment(user_name,media_id)
    else:
        print("you chose wrong")

    print("PRESS Y TO CONTINUE ELSE PRESS ANY OTHER KEY TO EXIT")
    v=input()
