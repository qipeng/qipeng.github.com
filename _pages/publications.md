---
layout: page
permalink: /publications/
title: publications
description: (<span style="color:#cc1515;font-weight:bold">*</span>=equal contribution)
years: [2020, 2019, 2018, 2017, 2016, 2014, 2013, 2012]
nav: true
---

<div class="publications">

{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
