from typing import Optional

from octodiary.types.model import DT, Type


from typing import Optional, List
from datetime import datetime as DT
from pydantic import BaseModel


class UrlItem(BaseModel):
    url: Optional[str] = None
    type: Optional[str] = None


class Material(BaseModel):
    uuid: Optional[str] = None
    type: Optional[str] = None
    selected_mode: Optional[str] = None
    type_name: Optional[str] = None
    id: Optional[int] = None
    urls: Optional[List[UrlItem]] = None
    description: Optional[str] = None
    content_type: Optional[str] = None
    title: Optional[str] = None
    action_id: Optional[int] = None
    action_name: Optional[str] = None


class Payload(BaseModel):
    type: Optional[str] = None
    description: Optional[str] = None
    comments: Optional[List[str]] = None
    materials: Optional[List[Material]] = None
    homework: Optional[str] = None
    homework_entry_student_id: Optional[int] = None
    attachments: Optional[List[str]] = None
    subject_id: Optional[int] = None
    group_id: Optional[int] = None
    date: Optional[DT] = None
    date_assigned_on: Optional[str] = None
    subject_name: Optional[str] = None
    lesson_date_time: Optional[DT] = None
    is_done: Optional[bool] = None
    has_teacher_answer: Optional[bool] = None
    homework_id: Optional[int] = None
    homework_entry_id: Optional[int] = None
    homework_created_at: Optional[DT] = None
    homework_updated_at: Optional[DT] = None
    written_answer: Optional[str] = None
    date_prepared_for: Optional[DT] = None


class Homeworks(Type):
    payload: list[Payload] | None = None


class DoneHomework(Type):
    success: bool = None
