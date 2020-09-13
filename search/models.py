from django.db import models


class Pref(models.Model):
    """都道府県"""
    PREF = [
            ("hokkaido","北海道"),("aomori","青森県"),
            ("iwate","岩手県"),("miyagi","宮城県"),("akita","秋田県"),
            ("yamagata","山形県"),("fukushima","福島県"),("ibaraki","茨城県"),
            ("tochigi","栃木県"),("gunma","群馬県"),("saitama","埼玉県"),
            ("chiba","千葉県"),("tokyo","東京都"),("kanagawa","神奈川県"),
            ("niigata","新潟県"),("toyama","富山県"),("ishikawa","石川県"),
            ("fukui","福井県"),("yamanashi","山梨県"),("nagano","長野県"),
            ("gifu","岐阜県"),("shizuoka","静岡県"),("aichi","愛知県"),
            ("mie","三重県"),("shiga","滋賀県"),("kyoto","京都府"),
            ("osaka","大阪府"),("hyogo","兵庫県"),("nara","奈良県"),
            ("wakayama","和歌山県"),("tottori","鳥取県"),("shimane","島根県"),
            ("okayama","岡山県"),("hiroshima","広島県"),("yamaguchi","山口県"),
            ("tokushima","徳島県"),("kagawa","香川県"),("ehime","愛媛県"),
            ("kochi","高知県"),("fukuoka","福岡県"),("saga","佐賀県"),
            ("nagasaki","長崎県"),("kumamoto","熊本県"),("oita","大分県"),
            ("miyazaki","宮崎県"),("kagoshima","鹿児島県"),("okinawa","沖縄県"),
    ]

    pref = models.CharField(max_length=9,choices=PREF)

    class Meta:
        verbose_name_plural = 'Pref'


class Menu(models.Model):
    """メニュー　id(自動採番),menu"""
    
    menu = models.TextField(verbose_name='メニュー')

    class Meta:
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.menu



class Store(models.Model):
    """店舗情報　id(自動採番),都道府県,都道府県（市区町村以下）,menu """
    
    PREF = [
            ("hokkaido","北海道"),("aomori","青森県"),
            ("iwate","岩手県"),("miyagi","宮城県"),("akita","秋田県"),
            ("yamagata","山形県"),("fukushima","福島県"),("ibaraki","茨城県"),
            ("tochigi","栃木県"),("gunma","群馬県"),("saitama","埼玉県"),
            ("chiba","千葉県"),("tokyo","東京都"),("kanagawa","神奈川県"),
            ("niigata","新潟県"),("toyama","富山県"),("ishikawa","石川県"),
            ("fukui","福井県"),("yamanashi","山梨県"),("nagano","長野県"),
            ("gifu","岐阜県"),("shizuoka","静岡県"),("aichi","愛知県"),
            ("mie","三重県"),("shiga","滋賀県"),("kyoto","京都府"),
            ("osaka","大阪府"),("hyogo","兵庫県"),("nara","奈良県"),
            ("wakayama","和歌山県"),("tottori","鳥取県"),("shimane","島根県"),
            ("okayama","岡山県"),("hiroshima","広島県"),("yamaguchi","山口県"),
            ("tokushima","徳島県"),("kagawa","香川県"),("ehime","愛媛県"),
            ("kochi","高知県"),("fukuoka","福岡県"),("saga","佐賀県"),
            ("nagasaki","長崎県"),("kumamoto","熊本県"),("oita","大分県"),
            ("miyazaki","宮崎県"),("kagoshima","鹿児島県"),("okinawa","沖縄県"),
    ]


    name = models.CharField(max_length=100,verbose_name="店舗名")
    pref = models.CharField(max_length=9,choices=PREF)
    address = models.TextField(verbose_name="住所")
    menu = models.TextField(verbose_name="メニュー")
    store_map = models.TextField(verbose_name="地図",null=True)

    class Meta: 
        verbose_name_plural = 'Store'


    def __str__(self):
       return str(self.name)



class Comment(models.Model):
    """投稿機能 画像１つ、ひとこと、投稿日時、いいね"""
    image = models.ImageField(
        verbose_name='image',
        upload_to='media/',
        blank=False,
        null=False
    )
    text = models.TextField(
        max_length=250,
        verbose_name='comment',
        blank=False,
        null=False
    )
    posted_at = models.DateTimeField(auto_now_add=True)
    iine = models.IntegerField(default=0)

    def __str__(self):
        return self.text