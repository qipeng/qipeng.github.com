// JavaScript Document

var email_name = {'qipeng':'qipeng.thu'}, email_domain = {'qipeng':'gmail.com'};

function loadimg(){$("a.fancyimg").fancybox({'width': '75%','height': '75%','overlayShow': false,'transitionIn': 'fade','transitionOut': 'fade','titlePosition': 'inside','overlayColor': '#000','overlayOpacity': 0.9});}
function loadgoogletranslate() {$("#googletranslate").empty();$("#googletranslate").append("<img src=\"media/images/loader.gif\" />&nbsp;Loading Google Translate Gadget...");$.ajax({type: "GET",url: "media/googletranslate",dataType:"html",success: function(data){$("#googletranslate").empty();$("#googletranslate").append(data);}});}
function sendEmail(name) {window.location.href="mailto:" + email_name[name] + "@" + email_domain[name];}