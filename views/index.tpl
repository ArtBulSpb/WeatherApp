% rebase('layout.tpl', title='Home Page', year=year)

<div id="search-bar" data-text="dwefwe">
    <input type="text" tabindex="0" name="name" id="search"  placeholder="Поиск города" bem-id="224" autocomplete="off">
</div>

<div class="main">
    <p class="lead">Получите сводку погоды по крупнейшим городам России</p>
    <p id="truncateLongTexts">Климат России весьма разнообразен из-за огромной территории страны, хотя на большей части территории он континентальный <span class="more">или умеренно континентальный с длинной холодной зимой и коротким нежарким летом. Высокие горные массы на юге России и в Средней Азии препятствуют проникновению на территорию России теплых воздушных масс.В зимние месяцы, например. Северный Ледовитый океан полностью покрыт льдом и является скорее огромной ледяной массой, способствующей холодной зиме северных регионов России. Немного на климат западной части страны влияет Атлантический океан, однако влияние это слабое и выражается прежде всего в повышенной влажности на Балтийском побережье. Среднегодовой уровень осадков на Европейской территории России составляет около 800 мм, однако в южных регионах уменьшается до 400 мм. В Сибири среднегодовая норма осадков составляет от 500 до 800 мм, в горных районах достигая 1000 мм. Что касается температур, то самым холодным регионом считается Сибирь, где в районе города Верхоянск находится “полюс холода” - средняя температура января здесь около -51°C, а в феврале столбик термометра опускается иногда до -68°C. На Арктическом побережье температуры не такие низкие, однако из-за влияния Ледовитого океана иногда опускаются до -50°C. Однако те же факторы, что вызывают низкие зимние температуры, способствуют теплому, а иногда жаркому лету в этих регионах: средняя температура июля в Верхоянске составляет около 13°C, а иногда летние температуры достигают 37°C. В Европейской части климат более умеренный, а на черноморском побережье - мягкий. Средняя январская температура в Москве составляет от -16°C до -9°C, средняя июльская температура - от 13°C до 23°C.
	</span></p>
    <ul class="nav navbar-nav">
        %for city in cities:
            <li><a href="/city_weather?city={{cities.index(city)}}">{{city}}</a></li>
        %end
    </ul>
</div>
