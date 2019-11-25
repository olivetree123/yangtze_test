import json
from typing import List, Dict
from winney import Winney

from errors import HTTPResponseError, ConditionError, ServerResponseError
from entity.params import LogInParam, SchoolAddParam, PhaseAddParam, SubjectAddParam, TbEditionAddParam, \
    TextBookAddParam, KnowledgeAddParam, ChapterAddParam, QuestionUploadParam, QuestionListParam, \
    QuestionLabelParam, SourceFilePublishParam, SourceFileUpdateParam, ResourceAddParam, ResourceChapterParam, \
    ResourceKnowledgeParam, ExamKindAddParam, ExamKindUpdateParam, ExamAddParam, ExamListParam, SourceFileDeleteParam, \
    QuestionDeleteBulkParam, ResourceListParam, ResourcePublishParam, SignUpParam, FocusParam, FocusRemoveParam, \
    FocusListParam, DownloadHistoryParam
from entity.base import UserEntity, SchoolEntity, PhaseEntity, SubjectEntity,  TextBookEditionEntity, TextBookEntity, \
    KnowledgeEntity, ChapterEntity, ExamEntity, ExamKindEntity, QuestionEntity, SourceFileEntity, ResourceEntity, \
    ResourceCategoryEntity, FocusEntity, DownloadHistoryEntity


"""
测试用例，可以使用 assert 判断结果是否满足条件
"""

QUESTION_FILE_PATH = "/Users/gao/Downloads/demo-2.docx"


class Jojo(object):

    def __init__(self, host, port):
        self.token = None
        self.school = None
        self.winney = Winney(host=host, port=port)
        self.init_functions()

    def init_functions(self):
        # 用户
        self.winney.register(method="POST", name="sign_up", uri="/yangtze/accounts/register/")
        self.winney.register(method="POST", name="sign_in", uri="/yangtze/login/")

        # 基础数据
        self.winney.register(method="POST", name="school_add", uri="/yangtze/schools/")
        self.winney.register(method="GET", name="school_list", uri="/yangtze/schools/")
        self.winney.register(method="POST", name="subject_add", uri="/yangtze/subjects/")
        self.winney.register(method="GET", name="subject_list", uri="/yangtze/subjects/")
        self.winney.register(method="GET", name="subject_get", uri="/yangtze/subjects/{subject_id}/")
        self.winney.register(method="POST", name="phase_add", uri="/yangtze/phases/")
        self.winney.register(method="GET", name="phase_list", uri="/yangtze/phases/")
        self.winney.register(method="GET", name="phase_get", uri="/yangtze/phases/{phase_id}/")
        self.winney.register(method="POST", name="knowledge_add", uri="/yangtze/knowledge/")
        self.winney.register(method="GET", name="knowledge_list", uri="/yangtze/knowledge/")
        self.winney.register(method="POST", name="chapter_add", uri="/yangtze/chapters/")
        self.winney.register(method="GET", name="chapter_list", uri="/yangtze/chapters/")
        self.winney.register(method="POST", name="tb_edition_add", uri="/yangtze/textbook_editions/")
        self.winney.register(method="GET", name="tb_edition_list", uri="/yangtze/textbook_editions/")
        self.winney.register(method="POST", name="textbook_add", uri="/yangtze/textbooks/")
        self.winney.register(method="GET", name="textbook_list", uri="/yangtze/textbooks/")
        self.winney.register(method="GET", name="diff_level_list", uri="/yangtze/diff_level/list/")

        # 资源
        self.winney.register(method="POST", name="resource_add", uri="/yangtze/resource/")
        self.winney.register(method="GET", name="resource_list", uri="/yangtze/resource/list/")
        self.winney.register(method="POST", name="resource_publish", uri="/yangtze/resource/publish/")
        self.winney.register(method="GET", name="resource_download", uri="/yangtze/resource/download/{resource_id}/")
        self.winney.register(method="POST", name="resource_chapter", uri="/yangtze/resource/chapter/")
        self.winney.register(method="POST", name="resource_knowledge", uri="/yangtze/resource/knowledge/")
        self.winney.register(method="GET", name="resource_category_list", uri="/yangtze/resource/category/list/")

        # 资源类别
        self.winney.register(method="POST", name="resource_kind_add", uri="/yangtze/resource_kind/")
        self.winney.register(method="GET", name="resource_kind_list", uri="/yangtze/resource_kind/list/")

        # 题目
        self.winney.register(method="POST", name="question_upload", uri="/yangtze/question/upload/")
        self.winney.register(method="POST", name="question_add", uri="/yangtze/question/")
        self.winney.register(method="GET", name="question_get", uri="/yangtze/question/{question_id}/")
        # self.winney.register(method="GET", name="question_list", uri="/yangtze/question/list/")
        self.winney.register(method="POST", name="question_list", uri="/yangtze/question/list/")
        self.winney.register(method="POST", name="question_update_label", uri="/yangtze/question/update/label/")
        self.winney.register(method="POST", name="question_remove_label", uri="/yangtze/question/remove/label/")
        self.winney.register(method="DELETE", name="question_delete", uri="/yangtze/question/{question_id}")
        self.winney.register(method="POST", name="question_delete_bulk", uri="/yangtze/question/delete/")
        self.winney.register(method="GET", name="sourcefile_list", uri="/yangtze/sourcefile/list/")
        self.winney.register(method="PUT", name="sourcefile_update", uri="/yangtze/sourcefile/{sourcefile_id}/")
        self.winney.register(method="POST", name="sourcefile_publish", uri="/yangtze/sourcefile/{sourcefile_id}/")
        self.winney.register(method="DELETE", name="sourcefile_delete", uri="/yangtze/sourcefile/{sourcefile_id}/")

        # 试卷
        self.winney.register(method="POST", name="exam_kind_add", uri="/yangtze/exam_kind/")
        self.winney.register(method="PUT", name="exam_kind_update", uri="/yangtze/exam_kind/{kind_id}/")
        self.winney.register(method="GET", name="exam_kind_get", uri="/yangtze/exam_kind/{kind_id}/")
        self.winney.register(method="DELETE", name="exam_kind_delete", uri="/yangtze/exam_kind/{kind_id}/")
        self.winney.register(method="GET", name="exam_kind_list", uri="/yangtze/exam_kind/list/")

        self.winney.register(method="POST", name="exam_add", uri="/yangtze/exam/")
        self.winney.register(method="GET", name="exam_list", uri="/yangtze/exam/list/")
        self.winney.register(method="PUT", name="exam_update", uri="/yangtze/exam/{exam_id}/")
        self.winney.register(method="GET", name="exam_get", uri="/yangtze/exam/{exam_id}/")
        self.winney.register(method="DELETE", name="exam_delete", uri="/yangtze/exam/{exam_id}/")

        # 收藏
        self.winney.register(method="POST", name="focus", uri="/yangtze/focus/")
        self.winney.register(method="GET", name="focus_list", uri="/yangtze/focus/list/")
        self.winney.register(method="POST", name="focus_remove", uri="/yangtze/focus/remove/")

        # 下载历史
        self.winney.register(method="GET", name="download_history", uri="/yangtze/download/history/")

    @staticmethod
    def get_data(r):
        if not r.ok():
            raise HTTPResponseError("出现异常，HTTP status code={}".format(r.status_code))
        data = r.json()
        if data["code"] != 0:
            raise ServerResponseError("服务器返回错误，code={}, message={}".format(data["code"], data["message"]))
        return data["data"]

    @staticmethod
    def check_type(param, tp):
        if not isinstance(param, tp):
            raise TypeError("param should be type of {}, but {} found".format(tp, type(param)))

    def sign_up(self, param: SignUpParam):
        r = self.winney.sign_up(json=param.json())
        user = UserEntity.loads(self.get_data(r))
        return user

    def sign_in(self, param: LogInParam):
        if not isinstance(param, LogInParam):
            raise TypeError("param should be type of LogInParam, but {} found".format(type(param)))
        r = self.winney.sign_in(json=param.json())
        user = UserEntity.loads(self.get_data(r))
        self.token = "Token " + user.token
        print("token = ", self.token)
        return user

    def school_add(self, param: SchoolAddParam):
        self.check_type(param, SchoolAddParam)
        r = self.winney.school_add(json=param.json(), headers={"Authorization": self.token})
        self.school = SchoolEntity.loads(self.get_data(r))
        return self.school

    def school_list(self):
        r = self.winney.school_list(headers={"Authorization": self.token})
        schools = self.get_data(r)["result"]
        schools = [SchoolEntity.loads(school) for school in schools] if schools else None
        self.school = schools[0] if schools else None
        return schools

    def phase_add(self, param: PhaseAddParam):
        self.check_type(param, PhaseAddParam)
        r = self.winney.phase_add(json=param.json(), headers={"Authorization": self.token})
        phase = PhaseEntity.loads(self.get_data(r))
        return phase

    def phase_list(self):
        r = self.winney.phase_list(headers={
            "Authorization": self.token,
            "X-Custom-Header-3School": self.school.uid
        })
        phases = self.get_data(r)["result"]
        phases = [PhaseEntity.loads(phase) for phase in phases] if phases else None
        return phases

    def subject_add(self, param: SubjectAddParam):
        self.check_type(param, SubjectAddParam)
        r = self.winney.subject_add(json=param.json(), headers={"Authorization": self.token})
        return SubjectEntity.loads(self.get_data(r))

    def subject_list(self):
        r = self.winney.subject_list(headers={
            "Authorization": self.token,
            "X-Custom-Header-3School": self.school.uid
        })
        subjects = self.get_data(r)["result"]
        subjects = [SubjectEntity.loads(subject) for subject in subjects] if subjects else None
        return subjects

    def tb_edition_add(self, param: TbEditionAddParam) -> TextBookEditionEntity:
        self.check_type(param, TbEditionAddParam)
        r = self.winney.tb_edition_add(json=param.json(), headers={"Authorization": self.token})
        return TextBookEditionEntity.loads(self.get_data(r))

    def tb_edition_list(self) -> List[TextBookEditionEntity]:
        r = self.winney.tb_edition_list(headers={
            "Authorization": self.token,
            "X-Custom-Header-3School": self.school.uid
        })
        editions = self.get_data(r)["result"]
        editions = [TextBookEditionEntity.loads(edition) for edition in editions] if editions else None
        return editions

    def textbook_add(self, param: TextBookAddParam) -> TextBookEntity:
        self.check_type(param, TextBookAddParam)
        r = self.winney.textbook_add(json=param.json(), headers={"Authorization": self.token})
        return TextBookEntity.loads(self.get_data(r))

    def textbook_list(self) -> [TextBookEntity]:
        r = self.winney.textbook_list(headers={
            "Authorization": self.token,
            "X-Custom-Header-3School": self.school.uid
        })
        textbooks = self.get_data(r)["result"]
        textbooks = [TextBookEntity.loads(tb) for tb in textbooks] if textbooks else None
        return textbooks

    def knowledge_add(self, param: KnowledgeAddParam) -> KnowledgeEntity:
        self.check_type(param, KnowledgeAddParam)
        r = self.winney.knowledge_add(json=param.json(), headers={"Authorization": self.token})
        return KnowledgeEntity.loads(self.get_data(r))

    def knowledge_list(self) -> [KnowledgeEntity]:
        r = self.winney.knowledge_list(headers={
            "Authorization": self.token,
            "X-Custom-Header-3School": self.school.uid
        })
        rs = self.get_data(r)["result"]
        rs = [KnowledgeEntity.loads(r) for r in rs] if rs else None
        return rs

    def chapter_add(self, param: ChapterAddParam) -> ChapterEntity:
        self.check_type(param, ChapterAddParam)
        r = self.winney.chapter_add(json=param.json(), headers={"Authorization": self.token})
        return ChapterEntity.loads(self.get_data(r))

    def chapter_list(self) -> List[ChapterEntity]:
        r = self.winney.chapter_list(headers={
            "Authorization": self.token,
            "X-Custom-Header-3School": self.school.uid
        })
        chapters = self.get_data(r)["result"]
        chapters = [ChapterEntity.loads(chapter) for chapter in chapters] if chapters else None
        return chapters

    def diff_level_list(self):
        r = self.winney.diff_level_list(headers={"Authorization": self.token})
        rs = self.get_data(r)
        print(rs)

    def question_upload(self, param: QuestionUploadParam) -> SourceFileEntity:
        self.check_type(param, QuestionUploadParam)
        r = self.winney.question_upload(
            data={
                "subject_id": param.subject_id
            },
            files={
                "file": param.file_obj
            },
            headers={"Authorization": self.token},
        )
        return SourceFileEntity.loads(self.get_data(r))

    def question_list(self, param: QuestionListParam) -> List[QuestionEntity]:
        self.check_type(param, QuestionListParam)
        r = self.winney.question_list(json=param.json(), headers={"Authorization": self.token})
        questions = self.get_data(r)["result"]  # 有分页参数
        # print(json.dumps(questions[0], indent=4))
        # print(questions[0]["uid"])
        questions = [QuestionEntity.loads(q) for q in questions] if questions else None
        return questions

    def question_get(self, param: QuestionEntity) -> QuestionEntity:
        self.check_type(param, QuestionEntity)
        r = self.winney.question_get(question_id=param.uid, headers={"Authorization": self.token})
        return QuestionEntity.loads(self.get_data(r))

    def question_update_label(self, param: QuestionLabelParam) -> List[QuestionEntity]:
        self.check_type(param, QuestionLabelParam)
        r = self.winney.question_update_label(json=param.json(), headers={"Authorization": self.token})
        questions = self.get_data(r)
        questions = [QuestionEntity.loads(q) for q in questions] if questions else None
        return questions

    def question_remove_label(self, param: QuestionLabelParam):
        self.check_type(param, QuestionLabelParam)
        r = self.winney.question_remove_label(json=param.json(), headers={"Authorization": self.token})
        questions = self.get_data(r)
        questions = [QuestionEntity.loads(q) for q in questions] if questions else None
        return questions

    def question_delete(self, param: QuestionEntity):
        self.check_type(param, QuestionEntity)
        r = self.winney.question_delete(question_id=param.uid, headers={"Authorization": self.token})
        return self.get_data(r)

    def question_delete_bulk(self, param: QuestionDeleteBulkParam):
        r = self.winney.question_delete_bulk(json=param.json(), headers={"Authorization": self.token})
        return self.get_data(r)

    def sourcefile_list(self) -> List[SourceFileEntity]:
        r = self.winney.sourcefile_list(headers={"Authorization": self.token})
        rs = self.get_data(r)["result"]
        rs = [SourceFileEntity.loads(r) for r in rs] if rs else None
        return rs

    def sourcefile_publish(self, param: SourceFilePublishParam):
        self.check_type(param, SourceFilePublishParam)
        r = self.winney.sourcefile_publish(sourcefile_id=param.sourcefile_id, headers={"Authorization": self.token})
        return SourceFileEntity.loads(self.get_data(r))

    def sourcefile_update(self, param: SourceFileUpdateParam):
        self.check_type(param, SourceFileUpdateParam)
        r = self.winney.sourcefile_update(
            sourcefile_id=param.sourcefile_id,
            json=param.json(),
            headers={"Authorization": self.token},
        )
        return SourceFileEntity.loads(self.get_data(r))

    def sourcefile_delete(self, param: SourceFileDeleteParam):
        self.check_type(param, SourceFileDeleteParam)
        r = self.winney.sourcefile_delete(sourcefile_id=param.sourcefile_id, headers={"Authorization": self.token})
        return self.get_data(r)

    def resource_add(self, param: ResourceAddParam):
        self.check_type(param, ResourceAddParam)
        r = self.winney.resource_add(data={
            "subject_id": param.subject_id
            },
            files={
                "file": param.file_obj
            },
            headers={"Authorization": self.token},
        )
        return ResourceEntity.loads(self.get_data(r))

    def resource_publish(self, param: ResourcePublishParam):
        r = self.winney.resource_publish(json=param.json(), headers={"Authorization": self.token})
        return ResourceEntity.loads(self.get_data(r))

    def resource_list(self, param: ResourceListParam):
        r = self.winney.resource_list(data=param.json(), headers={"Authorization": self.token})
        rs = self.get_data(r)["result"]
        rs = [ResourceEntity.loads(r) for r in rs] if rs else None
        return rs

    def resource_download(self, resource_id):
        r = self.winney.resource_download(resource_id=resource_id, headers={"Authorization": self.token})
        print("Success to download resource")
        print(r.headers)
        return r.content

    def resource_chapter(self, param: ResourceChapterParam):
        self.check_type(param, ResourceChapterParam)
        r = self.winney.resource_chapter(json=param.json(), headers={"Authorization": self.token})
        return ResourceEntity.loads(self.get_data(r))

    def resource_knowledge(self, param: ResourceKnowledgeParam):
        self.check_type(param, ResourceKnowledgeParam)
        r = self.winney.resource_knowledge(json=param.json(), headers={"Authorization": self.token})
        return ResourceEntity.loads(self.get_data(r))

    def resource_category_list(self):
        r = self.winney.resource_category_list(headers={"Authorization": self.token})
        rs = self.get_data(r)
        rs = [ResourceCategoryEntity.loads(r) for r in rs] if rs else None
        return rs

    def exam_kind_add(self, param: ExamKindAddParam):
        self.check_type(param, ExamKindAddParam)
        r = self.winney.exam_kind_add(json=param.json(), headers={"Authorization": self.token})
        return ExamKindEntity.loads(self.get_data(r))

    def exam_kind_update(self, param: ExamKindUpdateParam):
        self.check_type(param, ExamKindUpdateParam)
        r = self.winney.exam_kind_update(
            kind_id=param.kind_id,
            json=param.json(),
            headers={"Authorization": self.token},
        )
        return ExamKindEntity.loads(self.get_data(r))

    def exam_kind_get(self, param: ExamKindEntity):
        self.check_type(param, ExamKindEntity)
        r = self.winney.exam_kind_get(kind_id=param.uid, headers={"Authorization": self.token})
        return ExamKindEntity.loads(self.get_data(r))

    def exam_kind_list(self):
        r = self.winney.exam_kind_list(headers={"Authorization": self.token})
        kinds = self.get_data(r)
        kinds = [ExamKindEntity.loads(k) for k in kinds] if kinds else None
        return kinds

    def exam_add(self, param: ExamAddParam):
        self.check_type(param, ExamAddParam)
        r = self.winney.exam_add(json=param.json(), headers={"Authorization": self.token})
        return ExamEntity.loads(self.get_data(r))

    def exam_list(self, param: ExamListParam):
        self.check_type(param, ExamListParam)
        r = self.winney.exam_list(data=param.json(), headers={"Authorization": self.token})
        rs = self.get_data(r)["result"]
        rs = [ExamEntity.loads(r) for r in rs] if rs else None
        return rs

    def exam_get(self, param: ExamEntity):
        r = self.winney.exam_get(exam_id=param.uid, headers={"Authorization": self.token})
        return ExamEntity.loads(self.get_data(r))

    def focus(self, param: FocusParam) -> FocusEntity:
        self.check_type(param, FocusParam)
        r = self.winney.focus(json=param.json(), headers={"Authorization": self.token})
        return FocusEntity.loads(self.get_data(r))

    def focus_list(self, param: FocusListParam) -> List[FocusEntity]:
        r = self.winney.focus_list(data=param.json(), headers={"Authorization": self.token})
        rs = self.get_data(r)["result"]
        rs = [FocusEntity.loads(r) for r in rs] if rs else None
        return rs

    def focus_remove(self, param: FocusRemoveParam):
        r = self.winney.focus_remove(json=param.json())
        print("Success to remove focus")

    def download_history(self, param: DownloadHistoryParam):
        r = self.winney.download_history(data=param.json(), headers={"Authorization": self.token})
        rs = self.get_data(r)["result"]
        print(json.dumps(rs, indent=4))
        rs = [DownloadHistoryEntity.loads(r) for r in rs] if rs else None
        return rs
