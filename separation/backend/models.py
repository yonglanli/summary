from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
# class User(AbstractUser):
#     """
#     用户信息表
#     """
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u'编号', help_text=u'编号')
#     name = models.CharField(null=True, blank=True, max_length=50, verbose_name=u'姓名', help_text='姓名')
#     name_pinyin = models.CharField(null=True, blank=True, max_length=50, verbose_name=u'姓名拼音', help_text='姓名拼音')
#     username = models.CharField(max_length=50, verbose_name=u'用户名', help_text="用户名", unique=True, null=False,
#                                 blank=False)
#     mobile = models.CharField(verbose_name=u"手机号码", null=True, blank=True, default=None, max_length=20, unique=True,
#                               help_text='手机号码')
#     cardId = models.CharField(db_column='cardid', null=True, blank=True, max_length=40, verbose_name=u"身份证号",
#                               help_text='身份证号')
#     birthDate = models.DateField(db_column='birthdate', null=True, blank=True, verbose_name=u'出生日期', help_text="出生日期")
#     gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), null=True, blank=True,
#                               verbose_name="性别", help_text=u"性别")
#     email = models.EmailField(null=True, blank=True, verbose_name=u'邮箱', help_text="邮箱", unique=True)
#     # userPk = models.CharField(db_column='userpk', null=True, blank=True, max_length=100, verbose_name=u'原系统的id',
#     #                           help_text="原系统返回的id")
#     qq = models.CharField(max_length=20, null=True, blank=True, help_text=u'qq号', verbose_name=u'qq号')
#     weChat = models.CharField(db_column='wechat', max_length=50, null=True, blank=True, help_text=u'微信号',
#                               verbose_name=u'微信号')
#     address = models.CharField(max_length=100, null=True, blank=True, help_text=u'地址', verbose_name=u'地址')
#     # organization = models.ForeignKey('expedition.Organization', related_name='User_organization', null=True, blank=True,
#     #                                  on_delete=models.SET_NULL,help_text=u'单位', verbose_name=u'单位')
#     # passport = models.CharField(db_column='passport', null=True, blank=True, max_length=30, verbose_name=u"护照证号",
#     #                             help_text='护照证号')
#     modifyTime = models.DateTimeField(db_column='modifytime', null=True, blank=True, verbose_name=u'最后一次修改时间',
#                                       help_text="最后一次修改时间")
#
#     class Meta:
#         db_table = 'sys_user'
#         verbose_name = "用户信息表"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
# 关键词
class KeyWordType(models.Model):
    """
        关键词类型表
        2018-10-11 add haida
    """
    id = models.UUIDField(primary_key=True,verbose_name='UUID',help_text='UUID',default=uuid.uuid4,editable=False)
    typename = models.CharField(max_length=50,verbose_name=u'类型名称',help_text=u'类型名称',null=False,blank=False)
    isDelete = models.BooleanField(db_column='isdelete', verbose_name=u'是否已删除（是，否）',
                                   help_text=u'是否已删除（是，否）', default=False)
    modifytime = models.DateTimeField(null=True, blank=True, help_text=u'修改时间', verbose_name=u'修改时间')
    createtime = models.DateTimeField(null=True, blank=True, help_text=u'创建时间', verbose_name=u'创建时间')
    createuser = models.ForeignKey(User, db_column="createuser", verbose_name=u"创建人", help_text='创建人',
                                   on_delete=models.SET_NULL, related_name="Md_keywordtype_createuserid", null=True,
                                   blank=True)
    modifyuser = models.ForeignKey(User, db_column="modifyuser", verbose_name=u"修改人", help_text='修改人',
                                   on_delete=models.SET_NULL, related_name="Md_keywordtype_modifyuserid", null=True,
                                   blank=True)

    class Meta:
        verbose_name = u'关键词类型表'
        verbose_name_plural = verbose_name
        db_table = 'md_keyword_type'

    def __str__(self):
        return self.typename


class KeyWord(models.Model):
    """
        关键词表
    """
    id = models.UUIDField(primary_key=True, verbose_name='UUID',help_text='UUID',default=uuid.uuid4,editable=False)
    name_cn = models.CharField(max_length=1000, verbose_name=u'中文名称', help_text=u'中文名称', null=False, blank=False)
    name_en = models.CharField(max_length=1000, verbose_name=u'英文名称', help_text=u'英文名称', null=False, blank=False)
    kw_type = models.ForeignKey(KeyWordType, db_column="kw_type", verbose_name=u"关键字类型", help_text='关键字类型',
                                   on_delete=models.SET_NULL, related_name="Md_keyword_kw_type", null=True,
                                   blank=True)
    source = models.CharField(max_length=1000,verbose_name=u'还不知道是啥',help_text=u'还不知道是啥')
    isDelete = models.BooleanField(db_column='isdelete', verbose_name=u'是否已删除（是，否）',
                                   help_text=u'是否已删除（是，否）', default=False)
    class Meta:
        verbose_name = u'关键词表'
        verbose_name_plural = verbose_name
        db_table = 'md_keyword'

    def __str__(self):
        if self.name_cn:
            return self.name_cn
        else:
            return self.name_en
