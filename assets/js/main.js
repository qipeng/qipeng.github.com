// JavaScript Document

var email_name = {'pengqi':'pengqi'}, email_domain = {'pengqi':'cs.stanford.edu'};

function loadimg(){$("a.fancyimg").fancybox({'width': '75%','height': '75%','overlayShow': false,'transitionIn': 'fade','transitionOut': 'fade','titlePosition': 'inside','overlayColor': '#000','overlayOpacity': 0.9});
$("a.fancyimg img").after('<div style="display:block;width:16px;height:16px;position:absolute;top:0px;right:0px;background:url(\'/assets/img/fancycorner.png\') no-repeat;_background:none;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true, sizingMethod=noscale, src=\'/media/images/fancycorner.png\');"> </div>');
$("a.fancyimg").wrap("<div style='width:auto;overflow:hidden;' />");}
function sendEmail(name) {window.location.href="mailto:" + email_name[name] + "@" + email_domain[name];}
