<script type="text/javascript">
	function up_file(){
		var form_data = new FormData()
		form_data.append('file_obj',$('#file')[0].files[0])
		form_data.append('csrfmiddlewaretoken', '{{ csrf_token }}') 
		$.ajax({
			url:'{% url "myadmin_file_uploads" %}',
			type:'post',
			contentType:false,
			processData:false,
			data:form_data,
			success:function(data){
				$('#show_pic').attr('src',data.src)
				$('#pic_url').val(data.src)
			}
		})

	}
</script>

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from web.settings import BASE_DIR

def file_uploads(request):
	# 获取上传的文件
	myfile = request.FILES.get('file_obj')

	try:
		import time
		# 生成进的文件名
		filename = str(time.time())+"."+myfile.name.split('.').pop()
		# 打开存图片的文件夹
		destination = open(BASE_DIR+"/static/uploads/"+filename,'wb+')
		# 分流写入图片
		for chunk in myfile.chunks():
			destination.write(chunk)
		# 关闭资源
		destination.close()
		# 存入文件夹的图片的名字
		file_name = '/static/uploads/'+filename
		# 返回文件名
		return JsonResponse({'src':file_name})
	except:
		return False