from django.views import generic

from .forms import MenuChoiceForm, CreateCommentForm

from .models import Store, Comment

from django.views.generic import ListView

from django.http import HttpResponse, QueryDict

from django.urls import reverse_lazy

from datetime import datetime




class IndexView(generic.TemplateView,generic.FormView,generic.ListView):
    template_name = "index.html"
    form_class = MenuChoiceForm
    
    model = Store
    object_list = Store.objects.all()

         
#メニュー+都道府県検索
def exec_ajax(request):
    
    menu = request.GET.get("menu")  # GETパラメータ1
    pref = request.GET.get("pref")  # GETパラメータ2

    print(request,menu,pref)

    #メニュー＋都道府県　or メニューのみ
    if pref != 'todofuken':
        object_list = Store.objects.filter(menu__contains=menu,pref=pref)

    else:
        object_list = Store.objects.filter(menu__contains=menu)
        
    #検索結果件数
    count = object_list.count()


    html_tags = '<p class="result">検索結果：' + str(count) + ' 件</p><table>' 
    
    #検索結果一覧出力
    for i in object_list:

        #店舗名
        html_tags += '<tr><td><b>' + i.name + '</b></td></tr>' 
        
        #店舗住所
        html_tags += '<tr><td>' + i.address + ' '

        #地図
        html_tags += '<a href="' + str(i.store_map) + '" target="map_result">'
        html_tags += '<img src="/static/img/map.jpg" width="12px" height="12px" title="map"></a></td></tr>'

        #hr
        html_tags += '<tr><td><hr width="100%" class="hr"></td></tr>'

    html_tags += '</table>' 

    
    print(html_tags)
    return HttpResponse(html_tags)

#投稿フォーム
class CommentCreateView(generic.CreateView):
    template_name="comment.html"
    model = Comment
    form_class = CreateCommentForm
    
    success_url = '/'


def comment_list(request):
    
    object_list = Comment.objects.order_by('posted_at').reverse()
        
    comment_tags = ''

#投稿出力
    for i in object_list:   
        comment_tags += '<p class="cmmnt_list">'
        comment_tags += '<img src="/media/' + str(i.image) + '" width="120" height="120"><br>'
        comment_tags += i.text + '<br>'

        d = i.posted_at.strftime("%Y-%m-%d %a %H:%M:%S")
        
        comment_tags += d + '</p>'

    return HttpResponse(comment_tags)

def post_comment(request):
    """投稿を行う関数"""

    if request.method == 'POST':
        #文字列取得
        text = request.POST.get("text")

        if text is None:
            text = ''
            
        #画像取得
        image = request.FILES.get('image_file')
        
        #modelにデータ格納
        Comment(
            image = image,
            text = text,
        ).save()



        #レンダリング不要のため空文字列を返す
        return HttpResponse("", content_type='application/json')
