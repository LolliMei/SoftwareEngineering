from django.shortcuts import render
from  .models import Question
# 导入 HttpResponse 模块
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
# 视图函数
from user.models import user_profile_stu, imageprofile
from .models import CourseList, Question, Exersice, Item
import simplejson
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.contrib.auth.hashers import check_password,make_password
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User


#上传试题
@csrf_exempt
def submitproblem(request):
    ##用户验证机制
    response={}
    if(request.method=="POST"):
        req=simplejson.loads(request.body)
        sessionid=req["sessionid"]
        dic = cache.get(sessionid)
        if dic is None:
            return JsonResponse({"msg":"expire"})
        username=dic["username"]
        user=User.objects.get(username=username)
        to_which_course = CourseList.objects.get(id=req["course_id"])
        # 先数据库查询course_id, 没有则新建
        content=req["content"]
        answer=req["answer"]
        choice_a = req["choice_a"]
        choice_b = req["choice_b"]
        choice_c = req["choice_c"]
        choice_d = req["choice_d"]
        note = req["note"]
        
        try:
            print(user)
            question = Question(submit_user = user,course=to_which_course,content=content,answer=answer,choice_a=choice_a, choice_b = choice_b, choice_c = choice_c, choice_d = choice_d, note = note)
            question.save()
            response["msg"]="true"
            response["question_id"]=question.id
            response["question_time"]=question.add_time
        except Exception as e:
            response["msg"]=e
            print(e)
            return JsonResponse(response)
        return JsonResponse(response)