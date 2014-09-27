# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from django.template import Template,Context,RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import json

#doc
#Cross Site Request Forgery protection https://docs.djangoproject.com/en/dev/ref/contrib/csrf/

def test(request):
  fp = open('djtest_download/test.html')  
  t = Template(fp.read())  
  fp.close()  
  html = t.render(Context({"id":1}))  
  return HttpResponse(html) 
  
from django.core.servers.basehttp import FileWrapper  
def download_conf_zipfile(request): 
  print '---------- download -------------'
  import tempfile, zipfile 
  from django.http import HttpResponse 
   
 
  temp = tempfile.TemporaryFile() 
  archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED) 
  src = "C:\test\test\test\conf\test2" 
  files = os.listdir(src) 
  print 'files ',files
 
  for filename in files: 
    print filename
    archive.write(src+'/'+filename, filename) 
  archive.close() 
  wrapper = FileWrapper(temp) 
  response = HttpResponse(wrapper, content_type='application/zip') 
  response['Content-Disposition'] = 'attachment; filename=test.zip' 
  response['Content-Length'] = temp.tell() 
  temp.seek(0) 
  return response 
 
def send_file(request, type, ff):
  print 'args: ',type,ff   
  filename = r"C:\test\djtest_download\static\pujing.jpg" # Select your file here.    
  fname = filename.rsplit("\\",1)[1]  
  print fname
  temp = open(filename, 'rb')
  wrapper = FileWrapper(temp)   
  response = StreamingHttpResponse(wrapper, content_type='text/plain')   
  response['Content-Disposition'] = 'attachment; filename=%s'%fname 
  response['Content-Length'] = os.path.getsize(filename)
  print os.path.getsize(filename)
  temp.seek(0) 
  return response   


import os
import settings
import mimetypes 
def file_download(request, filename):  
    filepath = os.path.join(settings.MEDIA_ROOT, filename)     
    print (filepath)   
    wrapper = FileWrapper(open(filepath, 'rb'))  
    content_type = mimetypes.guess_type(filepath)[0]  
    response = HttpResponse(wrapper, mimetype='content_type')  
    response['Content-Disposition'] = "attachment; filename=%s" % filename  
    return response    


  


