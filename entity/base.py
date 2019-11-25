import json
import copy
from typing import Dict


class Entity(object):

    def json(self):
        r = copy.deepcopy(self.__dict__)
        for key, val in r.items():
            if isinstance(val, Entity):
                r[key] = val.json()
            elif isinstance(val, (list, tuple)):
                for i in range(len(val)):
                    if isinstance(val[i], Entity):
                        val[i] = val[i].json()
        return r


class UserEntity(Entity):

    def __init__(self, uid, name, token, role):
        self.uid = uid
        self.name = name
        self.role = role
        self.token = token

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        return cls(data["uid"], data["username"], data.get("token"), data["role"])


class SchoolEntity(Entity):

    def __init__(self, uid, name, province, city, area):
        self.uid = uid
        self.name = name
        self.province = province
        self.city = city
        self.area = area

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        return cls(data["uid"], data["name"], data["province"], data["city"], data["area"])


class SubjectEntity(Entity):
    """学科"""

    def __init__(self, uid, name, num):
        self.uid = uid
        self.num = num
        self.name = name

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        return cls(data["uid"], data["name"], data.get("num", 100))


class TextBookEditionEntity(Entity):
    """教材版本"""

    def __init__(self, uid, name, num, subject: SubjectEntity):
        if subject and not isinstance(subject, SubjectEntity):
            raise TypeError("subject should be type of Subject, but {} found".format(type(subject)))
        self.uid = uid
        self.num = num
        self.name = name
        self.subject = subject

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        subject = SubjectEntity.loads(data.get("subject"))
        return cls(data["uid"], data["name"], data.get("num", 100), subject)


class TextBookEntity(Entity):

    def __init__(self, uid, name, num, edition: TextBookEditionEntity):
        if edition and not isinstance(edition, TextBookEditionEntity):
            raise TypeError("edition should be type of TextBookEdition, but {} found".format(type(edition)))
        self.uid = uid
        self.num = num
        self.name = name
        self.edition = edition

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        edition = TextBookEditionEntity.loads(data.get("edition"))
        return cls(data["uid"], data["name"], data["num"], edition)


class PhaseEntity(Entity):

    def __init__(self, uid, name, num):
        self.uid = uid
        self.num = num
        self.name = name

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        return cls(data["uid"], data["name"], data["num"])


class GradeEntity(Entity):

    def __init__(self, uid, name, num, phase: PhaseEntity):
        if phase and not isinstance(phase, PhaseEntity):
            raise TypeError("phase should be type of Phase, but {} found".format(type(phase)))
        self.uid = uid
        self.num = num
        self.name = name
        self.phase = phase

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        phase = PhaseEntity.loads(data.get("phase"))
        return cls(data["uid"], data["name"], data["num"], phase)


class ChapterEntity(Entity):

    def __init__(self, uid, name, textbook, parent=None, num=100):
        self.uid = uid
        self.num = num
        self.name = name
        self.parent = parent
        self.textbook = textbook

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        return cls(data["uid"], data["name"], data["textbook"], data["p"], data["num"])


class QuestionTypeEntity(Entity):

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        return cls(data["uid"], data["name"])


class QuestionEntity(Entity):

    def __init__(self, uid, content, subject, source_file, q_type, q_year, is_sort, school, chapter, knowledge, label,
                 answer, explain, options, user, created):
        self.uid = uid
        self.user = user
        self.label = label
        self.school = school
        self.q_type = q_type
        self.q_year = q_year
        self.is_sort = is_sort
        self.content = content
        self.chapter = chapter
        self.created = created
        self.knowledge = knowledge
        self.answer = answer
        self.explain = explain
        self.options = options
        self.subject = subject
        self.source_file = source_file

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        chapters = []
        knowledges = []
        q_type = QuestionTypeEntity.loads(data["q_type"])
        subject = SubjectEntity.loads(data["subject"])
        school = SchoolEntity.loads(data["school"])
        user = UserEntity.loads(data["user"])
        source_file = SourceFileEntity.loads(data["source_file"])
        for k in data["knowledge"]:
            knowledges.append(KnowledgeEntity.loads(k))
        for c in data["chapter"]:
            chapters.append(ChapterEntity.loads(c))
        return cls(
            uid=data["uid"],
            content=data["content"],
            subject=subject,
            source_file=source_file,
            q_type=q_type,
            q_year=data["q_year"],
            is_sort=data["is_sort"],
            school=school,
            chapter=chapters,
            knowledge=knowledges,
            label=data["label"],
            answer=data["answer"],
            explain=data["explain"],
            options=data["options"],
            created=data["created"],
            user=user,
        )


class SourceFileEntity(Entity):

    def __init__(self, uid, name, phase, grade, subject, file):
        self.uid = uid
        self.name = name
        self.phase = phase
        self.grade = grade
        self.subject = subject
        self.file = file

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        grade = GradeEntity.loads(data["grade"])
        phase = PhaseEntity.loads(data["phase"])
        subject = SubjectEntity.loads(data["subject"])
        return cls(data["uid"], data["name"], phase, grade, subject, data["file"])


class KnowledgeEntity(Entity):

    def __init__(self, uid, name, subject_id, num=100, parent=None, tag=None):
        self.uid = uid
        self.name = name
        self.num = num
        self.tag = tag
        self.p = parent
        self.subject_id = subject_id

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        return cls(data["uid"], data["name"], data["subject"], data["num"], data["p"], data["tag"])


class ResourceKindEntity(Entity):

    def __init__(self, uid, name, subkinds=None):
        self.uid = uid
        self.name = name
        self.subkinds = subkinds

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        subkinds = []
        for kind in data["subkinds"]:
            subkinds.append(cls(kind["uid"], kind["name"]))
        return cls(data["uid"], data["name"], subkinds)


class ResourceCategoryEntity(Entity):

    def __init__(self, uid, name, school):
        self.uid = uid
        self.name = name
        self.school = school

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        school = SchoolEntity.loads(data["school"])
        return cls(data["uid"], data["name"], school)


class ResourceEntity(Entity):

    def __init__(self, uid, name, file, kind, status, school, phase, grade, subject, user, chapters, knowledges, file_object):
        self.uid = uid
        self.name = name
        self.file = file
        self.kind = kind
        self.phase = phase
        self.grade = grade
        self.school = school
        self.subject = subject
        self.user = user
        self.chapters = chapters
        self.status = status
        self.knowledges = knowledges
        self.file_object = file_object

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        user = UserEntity.loads(data["user"])
        kind = ResourceKindEntity.loads(data["kind"])
        phase = PhaseEntity.loads(data["phase"])
        grade = GradeEntity.loads(data["grade"])
        subject = SubjectEntity.loads(data["subject"])
        school = SchoolEntity.loads(data["school"])
        chapters = []
        knowledges = []
        for c in data["chapter"]:
            chapters.append(ChapterEntity.loads(c))
        for k in data["knowledge"]:
            knowledges.append(KnowledgeEntity.loads(k))
        return cls(
            uid=data["uid"],
            name=data["name"],
            file=data["file"],
            kind=kind,
            status=data["status"],
            school=school,
            phase=phase,
            grade=grade,
            subject=subject,
            user=user,
            chapters=chapters,
            knowledges=knowledges,
            file_object=data["file_object"],
        )


class ExamEntity(Entity):

    def __init__(self, uid, name, kind, phase, grade, subject, school, year):
        self.uid = uid
        self.name = name
        self.year = year
        self.kind = kind
        self.phase = phase
        self.grade = grade
        self.school = school
        self.subject = subject

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        kind = ExamKindEntity.loads(data["kind"])
        phase = PhaseEntity.loads(data["phase"])
        grade = GradeEntity.loads(data["grade"])
        subject = SubjectEntity.loads(data["subject"])
        school = SchoolEntity.loads(data["school"])
        return cls(data["uid"], data["name"], kind, phase, grade, subject, school, data["year"])


class ExamKindEntity(Entity):

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        return cls(data["uid"], data["name"])


class FocusEntity(Entity):

    def __init__(self, uid, kind, exam=None, question=None, resource=None):
        self.uid = uid
        self.kind = kind
        self.exam = exam
        self.question = question
        self.resource = resource

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        return cls(data["uid"], data["kind"], data.get("exam"), data.get("question"), data.get("resource"))


class DownloadHistoryEntity(Entity):

    def __init__(self, uid, kind, exam: ExamEntity = None, resource: ResourceEntity = None):
        self.uid = uid
        self.kind = kind
        self.exam = exam
        self.resource = resource

    @classmethod
    def loads(cls, data: Dict):
        if not data:
            return None
        exam = ExamEntity.loads(data["exam"])
        resource = ResourceEntity.loads(data["resource"])
        return cls(data["uid"], data["kind"], exam, resource)
