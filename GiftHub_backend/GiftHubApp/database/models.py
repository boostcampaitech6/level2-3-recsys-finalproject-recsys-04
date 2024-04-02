from django.db import models

class Genderinference(models.Model):
    product_id = models.CharField(max_length=500, blank=True, null=True)
    product_name = models.CharField(max_length=500, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    num_review = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    product_url = models.CharField(max_length=500, blank=True, null=True)
    new_cat_1_개업선물 = models.IntegerField(blank=True, null=True)
    new_cat_1_결혼기념일선물 = models.IntegerField(blank=True, null=True)
    new_cat_1_새차선물 = models.IntegerField(blank=True, null=True)
    new_cat_1_생일선물 = models.IntegerField(blank=True, null=True)
    new_cat_1_집들이선물 = models.IntegerField(blank=True, null=True)
    new_cat_1_출산선물 = models.IntegerField(blank=True, null=True)
    new_cat_1_취업선물 = models.IntegerField(blank=True, null=True)
    new_cat_1_퇴직선물 = models.IntegerField(blank=True, null=True)
    new_cat_1_합격기원선물 = models.IntegerField(blank=True, null=True)
    new_cat_2_10대남성 = models.IntegerField(blank=True, null=True)
    new_cat_2_10대여성 = models.IntegerField(blank=True, null=True)
    new_cat_2_2030대_남성 = models.IntegerField(db_column='new_cat_2_2030대 남성', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_2_2030대여성 = models.IntegerField(blank=True, null=True)
    new_cat_2_4050대_남성 = models.IntegerField(db_column='new_cat_2_4050대 남성', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_2_4050대_여성 = models.IntegerField(db_column='new_cat_2_4050대 여성', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_2_e쿠폰 = models.IntegerField(blank=True, null=True)
    new_cat_2_가전 = models.IntegerField(blank=True, null=True)
    new_cat_2_과일 = models.IntegerField(blank=True, null=True)
    new_cat_2_꽃 = models.IntegerField(blank=True, null=True)
    new_cat_2_남편선물 = models.IntegerField(blank=True, null=True)
    new_cat_2_데스크테리어 = models.IntegerField(blank=True, null=True)
    new_cat_2_디지털 = models.IntegerField(blank=True, null=True)
    new_cat_2_디지털_가전 = models.IntegerField(blank=True, null=True)
    new_cat_2_리빙_인테리어 = models.IntegerField(db_column='new_cat_2_리빙/인테리어', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_2_문구용품 = models.IntegerField(blank=True, null=True)
    new_cat_2_반려동물 = models.IntegerField(blank=True, null=True)
    new_cat_2_부모님선물 = models.IntegerField(blank=True, null=True)
    new_cat_2_생활용품 = models.IntegerField(blank=True, null=True)
    new_cat_2_세차용품 = models.IntegerField(blank=True, null=True)
    new_cat_2_셀프촬영 = models.IntegerField(blank=True, null=True)
    new_cat_2_손편지 = models.IntegerField(blank=True, null=True)
    new_cat_2_식물 = models.IntegerField(blank=True, null=True)
    new_cat_2_식품 = models.IntegerField(blank=True, null=True)
    new_cat_2_신생아선물 = models.IntegerField(blank=True, null=True)
    new_cat_2_아내선물 = models.IntegerField(blank=True, null=True)
    new_cat_2_영양제 = models.IntegerField(blank=True, null=True)
    new_cat_2_욕실용품 = models.IntegerField(blank=True, null=True)
    new_cat_2_이벤트_파티용품 = models.IntegerField(db_column='new_cat_2_이벤트/파티용품', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_2_인테리어 = models.IntegerField(blank=True, null=True)
    new_cat_2_임산부선물 = models.IntegerField(blank=True, null=True)
    new_cat_2_주방용품 = models.IntegerField(blank=True, null=True)
    new_cat_2_청소용품 = models.IntegerField(blank=True, null=True)
    new_cat_2_케이크 = models.IntegerField(blank=True, null=True)
    new_cat_2_쿠션_방석 = models.IntegerField(blank=True, null=True)
    new_cat_2_키용품 = models.IntegerField(blank=True, null=True)
    new_cat_2_파티용품 = models.IntegerField(blank=True, null=True)
    new_cat_2_편의용품 = models.IntegerField(blank=True, null=True)
    new_cat_2_푸드 = models.IntegerField(blank=True, null=True)
    new_cat_2_향초_디퓨저 = models.IntegerField(blank=True, null=True)
    new_cat_2_홈프레그런스 = models.IntegerField(blank=True, null=True)
    new_cat_2_화장품 = models.IntegerField(blank=True, null=True)
    new_cat_2_환갑_칠순선물 = models.IntegerField(db_column='new_cat_2_환갑/칠순선물', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_e쿠폰 = models.IntegerField(blank=True, null=True)
    new_cat_3_가구 = models.IntegerField(blank=True, null=True)
    new_cat_3_가전 = models.IntegerField(blank=True, null=True)
    new_cat_3_강아지간식 = models.IntegerField(blank=True, null=True)
    new_cat_3_강아지장난감 = models.IntegerField(blank=True, null=True)
    new_cat_3_건강식품 = models.IntegerField(blank=True, null=True)
    new_cat_3_견과류 = models.IntegerField(blank=True, null=True)
    new_cat_3_계절가전 = models.IntegerField(blank=True, null=True)
    new_cat_3_고양이간식 = models.IntegerField(blank=True, null=True)
    new_cat_3_고양이장남감 = models.IntegerField(blank=True, null=True)
    new_cat_3_골프 = models.IntegerField(blank=True, null=True)
    new_cat_3_과일 = models.IntegerField(blank=True, null=True)
    new_cat_3_그릇_식기 = models.IntegerField(db_column='new_cat_3_그릇/식기', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_기타반려동물용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_노트북 = models.IntegerField(blank=True, null=True)
    new_cat_3_디저트 = models.IntegerField(blank=True, null=True)
    new_cat_3_디지털 = models.IntegerField(blank=True, null=True)
    new_cat_3_디지털_이미용가전 = models.IntegerField(db_column='new_cat_3_디지털/이미용가전', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_리빙 = models.IntegerField(blank=True, null=True)
    new_cat_3_리빙_인테리어 = models.IntegerField(db_column='new_cat_3_리빙/인테리어', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_목욕용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_미용_목욕 = models.IntegerField(db_column='new_cat_3_미용/목욕', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_반려동물리빙 = models.IntegerField(blank=True, null=True)
    new_cat_3_방꾸미기 = models.IntegerField(blank=True, null=True)
    new_cat_3_보관_밀폐용기 = models.IntegerField(db_column='new_cat_3_보관/밀폐용기', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_생활가전 = models.IntegerField(blank=True, null=True)
    new_cat_3_샤워가운 = models.IntegerField(blank=True, null=True)
    new_cat_3_세제 = models.IntegerField(blank=True, null=True)
    new_cat_3_손편지 = models.IntegerField(blank=True, null=True)
    new_cat_3_수건 = models.IntegerField(blank=True, null=True)
    new_cat_3_수유용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_스포츠_휘트니스 = models.IntegerField(db_column='new_cat_3_스포츠/휘트니스', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_스포츠용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_식기_급수기 = models.IntegerField(db_column='new_cat_3_식기/급수기', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_식물_꽃 = models.IntegerField(db_column='new_cat_3_식물/꽃', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_식품 = models.IntegerField(blank=True, null=True)
    new_cat_3_신생아의류 = models.IntegerField(blank=True, null=True)
    new_cat_3_아기_스킨케어 = models.IntegerField(db_column='new_cat_3_아기 스킨케어', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_아기위생_건강용품 = models.IntegerField(db_column='new_cat_3_아기위생/건강용품', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_안마용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_언더웨어_홈웨어 = models.IntegerField(db_column='new_cat_3_언더웨어/홈웨어', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_영양제 = models.IntegerField(blank=True, null=True)
    new_cat_3_와인용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_완구 = models.IntegerField(blank=True, null=True)
    new_cat_3_외출용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_유모차_카시트 = models.IntegerField(db_column='new_cat_3_유모차/카시트', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_육류 = models.IntegerField(blank=True, null=True)
    new_cat_3_이미용가전 = models.IntegerField(blank=True, null=True)
    new_cat_3_이어폰_헤드폰 = models.IntegerField(blank=True, null=True)
    new_cat_3_인테리어용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_임산부용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_자동차용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_주방가전 = models.IntegerField(blank=True, null=True)
    new_cat_3_주방잡화 = models.IntegerField(blank=True, null=True)
    new_cat_3_주얼리 = models.IntegerField(blank=True, null=True)
    new_cat_3_주얼리_패션잡화 = models.IntegerField(db_column='new_cat_3_주얼리/패션잡화', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_주전자_티포트 = models.IntegerField(db_column='new_cat_3_주전자/티포트', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_차_커피 = models.IntegerField(db_column='new_cat_3_차/커피', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_청소도구 = models.IntegerField(blank=True, null=True)
    new_cat_3_출산_기념품 = models.IntegerField(db_column='new_cat_3_출산 기념품', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_치즈 = models.IntegerField(blank=True, null=True)
    new_cat_3_커피_차_와인용품 = models.IntegerField(db_column='new_cat_3_커피/차/와인용품', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_커피용품 = models.IntegerField(blank=True, null=True)
    new_cat_3_태교_취미 = models.IntegerField(db_column='new_cat_3_태교/취미', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_통조림_캔 = models.IntegerField(db_column='new_cat_3_통조림/캔', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_패션의류_잡화 = models.IntegerField(db_column='new_cat_3_패션의류/잡화', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_패션잡화 = models.IntegerField(blank=True, null=True)
    new_cat_3_펫리빙 = models.IntegerField(blank=True, null=True)
    new_cat_3_펫패션 = models.IntegerField(blank=True, null=True)
    new_cat_3_홈데코_패브릭 = models.IntegerField(db_column='new_cat_3_홈데코/패브릭', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_cat_3_홈프래그런스 = models.IntegerField(blank=True, null=True)
    new_cat_3_화장지 = models.IntegerField(blank=True, null=True)
    new_cat_3_화장품 = models.IntegerField(blank=True, null=True)
    new_cat_3_휴지통 = models.IntegerField(blank=True, null=True)
    number_10_m = models.FloatField(db_column='10_m', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_10_f = models.FloatField(db_column='10_f', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2030_m = models.FloatField(db_column='2030_m', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2030_f = models.FloatField(db_column='2030_f', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4050_m = models.FloatField(db_column='4050_m', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4050_f = models.FloatField(db_column='4050_f', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'genderinference'


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.CharField(max_length=20, blank=False, null=False, unique=True)
    product_name = models.CharField(max_length=128, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    num_review = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    product_url = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'product'


class ProductCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id')
    category_1 = models.CharField(max_length=20, blank=True, null=True)
    category_2 = models.CharField(max_length=20, blank=True, null=True)
    category_3 = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductSexGenerationInference(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id')
    sex_generation = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'product_sex_generation_inference'


class Rawdata(models.Model):
    product_id = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=128, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    category_1 = models.CharField(max_length=50, blank=True, null=True)
    category_2 = models.CharField(max_length=50, blank=True, null=True)
    category_3 = models.CharField(max_length=50, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    num_review = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    product_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'rawdata'


class Temp01(models.Model):
    product_id = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=128, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    category_1 = models.CharField(max_length=50, blank=True, null=True)
    category_2 = models.CharField(max_length=50, blank=True, null=True)
    category_3 = models.CharField(max_length=50, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    num_review = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    product_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'temp01'


class Temp02(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=128, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    category_1 = models.CharField(max_length=50, blank=True, null=True)
    category_2 = models.CharField(max_length=50, blank=True, null=True)
    category_3 = models.CharField(max_length=50, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    num_review = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    product_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'temp02'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=20, blank=False, null=False, unique=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    personality = models.IntegerField(blank=True, null=True)
    price_type = models.CharField(max_length=2, blank=True, null=True)
    category_1 = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'user'


class UserProductInteraction(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, to_field='user_id')
    product = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'user_product_interaction'


class UserProductLike(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, to_field='user_id')
    product = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'user_product_like'
        
class FilteredRawdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.CharField(max_length=20, blank=True, null=True)
    product_name = models.CharField(max_length=128, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    category_1 = models.CharField(max_length=20, blank=True, null=True)
    category_2 = models.CharField(max_length=20, blank=True, null=True)
    category_3 = models.CharField(max_length=20, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    num_review = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    product_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'filtered_rawdata'
        
        
class AmazonProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=256, blank=True, null=True)
    image_url = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'amazon_product'

class AmazonUserProductInteraction(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, to_field='user_id', blank=True, null=True)
    product = models.ForeignKey('AmazonProduct', models.DO_NOTHING, to_field='product_id', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'amazon_user_product_interaction'
        
class AmazonUserProductLike(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, to_field='user_id', blank=True, null=True)
    product = models.ForeignKey('AmazonProduct', models.DO_NOTHING, to_field='product_id', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        app_label = 'GiftHubApp'
        db_table = 'amazon_user_product_like'