{{#each locations}}
<li class="location-result" data-location-index="{{index}}">
  <button class="select-location">
    <h2 class="name">{{title}}</h2>
  </button>
  <div class="address">{{address1}}<br>{{address2}}</div>
</li>
{{/each}}