import json
import random

from jojo import Jojo
from entity.base import UserEntity, SchoolEntity, PhaseEntity, SubjectEntity,  TextBookEditionEntity, TextBookEntity, \
    KnowledgeEntity, ChapterEntity, ExamEntity, ExamKindEntity, QuestionEntity, SourceFileEntity, ResourceEntity
from entity.params import LogInParam, SchoolAddParam, PhaseAddParam, SubjectAddParam, TbEditionAddParam, \
    TextBookAddParam, KnowledgeAddParam, ChapterAddParam, QuestionUploadParam, QuestionListParam, \
    QuestionLabelParam, SourceFilePublishParam, SourceFileUpdateParam, ResourceAddParam, ResourceChapterParam, \
    ResourceKnowledgeParam, ExamKindAddParam, ExamKindUpdateParam, ExamAddParam, ExamListParam, SourceFileDeleteParam, \
    QuestionDeleteBulkParam, FocusParam, FocusListParam, ResourceListParam


class FocusInstance(object):

    def __init__(self, t: Jojo):
        self.t = t

    def test_focus_question(self):
        param = QuestionListParam()
        rs = self.t.question_list(param)
        if not rs:
            raise Exception("习题列表为空，无法收藏")
        question = rs[0]
        param = FocusParam(kind=1, question_id=question.uid)
        f = self.t.focus(param)
        print(f.json())
        print("Success to focus question")

    def test_focus_exam(self):
        pass

    def test_focus_resource(self):
        param = ResourceListParam(None, 1, 2)
        rs = self.t.resource_list(param)
        if not rs:
            raise Exception("资源列表为空，无法收藏")
        resource = rs[0]
        param = FocusParam(kind=3, resource_id=resource.uid)
        f = self.t.focus(param)
        print(f.json())
        print("Success to focus resource")

    def test_focus_list(self):
        param = FocusListParam(kind=3)
        rs = self.t.focus_list(param)
        rs = [r.json() for r in rs] if rs else []
        print(json.dumps(rs, indent=4))
        print("Success to get focus list")