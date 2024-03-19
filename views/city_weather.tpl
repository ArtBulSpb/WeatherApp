% rebase('layout.tpl', title=title, year=year)

<div class="main">
    <h2>{{ title }}</h2>
    <div style="display: flex;">
        <div>
            <p>Ср 20</p>
            <p style="font-size: 20px;">Сегодня</p>
        </div>
        <img title="{{weather_show}}" width="100px" src="{{weather.weather.value}}"></img> 
    </div>  
    <div style="display: flex;height: 43px">          
        <div title="Погода ночью" style="margin-top: 5px;width: 30px;background-color: #2e6cc3">
            <span>{{weather.night_temperature}}</span>
        </div>
        <div title="Погода днем" style="width: 30px;background-color: #bfdc49">
            <span>{{weather.day_temperature}}</span>
        </div>
    </div>
</div>