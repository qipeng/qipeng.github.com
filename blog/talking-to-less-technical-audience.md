<!DOCTYPE html>
<html lang="en" class="yui3-js-enabled" itemscope itemtype="http://schema.org/Thing">
<head>
   <meta charset="utf-8">

  <!-- Always force latest IE rendering engine (even in intranet) & Chrome Frame
       Remove this if you use the .htaccess -->
  <meta http-equiv="X-UA-Compatible" content="">
  <meta http-equiv="Content-Type" content="text/html; charset=utf8" />
  <meta name="robots" content="all" />
  <meta name="googlebot" content="all" />

  <title>Better Homeworks</title>
  <meta name="description" content="Talking to a Less-Technical Audience
">
  <meta name="keywords" content="">
  <meta name="author" content="Peng Qi">

  <!--  Mobile viewport optimized: j.mp/bplateviewport -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.4.2/pure.css">
  <link rel="stylesheet" href="/media/css/syntax.css" type="text/css">
  <link rel="stylesheet" href="/media/js/fancybox/jquery.fancybox.css" type="text/css">
  <link rel="stylesheet" href="/media/css/main-grid.css" type="text/css">
  <!--[if lte IE 8]>

    <link rel="stylesheet" href="http://yui.yahooapis.com/pure//grids-responsive-old-ie.css">

<![endif]-->
<!--[if gt IE 8]><!-->

    <link rel="stylesheet" href="http://yui.yahooapis.com/pure//grids-responsive.css">

<!--<![endif]-->
<!--[if lte IE 8]>
      <link rel="stylesheet" href="/media/css/layouts/marketing-old-ie.css">
  <![endif]-->
  <!--[if gt IE 8]><!-->
      <link rel="stylesheet" href="/media/css/layouts/marketing.css">
  <!--<![endif]-->
  <script type="text/javascript" src="/media/js/main.js"></script>

  
  <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
  <!--[if lt IE 9]>
    <script src="media/js/html5shiv.js"></script>
  <![endif]-->

    <!-- Fav and touch icons -->
  <link rel="shortcut icon" href="/favicon.ico">
  
        <link rel="stylesheet" href="/media/css/site.css" type="text/css">
  <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/default.min.css">
  <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
  <script>hljs.initHighlightingOnLoad();</script>
</head>

<body>

<div class="header">
    <div class="home-menu pure-menu pure-menu-open pure-menu-horizontal pure-menu-fixed">
        <a class="pure-menu-heading" href="/index.html">Peng Qi</a>

                <ul class="nav">
                <li class="nav-item ">
            <a title="Research"
                class="research"
                href="/research">
                Research
            </a>
        </li>        <li class="nav-item pure-menu-selected">
            <a title="Blog"
                class="active blog"
                href="/blog">
                Blog
            </a>
        </li>        <li class="nav-item ">
            <a title="Software"
                class="software"
                href="/software">
                Software
            </a>
        </li>    </ul>
    </div>
</div>

<div id="layout" class="pure-g">

    <div class="content pure-u-1 pure-u-med-3-4">
        <div>
            <!-- A wrapper for all the blog posts -->
            <div class="posts">
                        <section>
            <article class="post">

<div class="title"><h1 itemprop="name">
    Better&nbsp;Homeworks
</h1></div>
<time datetime="2018-03-01">
    Thu, 01 Mar 2018
</time>

<div>

<ul class="tags clear">
<li><span class="lighter" >Tags</span></li>
<li>
    <a class="tag pure-button" href="/blog/tags/TeachingInCS.html">&nbsp;TeachingInCS
    </a>
</li>
</ul>
</div>

<div class="postcontent">
<p>A while ago, I was invited to give an introduction to deep learning to high schoolers participating in a hackathon called <a href="http://linghacks.weebly.com/">LingHacks</a>. Here are some of the things I have learned from preparing for this presentation, as well as watching the presentation of some of the other&nbsp;tutorial&nbsp;speakers.</p>
<h2 id="background">Background</h2>
<p>LingHacks is a new hackathon focused on computational linguistics (a.k.a. natural language processing in most contexts) for high school students, where students spend one day in training (which is where I was at), and two days to flesh out their brilliant ideas about applying language technology to solving&nbsp;real-world&nbsp;problems.</p>
<p>Before I started preparing for <a href="#my-slides">my slides</a>, I asked the organizer about what mathematical background I should be expecting my audience to have. Here is a brief list of things I got from them that would hopefully be useful for others preparing for&nbsp;similar&nbsp;events:</p>
<ul>
<li>Linear algebra<ul>
<li>vectors and their representation in&nbsp;Cartesian&nbsp;coordinates</li>
<li>matrices</li>
<li>vector&nbsp;(inner)&nbsp;product</li>
<li>matrix-vector&nbsp;product</li>
<li>matrix-matrix&nbsp;product</li>
</ul>
</li>
<li>Basic algebra and calculus<ul>
<li>logarithmic and&nbsp;exponential&nbsp;functions</li>
<li>derivatives&nbsp;of&nbsp;functions</li>
</ul>
</li>
<li>(Slightly more) Advanced calculus<ul>
<li><del>multivariate functions and their derivatives</del></li>
</ul>
</li>
<li>Basic probability<ul>
<li>probability mass functions and probability&nbsp;density&nbsp;functions</li>
<li>conditional probability and&nbsp;marginal&nbsp;probability</li>
</ul>
</li>
</ul>
<p>Items crossed out are ones I was notified highschoolers are not supposed to know of by default. I didn&#8217;t end up using most of these anyway &#8212; I&#8217;ll mention why in&nbsp;a&nbsp;bit.</p>
<h2 id="initial-plan">Initial&nbsp;Plan</h2>
<p><strong>Skip if you just want to know what I ended up including in my slides! This section is not a prerequisite in&nbsp;any&nbsp;way.</strong></p>
<p>As you might have inferred from the list of mathematical prerequesites I asked the organizers for, I was going for a pedantic introduction leading up from &#8220;shallow learning&#8221; (linear classifiers) to deep learning (neural networks). I was planning to do this following some of the <a href="https://nlp.stanford.edu/courses/NAACL2013/NAACL2013-Socher-Manning-DeepLearning.pdf">great tutorials out there</a>, and tailoring it to my audience&#8217;s technical level by introducing the following things (in&nbsp;this&nbsp;order):</p>
<ul>
<li>Linear classifiers<ul>
<li>Connecting it to linear algebra and its&nbsp;geometric&nbsp;interpretations</li>
<li>Loss&nbsp;functions&nbsp;(intuitively)</li>
<li>Optimization of parameters (by waving my hands throughout, to avoid mentioning exactly how multivariate functions work or how to&nbsp;take&nbsp;derivatives)</li>
<li>Limitations of linear classifiers (hand-designing features, model&nbsp;capacity,&nbsp;etc.)</li>
</ul>
</li>
<li>Deep learning!<ul>
<li>Stacking&nbsp;linear&nbsp;classifiers!</li>
<li>Well, we also need nonlinearities to make it more powerful (sigmoid, tanh,&nbsp;ReLU,&nbsp;etc.)</li>
<li>So many different kinds of networks (<span class="caps"><span class="caps">CNN</span></span>, <span class="caps"><span class="caps">RNN</span></span>,&nbsp;etc.)</li>
</ul>
</li>
<li>By the way, there are such things called word vectors you&#8217;d need to use as your input to&nbsp;these&nbsp;networks</li>
</ul>
<p>Fortunately, my labmates heard about my plan and stopped me about 20 slides down&nbsp;this&nbsp;path.</p>
<h2 id="wzxhzdk0wzxhzdk1-my-slides-fwiw"><a name="my-slides"></a> My Slides&nbsp;(<span class="caps"><span class="caps">FWIW</span></span>)</h2>
<p>I put my slides on <a href="https://docs.google.com/presentation/d/1ZhAwRlyMkOClLY-6An4h211i0-EgecwGAir671Shh_c/edit?usp=sharing">Google Drive</a>, and hereby make them available under the <a href="https://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License (<span class="caps"><span class="caps">CC</span></span> <span class="caps"><span class="caps">BY</span></span>-<span class="caps"><span class="caps">SA</span></span> 4.0)</a>.</p>
<h2 id="acknowledgements">Acknowledgements</h2></div>

<div style="float:left"><span class="lighter">Newer Post</span>&nbsp;
None
</div>

<div style="float:right"><span class="lighter">Older Post</span>&nbsp;
None
</div>
<br>
<div id="disqus_thread"></div>
<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
    var disqus_shortname = 'pengqishomepage'; // required: replace example with your forum shortname

    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
<a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>
</article>            </section>
                        <div class="footer">
                <div id="sociallinks" class="clear" style="font-size:10px;"></div>
                <div class="pure-menu pure-menu-horizontal pure-menu-open">
                    <ul>
                        <li><a href="http://purecss.io/">Copyright &copy; Peng Qi, 2018</a></li>
                        <li><a href="http://github.com/qipeng/">GitHub</a></li>
                        <li><a href="http://www.linkedin.com/pub/peng-qi/90/800/395/">LinkedIn</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"></script>
<script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>
<script>
window.jQuery || document.write("<script src=\"/media/js/jquery.min.js\"><\/script>")
</script>
<script type="text/javascript" src="/media/js/fancybox/jquery.fancybox.pack.js"></script>
<script type="text/javascript">$(function(){loadsociallinks();loadimg();});</script>

<script src="http://yui.yahooapis.com/3.14.1/build/yui/yui.js"></script>
<script>
YUI().use('node-base', 'node-event-delegate', function (Y) {
    // This just makes sure that the href="#" attached to the <a> elements
    // don't scroll you back up the page.
    Y.one('body').delegate('click', function (e) {
        e.preventDefault();
    }, 'a[href="#"]');
});
</script>


</div>

  <!-- Javascript at the bottom for fast page loading -->

  
  <!--[if lt IE 7 ]>
    <script src="/media/js/libs/dd_belatedpng.js"></script>
    <script>DD_belatedPNG.fix('img, .png_bg'); // Fix any <img> or .png_bg bg-images. Also, please read goo.gl/mZiyb </script>
  <![endif]--><script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-26770326-1', 'qipeng.me');
  ga('require', 'displayfeatures');
  ga('send', 'pageview');
</script>
  
</body>
</html>