from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'job'

# URLパターンを登録するための変数
urlpatterns = [
    # リクエストされたURLが''(無し)の場合
    # viewsモジュールのIndexVieを実行
    path('', views.IndexView.as_view(), name='index'),


    # 投稿ページへのアクセスはviewsモジュールのCreateBlogViewを実行
    path('post/', views.CreateBlogView.as_view(), name='post'),
    # 投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),




path(
        # 詳細ページのURLは「blog-detail/レコードのid/」
        'blog-detail/<int:pk>/',
        # viewsモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        # URLパターンの名前を'blog_detail'にする
        name='blog_detail'
        ),



# 自己分析カテゴリの一覧ページのURLパターン
    path(
        # エントリーシートカテゴリの一覧ページのURLは「Yourself-list/」
        'Yourself-list/',
        # viewsモジュールのYourselfViewを実行
        views.YourselfView.as_view(),
        # URLパターンの名前を'Yourself_list'にする
        name='Yourself_list'
        ),

    # Interviewカテゴリの一覧ページのURLパターン
    path(
        # Interviewカテゴリの一覧ページのURLは「Interview-list/」
        'Interview-list/',
        # viewsモジュールのInterviewViewを実行
        views.InterviewView.as_view(),
        # URLパターンの名前を'Interview_list'にする
        name='Interview_list'
        ),

    # Companyinfoカテゴリの一覧ページのURLパターン
    path(
        # Companyinfoカテゴリの一覧ページのURLは「Companyinfo-list/」
        'Companyinfo-list/',
        # viewsモジュールのCompanyinfoViewを実行
        views.CompanyinfoView.as_view(),
        # URLパターンの名前を'Companyinfo_list'にする
        name='Companyinfo_list'
        ),
]