from BlogApp.models import Post
from CommentApp.models import Comment


# Creating Post Records
post1 = Post.objects.create(title="WeeklyReport", content="WeeklyNews", category="R-rated", tags="tag1")
post2 = Post.objects.create(title="MonthlyReport", content="MonthlyNews", category="R-rated", tags="tag2")
post3 = Post.objects.create(title="AnnualyReport", content="AnnualNews", category="R-rated", tags="tag3")

# Updating Post2 title
post2.title="DailyReport"

# Erasing Post1 from Records
post1.delete()

# Creating Comment Records
comment1 = Comment.objects.create(content="Post1 was 100 perent useless compared to post2", author="Unknown Brain",post_id=1)
comment2 = Comment.objects.create(content="Post2 was 100 perent useless compared to post3", author="Unknown Brain",post_id=2)
comment3 = Comment.objects.create(content="Post3 was 100 perent useless compared to post1", author="Unknown Brain",post_id=3)
# Updating Comment Content
comment3.content=("same damn thing")

# Using get method to query based on post_id of comments
query1 = Comment.objects.get(pk=2)


comment1.delete()