from django.db import models


# Create your models here.
class Company(models.Model):
    """
    Company model
    """
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    about = models.TextField(blank=True)
    facebook = models.CharField(max_length=250)
    twitter = models.CharField(max_length=250)
    youtube = models.CharField(max_length=250)

    class Meta:
        verbose_name = "company"
        verbose_name_plural = "company"
        db_table = "company"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("company_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    """
    Post model
    many=to=many relationship with Category model
    """

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True)
    body = models.TextField()
    pub = models.BooleanField()
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    categorys = models.ManyToManyField("Category")

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["-pub_date", "title"]
        db_table = "posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    """
    Category model
    """

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["name"]
        db_table = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    """
    Comment model
    many-to-one relationship with Post model
    """

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    comment = models.TextField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})
