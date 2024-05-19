% rebase('layout.tpl', title='Полезные статьи', year=date_today.year)

<div class="main">

    <div>
        %for article in articles:
            <div class="aritcle_container">
                <div class="aritcle_header">
                    <p><h3>{{article.author}}</h3></p>
                    <p><a>{{article.date}}</a></p>
                </div>
                
                <p><h3>{{article.title}}</a></h3>
            </div>
        %end
    </div>        

</div>
    <p><a>{{error}}</a></p>
    <form method="post">
        <p>
            <p><input type="text" size="50" name="AUTHOR" placeholder="Автор статьи"></p>
            <p><input type="text" size="50" name="TITLE" placeholder="Название статьи"></p>
            <p><input type="date" name="DATE" required="true" value="{{date_today}}" min="2000-01-01" max="{{date_today}}" /></p>
            <p><input class="btn btn-default" type="submit" value="Send"></p>
        </p>
    </form>