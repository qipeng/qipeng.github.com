<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="utf-8">

  <!-- Always force latest IE rendering engine (even in intranet) & Chrome Frame
       Remove this if you use the .htaccess -->
  <meta http-equiv="X-UA-Compatible" content="">
  <meta http-equiv="Content-Type" content="text/html; charset=utf8" />
  <meta name="robots" content="all" />
  <meta name="googlebot" content="all" />

  <title></title>
  <meta name="description" content="">
  <meta name="keywords" content="">
  <meta name="author" content="Peng Qi">

  <!--  Mobile viewport optimized: j.mp/bplateviewport -->
  <meta name="viewport" content="">

	<link href="//netdna.bootstrapcdn.com/bootswatch/2.3.2/cerulean/bootstrap.min.css" rel="stylesheet"> 
    
     
  <link rel="stylesheet" href="/media/css/syntax.css" type="text/css">
  <link rel="stylesheet" href="/media/js/fancybox/jquery.fancybox-1.3.4.css" type="text/css">
  <link rel="stylesheet" href="/media/js/nivo-slider/themes/light/light.css" type="text/css" media="screen" />
  <link rel="stylesheet" href="/media/js/nivo-slider/nivo-slider.css" type="text/css" media="screen" />
  <link href='http://fonts.googleapis.com/css?family=Telex' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" href="/media/css/site.css" type="text/css">
   
  
  <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
  <!--[if lt IE 9]>
    <script src="media/js/html5shiv.js"></script>
  <![endif]-->

    <!-- Fav and touch icons -->
  <link rel="shortcut icon" href="favicon.ico">
      
      </head>

<body>
<div class="container-fluid">
	<div class="row-fluid">
		<div class="span12">
			<div class="navbar">
				<div class="navbar-inner">
					<div class="container-fluid" style="padding:0;border-bottom:1px solid #ccc">
						 <a data-target=".navbar-responsive-collapse" data-toggle="collapse" class="btn btn-navbar"><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></a> <a href="#" class="brand">Peng <span class="surname">Qi</span></a>
						<div class="nav-collapse collapse navbar-responsive-collapse">
                                    <ul class="nav">
                <li >
            <a title="Home Page"
                class="home"
                href="/index.html">
                Home
            </a>
        </li>        <li >
            <a title="Research"
                class="research"
                href="/research">
                Research
            </a>
        </li>        <li >
            <a title="Blog"
                class="blog"
                href="/blog">
                Blog
            </a>
        </li>        <li >
            <a title="Software"
                class="software"
                href="/software">
                Software
            </a>
        </li>        <li >
            <a title="Misc"
                class="misc"
                href="/misc">
                Me &amp; My ...
            </a>
        </li>    </ul>
						</div>
					</div>
				</div>
				
			</div>
            		</div>
	</div>
	<div class="row-fluid">
		<div class="span9">
        <div id="container">
                <section class="content">
          <article class="post">

<ul class="breadcrumb">
    <li>
        <a href="/software/mnlr">Software</a> <span class="divider">/</span>
    </li>
    <li class="active">
        
    </li>
</ul>


<div class="title"><h1 >
    
</h1></div>

<div class="postcontent">
<p>function [model]=mnlr_fit(X, label, reg)
% MNLR_FIT  MultiNomial Logistic Regression Fitting
%   Usage:
%      [model] = MNLR_FIT(X, label, reg)
%   X is an N-by-M matrix of features, where each row is a data sample
%   label is an N-by-1 vector of data labels, where each element takes a
%       value from exactly 1,2,..,K
%   reg is the L2 regularization parameter, default 0
%   model is an (M+1)-by-(K-1) matrix, where the first row corresponds to
%       the bias term of each feature, and the the column corresponding to
%       the last feature is omitted to avoid over-parameterization. This
%       model is compatible with Matlab built-in function mnrfit and mnrval.
%
%   See also <span class="caps">MNRFIT</span>, <span class="caps">MNRVAL</span>.
%   Written by Peng Qi (qipeng.thu@gmail.com).
%   Last_update: Dec 29,&nbsp;2012</p>
<pre><code>[N, M] = size(X);
K = max(label);
model = 0.01 * randn(M + 1, K - 1);

if (nargin &lt; 3),
    reg = 0;
end
options = optimset('GradObj','on','Display','none', 'MaxIter', 1e4, 'MaxFunEvals', 1e5);
model = reshape(minFunc(@(model)target_fun(model, X, label, reg), model(:), options), M+1,K - 1);
</code></pre>
<p>end</p>
<p>function [f, g] = target_fun(model_, X, y, reg)
    [n,p] = size(X);
    k = max(y);
    X = [ones(n,1), X];
    p = p + 1;
    w = reshape(model_,[p k-1]);
    w(:,k) =&nbsp;zeros(p,1);</p>
<pre><code>Z = sum(exp(X*w),2);
f = -sum((sum(X.*w(:,y).',2) - log(Z))) / n + reg / 2 * sum(sum(w(2:end,:).^2));

if nargout &gt; 1
    g = zeros(p,k-1);

    for c = 1:k-1
        g(:,c) = -sum(X.*repmat((y==c) - exp(X*w(:,c))./Z,[1 p]));
    end
    g = g / n;
    g(2:end,:) = g(2:end,:) + reg * w(2:end,1:end-1);
    g = reshape(g,[p*(k-1) 1]);
end
</code></pre>
<p>end</p></div>

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
</article>          </section>
                    </div>
		</div>
		<div class="span3">
        <div class="right-float">
<span class="lighter" >Related Posts</span><br/>
Previous:
None
<br/>

Next:
None
</div>

        <div class="right-float"><div id="sociallinks" style="font-size:10px;"></div>
            <div id="googletranslate"></div>
		</div>
	</div>
	<div class="row-fluid">
		<div class="span12">
        <footer>
      <div id="designlogo"><a href="http://qipeng.github.com/misc/homepage.html" target="_blank"><span class="lighter">Designed</span>by<br>
    <span style="padding-left:40px">Qi<span class="lighter">Peng</span></span></a>
    <br><span style="font-size:10px;text-align:center;">Powered by <a href="http://hyde.github.com/" target="_blank" class="hyde">hyde</a>.</span></div>
      <p style="text-align:center">&copy; <a href="http://qipeng.github.com/">Peng Qi</a>, 2011 &ndash; 2013. Hosted by <a href="http://www.github.com">GitHub</a>.</p>
  </footer>
		</div>
	</div>
</div>
  <!-- Javascript at the bottom for fast page loading -->

  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"></script>
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>
    <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>
  <script src="/media/js/nivo-slider/jquery.nivo.slider.pack.js" type="text/javascript"></script>
  <script> $(window).load(function() {$('#slider').nivoSlider({effect: 'sliceDownRight', slices:15, animSpeed: 300, pauseTime: 5000});});</script>
  <script type="text/javascript" src="/media/js/fancybox/jquery.fancybox-1.3.4.js"></script>
  <script type="text/javascript" src="/media/js/main.js"></script>
  <script type="text/javascript">$(function(){loadimg();loadgoogletranslate();loadsociallinks();});</script>
  
  
  
  <!--[if lt IE 7 ]>
    <script src="/media/js/libs/dd_belatedpng.js"></script>
    <script>DD_belatedPNG.fix('img, .png_bg'); // Fix any <img> or .png_bg bg-images. Also, please read goo.gl/mZiyb </script>
  <![endif]--><script>
    var _gaq = [['_setAccount', 'UA-26770326-1'], ['_trackPageview']];
    (function(d, t) {
    var g = d.createElement(t),
        s = d.getElementsByTagName(t)[0];
    g.async = true;
    g.src = ('https:' == location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    s.parentNode.insertBefore(g, s);
    })(document, 'script');
</script>
  
</body>
</html>