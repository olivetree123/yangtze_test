import json
import random

from jojo import Jojo
from entity.base import UserEntity, SchoolEntity, PhaseEntity, SubjectEntity,  TextBookEditionEntity, TextBookEntity, \
    KnowledgeEntity, ChapterEntity, ExamEntity, ExamKindEntity, QuestionEntity, SourceFileEntity, ResourceEntity, \
    ResourceCategoryEntity
from entity.params import LogInParam, SchoolAddParam, PhaseAddParam, SubjectAddParam, TbEditionAddParam, \
    TextBookAddParam, KnowledgeAddParam, ChapterAddParam, QuestionUploadParam, QuestionListParam, \
    QuestionLabelParam, SourceFilePublishParam, SourceFileUpdateParam, ResourceAddParam, ResourceChapterParam, \
    ResourceKnowledgeParam, ExamKindAddParam, ExamKindUpdateParam, ExamAddParam, ExamListParam, SourceFileDeleteParam, \
    QuestionDeleteBulkParam, ResourceListParam, ResourcePublishParam, DownloadHistoryParam


QUESTION_FILE_PATH = "/Users/gao/Downloads/demo-2.docx"


class ResourceInstance(object):

    def __init__(self, t: Jojo):
        self.t = t

    def test_upload(self):
        subjects = self.t.subject_list()
        subject = subjects[0]
        param = ResourceAddParam(subject.uid, QUESTION_FILE_PATH)
        resource = self.t.resource_add(param)
        if resource:
            print("Success to upload resource")

    def test_category_list(self):
        rs = self.t.resource_category_list()
        for r in rs:
            print(json.dumps(r.json(), indent=4))

    def test_my_list(self):
        param = ResourceListParam(None, 1)
        rs = self.t.resource_list(param)
        print("我的资源数量 = ", len(rs) if rs else 0)
        for r in rs:
            print(json.dumps(r.json(), indent=4))

    def test_list(self):
        category_list = self.t.resource_category_list()
        for category in category_list:
            param = ResourceListParam(category.uid, 0)
            rs = self.t.resource_list(param)
            for r in rs:
                print(json.dumps(r.json(), indent=4))
            print("category = ", category.name, " 资源数量 = ", len(rs) if rs else 0)

    def test_publish(self):
        param = ResourceListParam(None, 1, 0)
        rs = self.t.resource_list(param)
        if not rs:
            print("没有待发布的资源")
            return
        rs = [r.uid for r in rs]
        param = ResourcePublishParam(rs)
        self.t.resource_publish(param)
        print("发布成功")

    def test_download(self):
        param = ResourceListParam(None, 1, 2)
        rs = self.t.resource_list(param)
        if not rs:
            print("没有待发布的资源")
            return
        content = self.t.resource_download("4bf6b35d-58f6-4372-b9ea-80f9f873e40b")
        with open("gaojian.docx", "wb") as f:
            f.write(content)
        print("下载成功")

    def test_download_history(self):
        param = DownloadHistoryParam(1)
        rs = self.t.download_history(param)
        rs = [r.json() for r in rs] if rs else None
        print("rs = ", rs)
        print("获取下载历史成功")

