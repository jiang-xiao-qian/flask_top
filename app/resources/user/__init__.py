from flask import Blueprint
from flask_restful import Api
from .passport import SMSCodesResource, LoginRegisterResource
from .profile import CurrentUserResource, UserPhotoResource
from .channel import UserChannelResource
from utils.output import output_json
from utils.constants import USER_URL_PREFIX

# 1.创建蓝图对象[管理User模块]
user_bp = Blueprint("user_bp", __name__, url_prefix=USER_URL_PREFIX)

# 2.将蓝图对象包装成API对象
user_api = Api(user_bp)

# 3.添加路由信息
# mob 自定义转换器进行手机号码格式验证
user_api.add_resource(SMSCodesResource, '/sms/codes/<mob:mobile>')
user_api.add_resource(LoginRegisterResource, '/authorizations')
# /app/user
user_api.add_resource(CurrentUserResource, '/user')
# /app/user/photo
user_api.add_resource(UserPhotoResource, '/user/photo')
# /app/user/channels
user_api.add_resource(UserChannelResource, '/user/channels')

# 4.在app中注册蓝图对象

# 5.自定义返回的json格式
# 主动寻求装饰
user_api.representation(mediatype="application/json")(output_json)
