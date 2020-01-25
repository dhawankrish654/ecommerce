from django.db import models

# Create your models here.
#db_column='cname'
class Customer(models.Model):
    cust_name=models.CharField(max_length=50)
    cust_email=models.EmailField(default='na')
    cust_mobile=models.CharField(max_length=12)
    cust_role=models.CharField(max_length=50)
    cust_password = models.CharField(max_length=50)
    class Meta:
        db_table="customer"
class Category(models.Model):
    category_id=models.IntegerField(primary_key=True)
    category_name=models.CharField(max_length=100)
    class Meta:
        db_table="category"
    def __str__(self):
        return self.category_name
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_details=models.TextField(default='na')
    product_price=models.FloatField(default=0)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to='product_img',blank=True)
    class Meta:
        db_table="product"
class Orders(models.Model):
    order_dt=models.DateField(auto_now=True)
    order_amount=models.FloatField(default=0)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    class Meta:
        db_table="orders"
class Order_Details(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty=models.IntegerField(default=0)
    class Meta:
        db_table="order_details"
class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100,default='na')
    product_price=models.FloatField(default=0)
    class Meta:
        db_table="cart"
