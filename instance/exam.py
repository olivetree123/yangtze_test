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


class ExamInstance(object):

    def __init__(self, t: Jojo):
        self.t = t

    def test_list(self):
        param = ExamListParam()
        rs = self.t.exam_list(param)
        if not rs:
            print("Failed to get exam list")
            return
        rs = [r.json() for r in rs]
        print(rs)
