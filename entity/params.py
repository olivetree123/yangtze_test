import os
import base64
from typing import List

from errors import ParamError


class Param(object):

    def json(self):
        return self.__dict__


class SignUpParam(Param):

    def __init__(self, username, password, email, role):
        self.email = email
        self.role = role
        self.username = username
        self.password = base64.b64encode(password.encode("utf8")).decode("ascii")


class LogInParam(Param):

    def __init__(self, username, password):
        if not username:
            raise ParamError("username should not be None")
        if not password:
            raise ParamError("password should not be None")
        self.username = username
        self.password = base64.b64encode(password.encode("utf8")).decode("ascii")


class SchoolAddParam(Param):

    def __init__(self, name, province, city, area):
        if not name:
            raise ParamError("name should not be None")
        if not province:
            raise ParamError("province should not be None")
        if not city:
            raise ParamError("city should not be None")
        if not area:
            raise ParamError("area should not be None")
        self.name = name
        self.province = province
        self.city = city
        self.area = area


class PhaseAddParam(Param):

    def __init__(self, name, num=100):
        if not name:
            raise ParamError("name should not be None")
        self.name = name
        self.num = num


class SubjectAddParam(Param):

    def __init__(self, name, phase_id, num=100):
        if not name:
            raise ParamError("name should not be None")
        if not phase_id:
            raise ParamError("phase_id should not be None")
        self.name = name
        self.phase = phase_id
        self.num = num


class TbEditionAddParam(Param):

    def __init__(self, name, subject_id):
        if not name:
            raise ParamError("name should not be None")
        if not subject_id:
            raise ParamError("subject_id should not be None")
        self.name = name
        self.subject = subject_id


class TextBookAddParam(Param):

    def __init__(self, name, edition_id):
        if not name:
            raise ParamError("name should not be None")
        if not edition_id:
            raise ParamError("edition_id should not be None")
        self.name = name
        self.edition = edition_id


class KnowledgeAddParam(Param):

    def __init__(self, name, subject_id):
        if not name:
            raise ParamError("name should not be None")
        if not subject_id:
            raise ParamError("subject_id should not be None")
        self.name = name
        self.subject = subject_id


class ChapterAddParam(Param):

    def __init__(self, name, textbook_id):
        if not name:
            raise ParamError("name should not be None")
        if not textbook_id:
            raise ParamError("textbook_id should not be None")
        self.name = name
        self.textbook = textbook_id


class QuestionUploadParam(Param):

    def __init__(self, subject_id, file_path):
        if not subject_id:
            raise ParamError("subject_id should not be None")
        if not file_path:
            raise ParamError("file_path should not be None")
        if not os.path.exists(file_path):
            raise ParamError("file_path={} not exists".format(file_path))
        self.subject_id = subject_id
        self.file_obj = open(file_path, "rb")


class QuestionListParam(Param):

    def __init__(self, user_id=None, subject_id=None, knowledge_id=None, sourcefile_id=None, q_type_id=None, year=None, page=1):
        self.year = year
        self.user_id = user_id
        self.q_type_id = q_type_id
        self.subject_id = subject_id
        self.knowledge_id = knowledge_id
        self.sourcefile_id = sourcefile_id
        self.page = page


class QuestionLabelParam(Param):

    def __init__(self,
                 question_ids: List[str],
                 subject_id: str = None,
                 chapters: List[str] = None,
                 knowledges: List[str] = None,
                 labels: List[str] = None):
        if not isinstance(question_ids, (list, tuple)):
            raise ParamError("question_ids should not be type of list or tuple, but {} found".format(type(question_ids)))
        self.questions = question_ids
        self.subject_id = subject_id
        self.chapters = chapters
        self.knowledges = knowledges
        self.labels = labels


class QuestionDeleteBulkParam(Param):

    def __init__(self, question_ids: List[str]):
        if not isinstance(question_ids, (list, tuple)):
            raise ParamError("question_ids should be type of list, but {} found".format(type(question_ids)))
        self.questions = question_ids


class SourceFilePublishParam(Param):

    def __init__(self, sourcefile_id):
        self.sourcefile_id = sourcefile_id


class SourceFileUpdateParam(Param):

    def __init__(self, sourcefile_id, grade_id, subject_id):
        self.sourcefile_id = sourcefile_id
        self.grade_id = grade_id
        self.subject_id = subject_id

    def json(self):
        return {"grade_id": self.grade_id, "subject_id": self.subject_id}


class SourceFileDeleteParam(Param):

    def __init__(self, sourcefile_id):
        self.sourcefile_id = sourcefile_id


class ResourceAddParam(Param):

    def __init__(self, subject_id, file_path):
        if not subject_id:
            raise ParamError("subject_id should not be None")
        if not file_path:
            raise ParamError("file_path should not be None")
        if not os.path.exists(file_path):
            raise ParamError("file_path={} not exists".format(file_path))
        self.subject_id = subject_id
        self.file_obj = open(file_path, "rb")


class ResourcePublishParam(Param):

    def __init__(self, resources=None):
        if resources and not isinstance(resources, (list, tuple)):
            raise ParamError("resources should be list or tuple, but {} found".format(type(resources)))
        self.resources = resources if resources else []

    def add(self, resource_id):
        self.resources.append(resource_id)


class ResourceChapterParam(Param):

    def __init__(self, resource_id, chapters: List):
        if not isinstance(chapters, (list, tuple)):
            raise ParamError("chapters should be type of list, but {} found".format(type(chapters)))
        self.chapters = chapters
        self.resource_id = resource_id


class ResourceKnowledgeParam(Param):

    def __init__(self, resource_id, knowledges: List):
        if not isinstance(knowledges, (list, tuple)):
            raise ParamError("chapters should be type of list, but {} found".format(type(chapters)))
        self.knowledges = knowledges
        self.resource_id = resource_id


class ResourceListParam(Param):

    def __init__(self, category_id, is_my_own, status=0):
        self.is_my_own = is_my_own
        self.status = status
        self.category_id = category_id


class ExamKindAddParam(Param):

    def __init__(self, name):
        self.name = name


class ExamKindUpdateParam(Param):

    def __init__(self, kind_id, name):
        self.name = name
        self.kind_id = kind_id

    def json(self):
        return {"name": self.name}


class ExamAddParam(Param):

    def __init__(self, name, kind_id, phase_id, grade_id, subject_id, year):
        self.name = name
        self.year = year
        self.kind_id = kind_id
        self.phase_id = phase_id
        self.grade_id = grade_id
        self.subject_id = subject_id


class ExamListParam(Param):

    def __init__(self, kind_id=None):
        self.kind_id = kind_id


class FocusParam(Param):

    def __init__(self, kind: int, exam_id: str = None, question_id: str = None, resource_id: str = None):
        self.kind = kind
        self.exam_id = exam_id
        self.question_id = question_id
        self.resource_id = resource_id


class FocusListParam(Param):

    def __init__(self, kind):
        self.kind = kind


class FocusRemoveParam(Param):

    def __init__(self, focus_ids):
        self.focus_ids = focus_ids


class DownloadHistoryParam(Param):

    def __init__(self, kind):
        self.kind = kind

