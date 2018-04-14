from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

def post_comment(request, post_pk):
    #通过文章的primarykey索引到文章对象
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        #django会根据form的字段设置去校验字段的合法性
        if form.is_valid():
            #保存数据但是不提交到数据库
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            #redirect对象的时候，会自动调用对象的get_absolute_url方法获取url然后在重定向
            return redirect(post)
        else:
            #由于comment和post是外键关系，可以通过post.comment_set获取一个post下的所有comment
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'blog/detail.html', context=context)
    else:
        return redirect(post)

# Create your views here.
#redirect 既可以接收一个 URL 作为参数，也可以接收一个模型的实例作为参数（例如这里的 post）。如果接收一个模型的实例，那么这个实例必须实现了 get_absolute_url 方法，这样 redirect 会根据 get_absolute_url 方法返回的 URL 值进行重定向
#另外我们使用了 post.comment_set.all() 来获取 post 对应的全部评论。 Comment 和Post 是通过 ForeignKey 关联的，回顾一下我们当初获取某个分类 cate 下的全部文章时的代码：Post.objects.filter(category=cate)。
#这里 post.comment_set.all() 也等价于 Comment.objects.filter(post=post). 其中 xxx_set 中的 xxx 为关联模型的类名（小写）。例如 Post.objects.filter(category=cate) 也可以等价写为 cate.post_set.all()。

