import json

from jojo import Jojo
from entity.base import UserEntity, SchoolEntity, PhaseEntity, SubjectEntity,  TextBookEditionEntity, TextBookEntity, \
    KnowledgeEntity, ChapterEntity, ExamEntity, ExamKindEntity, QuestionEntity, SourceFileEntity, ResourceEntity
from entity.params import LogInParam, SchoolAddParam, PhaseAddParam, SubjectAddParam, TbEditionAddParam, \
    TextBookAddParam, KnowledgeAddParam, ChapterAddParam, QuestionUploadParam, QuestionListParam, \
    QuestionLabelParam, SourceFilePublishParam, SourceFileUpdateParam, ResourceAddParam, ResourceChapterParam, \
    ResourceKnowledgeParam, ExamKindAddParam, ExamKindUpdateParam, ExamAddParam, ExamListParam, SourceFileDeleteParam, \
    QuestionDeleteBulkParam


class BaseDataInstance(object):

    def __init__(self, t: Jojo):
        self.t = t

    def create_school(self):
        param = SchoolAddParam("实验中学", "浙江省", "杭州市", "滨江区")
        school = self.t.school_add(param)
        print("Success to create school")

    def list_school(self):
        pass

    def create_phase(self):
        param = PhaseAddParam("高中222")
        phase = self.t.phase_add(param)
        print(json.dumps(phase.json()))
        print("Success to create phase")

    def list_phase(self):
        pass

    def create_subject(self):
        phase = self.t.phase_list()[0]
        param = SubjectAddParam("物理", phase.uid)
        subject = self.t.subject_add(param)
        print(json.dumps(subject.json()))
        print("Success to create subject")

    def list_subject(self):
        pass

    def create_grade(self):
        pass

    def list_grade(self):
        pass

    def create_chapter(self):
        textbook = self.t.textbook_list()[0]
        param = ChapterAddParam("第一章", textbook.uid)
        r = self.t.chapter_add(param)
        print(json.dumps(r.json()))
        print("Success to create chapter")

    def list_chapter(self):
        pass

    def create_knowledge(self):
        subject = self.t.subject_list()[0]
        param = KnowledgeAddParam("知识点1", subject.uid)
        r = self.t.knowledge_add(param)
        print(json.dumps(r.json()))
        print("Success to create knowledge")

    def list_knowledge(self):
        pass

    def create_textbook_edition(self):
        subject = self.t.subject_list()[0]
        param = TbEditionAddParam("川教版", subject.uid)
        r = self.t.tb_edition_add(param)
        print(json.dumps(r.json()))
        print("Success to create textbook edition")

    def list_textbook_edition(self):
        pass

    def create_textbook(self):
        edition = self.t.tb_edition_list()[0]
        param = TextBookAddParam("教材 2", edition.uid)
        r = self.t.textbook_add(param)
        print(json.dumps(r.json()))
        print("Success to create textbook")

    def list_textbook(self):
        pass

    def create_all(self):
        # self.create_school()
        self.create_phase()
        # self.create_subject()
        # self.create_textbook_edition()
        # self.create_textbook()
        # self.create_grade()
        # self.create_chapter()
        # self.create_knowledge()

