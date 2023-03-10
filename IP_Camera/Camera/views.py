from django.http import StreamingHttpResponse
from django.shortcuts import render
from  django.views import generic as view_dj
from Camera.helper import VideoCamera, gen
from django.views.decorators import gzip


class IndexView(view_dj.TemplateView):
    template_name = 'stream.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['start'] = True
        return context




@gzip.gzip_page
def openCam(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'stream.html')
