// JavaScript Document

var email_name = {'qipeng':'qipeng.thu'}, email_domain = {'qipeng':'gmail.com'};

function loadimg(){$("a.fancyimg").fancybox({'width': '75%','height': '75%','overlayShow': false,'transitionIn': 'fade','transitionOut': 'fade','titlePosition': 'inside','overlayColor': '#000','overlayOpacity': 0.9});
$("a.fancyimg img").after('<div style="display:block;width:16px;height:16px;position:absolute;top:0px;right:0px;background:url(\'/media/images/fancycorner.png\') no-repeat;_background:none;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true, sizingMethod=noscale, src=\'/media/images/fancycorner.png\');"> </div>');
$("a.fancyimg").wrap("<div style='width:auto;overflow:hidden;' />");}
function loadgoogletranslate() {$("#googletranslate").html("<img src=\"/media/images/loader.gif\" />&nbsp;Loading Google Translate Gadget...");$.ajax({type: "GET",url: "/media/googletranslate",dataType:"html",success: function(data){$("#googletranslate").html(data);}});}
function loadsociallinks() {$("#sociallinks").html("<img src=\"/media/images/loader.gif\" />&nbsp;Loading SNS Buttons...");$.ajax({type: "GET",url: "/media/sociallinks",dataType:"html",success: function(data){$("#sociallinks").html(data);}});}
function sendEmail(name) {window.location.href="mailto:" + email_name[name] + "@" + email_domain[name];}