import os
import uuid
from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.http import require_POST

from file_upload.models import Screenshot


def list_screenshots(request):
    screenshots = Screenshot.objects.all()
    return render_to_response('landing_page.html',{'screenshots':screenshots},context_instance=RequestContext(request))


@require_POST
def upload_screenshot(request):
    unique_filename = 'screenshot_' + str(uuid.uuid4()) + '.png'
    file_upload_path = os.path.join('screenshots', unique_filename)

    try:
        content = request.POST.get('data').replace('data:image/png;base64,', '')
        fh = open(os.path.join(settings.MEDIA_ROOT,file_upload_path), "wb")
        fh.write(content.decode('base64'))
        fh.close()

        file = Screenshot.objects.create(attachment = file_upload_path)

        return JsonResponse({
            'status': 'success',
            # 'delete_url': reverse('delete_file', kwargs={'pk':file.id}),
            'fileName': unique_filename,
            'url': file.attachment.url
    })
    except Exception,e:
        print e
        return JsonResponse({'status': 'error'})