---
layout: page
permalink: /publications/
title: publications
description: (<span style="color:#cc1515;font-weight:bold">*</span>=equal contribution)
nav: true
---

<div class="publications">

{% capture current_year %}{{  "now" | date: '%Y' }}{% endcapture %}
{% for y in (2012..current_year) reversed %}
  <!-- <h2 class="year">{{y}}</h2> -->
  {% capture bib %}{% bibliography -f papers -q @*[year={{y}}]* %}{% endcapture %}
  {% if bib contains "<li>" %}
  <h2 class="year">{{y}}</h2>
  {{ bib }}
  {% endif %}
{% endfor %}

</div>
