% rebase('layout.tpl', title='Полезные статьи', year=date_today.year)

<form method="post" class="article-form">
    <p class="error-message"><a>{{error}}</a></p>
    <div class="form-group">
        <input type="text" size="50" name="AUTHOR" placeholder="Автор статьи">
    </div>
    <div class="form-group">
        <input type="text" size="50" name="TITLE" placeholder="Название статьи">
    </div>
    <div class="form-group">
        <textarea name="DESCRIPTION" placeholder="Описание" cols="40" rows="5"></textarea>
    </div>
    <div class="form-group">
        <input type="date" name="DATE" required value="{{date_today}}" min="2000-01-01" max="{{date_today}}">
    </div>
    <div class="form-group">
        <input class="btn btn-default" type="submit" value="Send">
    </div>
</form>
<div class="main">
    <div class="articles-container">
        %for article in articles:
            <div class="article-container">
                <div class="article-header">
                    <h4>{{article.author}}</h4>
                    <p class="article-date">{{article.date}}</p>
                </div>
                <h1 class="article-title">{{article.title}}</h1>
                <p>{{article.description}}</p>
            </div>
        %end
    </div>        
</div>
