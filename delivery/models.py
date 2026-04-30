from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.username
    

class Restaurant(models.Model):
    name = models.CharField(max_length = 20)
    picture = models.URLField(max_length = 200, default='https://images.travelandleisureasia.com/wp-content/uploads/sites/2/2025/05/02141004/aesthetic-rest-hero.jpeg?tr=w-1200,q-60')
    cuisine = models.CharField(max_length = 200)
    rating = models.FloatField()


class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    vegeterian = models.BooleanField(default=False)
    picture = models.URLField(max_length=400, default='https://www.indiafilings.com/learn/wp-content/uploads/2024/08/How-to-Start-Food-Business.jpg')


class Cart(models.Model):
    customer = models.ForeignKey(user, on_delete= models.CASCADE, related_name='cart')
    items = models.ManyToManyField("Item",related_name='carts')

    def total_price(self):
        return sum(item.price for item in self.items.all())
    
from django.db import models

class Order(models.Model):
    customer = models.ForeignKey('user', on_delete=models.CASCADE)
    total_price = models.FloatField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Confirmed', 'Confirmed'),
            ('Delivered', 'Delivered')
        ],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name