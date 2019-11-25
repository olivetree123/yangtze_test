import json
import random

from jojo import Jojo
from entity.base import UserEntity, SchoolEntity, PhaseEntity, SubjectEntity,  TextBookEditionEntity, TextBookEntity, \
    KnowledgeEntity, ChapterEntity, ExamEntity, ExamKindEntity, QuestionEntity, SourceFileEntity, ResourceEntity
from entity.params import LogInParam, SchoolAddParam, PhaseAddParam, SubjectAddParam, TbEditionAddParam, \
    TextBookAddParam, KnowledgeAddParam, ChapterAddParam, QuestionUploadParam, QuestionListParam, \
    QuestionLabelParam, SourceFilePublishParam, SourceFileUpdateParam, ResourceAddParam, ResourceChapterParam, \
    ResourceKnowledgeParam, ExamKindAddParam, ExamKindUpdateParam, ExamAddParam, ExamListParam, SourceFileDeleteParam, \
    QuestionDeleteBulkParam


class ExamKindInstance(object):

    def __init__(self, t: Jojo):
        self.t = t

    def test_create(self):
        param = ExamKindAddParam("月考")
        exam = self.t.exam_kind_add(param)
        print(json.dumps(exam.json(), indent=4))

    def test_list(self):
        rs = self.t.exam_kind_list()
        rs = [r.json() for r in rs]
        print(rs)
