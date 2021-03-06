from django.db import models
from datetime import datetime

# Create a Blog model
#title
#publication date
#text in post
#image
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date

# Add the blog app to settings
#create a migration
#Migrate
#Add to the admin
