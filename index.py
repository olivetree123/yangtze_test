from jojo import Jojo
from config import YANGTZE_HOST, YANGTZE_PORT
from instance import SubjectInstance, SourceFileInstance, QuestionInstance, ResourceInstance, ExamKindInstance, \
    ExamInstance, BaseDataInstance, FocusInstance
from entity.params import LogInParam


if __name__ == "__main__":
    t = Jojo(host=YANGTZE_HOST, port=YANGTZE_PORT)
    # param = SignUpParam("admin", "admin@123", "gaojian@h3c.com", 1)
    # t.sign_up(param)
    login_param = LogInParam("admin", "admin@123")
    t.sign_in(login_param)
    t.school_list()
    baseDataIns = BaseDataInstance(t)
    # subjectIns = SubjectInstance(t)
    questionIns = QuestionInstance(t)
    sourcefileIns = SourceFileInstance(t)
    resourceIns = ResourceInstance(t)
    examKindIns = ExamKindInstance(t)
    examIns = ExamInstance(t)
    focusIns = FocusInstance(t)
    # baseDataIns.create_all()
    # questionIns.test_upload()
    # sourcefileIns.test_list()
    questionIns.test_list()
    # sourcefileIns.test_update()
    # questionIns.test_label()
    # resourceIns.test_upload()
    # resourceIns.test_my_list()
    # resourceIns.test_list()
    # resourceIns.test_publish()
    # resourceIns.test_list()
    # resourceIns.test_category_list()
    # resourceIns.test_download()
    # resourceIns.test_download_history()
    # examKindIns.test_create()
    # examKindIns.test_list()
    # examIns.test_list()
    # focusIns.test_focus_list()
    # focusIns.test_focus_resource()
    # focusIns.test_focus_list()
