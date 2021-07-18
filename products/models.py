from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)
    class Meta: #테이블 이름 지정
        db_table = 'menus' #안 쓰면 products_menus라고 컬럼이름 자동 생성
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, default='')
    #default에러가 떠서 디폴트를 추가했다 #외래키 쓸 때 장고가 알아서 _id를 붙여서 데이터베이스에 넘겨서 _id를 안 써도 된다.
    class Meta: 
        db_table='categories' 
    def __str__(self):
        return self.name

class Product(models.Model):
    korean_name = models.CharField(max_length=45, default='')
    english_name = models.CharField(max_length=45, default='')
    description = models.TextField(max_length=300, default='')
    isnew = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) #cascade : 부모개체가 사라지면 자식도 사라지도록
    class Meta:
        db_table = 'products'
    def __str__(self):
        return self.english_name

class Image(models.Model):
    image_url = models.URLField(max_length=2000)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    class Meta:
        db_table = 'images'

class Allergy(models.Model):
    name = models.CharField(max_length=45)
    products = models.ManyToManyField('Product', through='AllergyProduct')
    class Meta:
        db_table = 'allergies'

class AllergyProduct(models.Model):
    allergy = models.ForeignKey('Allergy',on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    class Meta:
        db_table = 'allergies_products'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sodium_mg = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    protein_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    size_ml = models.CharField(max_length=45,  null=True)
    size_fluid_ounce = models.CharField(max_length=45,  null=True)
    product = models.OneToOneField('Product', on_delete=models.CASCADE)
    class Meta:
        db_table = 'nutritions'