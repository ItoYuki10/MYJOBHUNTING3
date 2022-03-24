from django.shortcuts import render
# django.views.genericからListView、DetailViewをインポート
from django.views.generic import ListView, DetailView, TemplateView
# django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからPhotoPostFormをインポート
from .forms import BlogPostForm

from .models import BlogPost

class IndexView(ListView):
    '''トップページのビュー
    
    投稿記事を一覧表示するのでListViewを継承する
    
    Attributes:
      template_name: レンダリングするテンプレート
      context_object_name: object_listキーの別名を設定
      queryset: データベースのクエリ
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # context_object_nameーの別名を設定
    context_object_name = 'orderby_records'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並べ替える
    queryset = BlogPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 4


class CreateBlogView(CreateView):
    
    # BlogPostFormをフォームクラスとして登録
    form_class = BlogPostForm
    # レンダリングするテンプレート
    template_name = "post_blog.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('job:post_done')

    def form_valid(self, form):
        
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
    '''
    # post_success.htmlをレンダリングする
    template_name ='post_success.html'


class BlogDetail(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するのでDetailViewを継承する
     Attributes:
      template_name: レンダリングするテンプレート
    '''
    # post.htmlをレンダリングする
    template_name ='post.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost


class YourselfView(ListView):
    '''自己分析(Yourself)カテゴリの記事を一覧表示するビュー
    
    '''
    # Yourself_list.htmlをレンダリングする
    template_name ='Yourself_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # context_object_nameの別名を設定
    context_object_name = 'Yourself_records'
    # category='Yourself'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='Yourself').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 3

class InterviewView(ListView):
    '''面接(Interview)カテゴリの記事を一覧表示するビュー
    
    '''
    # Interview_list.htmlをレンダリングする
    template_name ='Interview_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # context_object_nameの別名を設定
    context_object_name = 'Interview_records'
    # category='Interview'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='Interview').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 3

class CompanyinfoView(ListView):
    '''企業情報(Companyinfo)カテゴリの記事を一覧表示するビュー
    
    '''
    # Companyinfo_list.htmlをレンダリングする
    template_name ='Companyinfo_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # context_object_nameの別名を設定
    context_object_name = 'Companyinfo_records'
    # category='Companyinfo'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='Companyinfo').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 3
# Create your views here.
