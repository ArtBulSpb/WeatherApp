<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Погода в России</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script>
        $(function(){
          $('span.more').each(function() {
            $(this).html( '<span class="content">'+ $(this).html() +'</span>&nbsp;<a href="#" class="expand">подробнее</span><a href="#" class="close">свернуть<span>' ).addClass( 'closed' );
          });
          $('.more .close').click(function(){
            $(this).parent().removeClass( 'open').addClass('closed');
            return false;
          });
          $('.more .expand').click(function(){
            $(this).parent().removeClass( 'closed').addClass('open');
            return false;
          }); 
        });
    </script>
</head>

<body>
    <div style="background-color: #c4c4c4;" class="navbar navbar-default navbar-fixed-top">
        <div class="container">          
            <div class="navbar-header">             
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>          
                <a href="/" class="navbar-brand">Погода в России</a>
                <img width="50" src="static\images\logo.png"></img>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/home">Начальная страница</a></li>
                    <li><a href="/about">О нас</a></li>
                    <li><a href="/contact">Контакты</a></li>
                    <li><a href="/view_articles">Полезные статьи</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container body-content">
        {{!base}}
        <hr />
        <footer>
            <p>&copy; {{ year }} - Погода в России</p>
        </footer>
    </div>
    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>
</body>
</html>
