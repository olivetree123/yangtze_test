import json
import random

from jojo import Jojo
from entity.base import UserEntity, SchoolEntity, PhaseEntity, SubjectEntity,  TextBookEditionEntity, TextBookEntity, \
    KnowledgeEntity, ChapterEntity, ExamEntity, ExamKindEntity, QuestionEntity, SourceFileEntity, ResourceEntity
from entity.params import LogInParam, SchoolAddParam, PhaseAddParam, SubjectAddParam, TbEditionAddParam, \
    TextBookAddParam, KnowledgeAddParam, ChapterAddParam, QuestionUploadParam, QuestionListParam, \
    QuestionLabelParam, SourceFilePublishParam, SourceFileUpdateParam, ResourceAddParam, ResourceChapterParam, \
    ResourceKnowledgeParam, ExamKindAddParam, ExamKindUpdateParam, ExamAddParam, ExamListParam, SourceFileDeleteParam, \
    QuestionDeleteBulkParam, FocusParam


QUESTION_FILE_PATH = "/Users/gao/Downloads/demo-2.docx"


class QuestionInstance(object):

    def __init__(self, t: Jojo):
        self.t = t

    def test_upload(self):
        """测试导入习题"""
        subjects = self.t.subject_list()
        subject = subjects[0]
        param = QuestionUploadParam(subject.uid, QUESTION_FILE_PATH)
        source_file = self.t.question_upload(param)
        param = QuestionListParam(sourcefile_id=source_file.uid)
        rs = self.t.question_list(param)
        if rs and len(rs) > 0:
            print("Success to upload question")
        else:
            print("Failed to upload question")

    def test_list(self):
        """测试题目列表"""
        param = QuestionListParam(page=1, sourcefile_id="fef9cdb1-7af4-464b-835b-d04fc05587b1")
        rs = self.t.question_list(param)
        if rs and len(rs) > 0:
            print(json.dumps(rs[0].json(), indent=4))
            print("Success to list question")
        else:
            print("Failed to list question")

    def test_delete(self):
        """测试删除习题"""
        param = QuestionListParam()
        rs = self.t.question_list(param)
        if not rs:
            raise Exception("习题列表为空，无法删除")
        questions = rs[:2]
        questions_ids = [q.uid for q in questions]
        print("即将删除以下习题：", questions_ids)
        param = QuestionDeleteBulkParam(questions_ids)
        self.t.question_delete_bulk(param)
        print("删除成功")
        print("开始验证是否成功")
        for question in questions:
            self.t.question_get(question)

    def test_label(self):
        """测试更新/删除标注"""
        param = QuestionListParam()
        rs = self.t.question_list(param)
        if not rs:
            raise Exception("习题列表为空，无法标注")
        question = rs[0]
        chapters = self.t.chapter_list()
        if not chapters:
            raise Exception("章节列表为空，无法标注")
        chapters = [c.uid for c in chapters[:2]]
        print("chapters = ", chapters)
        param = QuestionLabelParam([question.uid], chapters=chapters)
        questions = self.t.question_update_label(param)
        for question in questions:
            cs = [c.uid for c in question.chapter]
            if set(cs).intersection(set(chapters)) != set(chapters):
                print("标注失败！")
                return
        print("标注成功！")
        questions = self.t.question_remove_label(param)
        for question in questions:
            cs = [c.uid for c in question.chapter]
            if set(cs).intersection(set(chapters)) != set():
                print("删除标注失败！")
                return
        print("删除标注成功！")

    def test_diff_level_list(self):
        pass

