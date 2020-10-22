### tasks

* Model for the Blog app with user as foreign key.
```
class Post(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
```
* added function based list, detail view. (use api_view decorator)

<b>post_list_view</b>
* action - 
    1. get - get the list of all the posts.
    2. post - can add any post if authenticated.

<b>post_detail_view</b>
* action - 
    1. get - get the details of the post. arg has to be provided in url.
    2. put - can update the content and title of the post.
    3. delete - can delete the specified post.
    
* added project level permission(prebuilt) `['rest_framework.permissions.IsAuthenticated']`
* added view level permission(custom) `[IsAuthorOrReadOnly,]`
 

