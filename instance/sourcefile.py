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


class SourceFileInstance(object):

    def __init__(self, t: Jojo):
        self.t = t

    def test_update(self):
        subjects = self.t.subject_list()
        # print(json.dumps([s.json() for s in subjects], indent=4))
        print("学科数量 = ", len(subjects))
        n = random.randint(0, len(subjects)-1)
        rs = self.t.sourcefile_list()
        sourcefile = rs[0]
        print("当前源文件信息：")
        print(json.dumps(sourcefile.json(), indent=4))
        print("准备更新源文件信息，new subject_id = ", subjects[n].uid)
        param = SourceFileUpdateParam(sourcefile.uid, None, subjects[n].uid)
        sourcefile = self.t.sourcefile_update(param)
        print("更新后源文件信息：")
        print(json.dumps(sourcefile.json(), indent=4))

    def test_list(self):
        rs = self.t.sourcefile_list()
        rs = [r.json() for r in rs]
        print(rs)
