#                 © Copyright 2023
#          Licensed under the MIT License
#        https://opensource.org/licenses/MIT
#           https://github.com/OctoDiary

from typing import Optional, List, Any
from pydantic import Field
from datetime import datetime
from octodiary.types.model import DT, Type


class Teacher(Type):
    last_name: Optional[str] = Field(None, alias="last_name")
    first_name: Optional[str] = Field(None, alias="first_name")
    middle_name: Optional[str] = Field(None, alias="middle_name")
    birth_date: Optional[DT] = Field(None, alias="birth_date")
    sex: Optional[str] = None
    user_id: Optional[int] = Field(None, alias="user_id")


class Grade(Type):
    """Модель оценки в разных системах"""
    five: Optional[float] = None
    ten: Optional[float] = None
    hundred: Optional[float] = None
    origin: Optional[str] = None


class Value(Type):
    name: Optional[str] = None
    nmax: Optional[float] = None
    grade: Optional[Grade] = None
    grade_system_id: Optional[int] = Field(None, alias="grade_system_id")
    grade_system_type: Optional[str] = Field(None, alias="grade_system_type")


class Criterion(Type):
    name: Optional[str] = None
    value: Optional[str] = None


class Mark(Type):
    id: Optional[int] = None
    value: Optional[str] = None
    values: Optional[List[Value]] = None
    comment: Optional[str] = None
    weight: Optional[int] = None
    point_date: Optional[DT] = Field(None, alias="point_date")
    control_form_name: Optional[str] = Field(None, alias="control_form_name")
    comment_exists: Optional[bool] = Field(None, alias="comment_exists")
    created_at: Optional[DT] = Field(None, alias="created_at")
    updated_at: Optional[DT] = Field(None, alias="updated_at")
    criteria: Optional[List[Criterion]] = None
    is_point: Optional[bool] = Field(None, alias="is_point")
    is_exam: Optional[bool] = Field(None, alias="is_exam")
    original_grade_system_type: Optional[str] = Field(None, alias="original_grade_system_type")


class HomeworkCount(Type):
    total_count: Optional[int] = Field(None, alias="total_count")
    ready_count: Optional[int] = Field(None, alias="ready_count")


class Lesson(Type):
    schedule_item_id: Optional[int] = Field(None, alias="schedule_item_id")
    subject_id: Optional[int] = Field(None, alias="subject_id")
    subject_name: Optional[str] = Field(None, alias="subject_name")
    course_lesson_type: Optional[Any] = Field(None, alias="course_lesson_type")
    teacher: Optional[Teacher] = None
    marks: Optional[List[Mark]] = None
    homework: Optional[str] = None
    lesson_type: Optional[str] = Field(None, alias="lesson_type")
    lesson_education_type: Optional[str] = Field(None, alias="lesson_education_type")
    evaluation: Optional[Any] = Field(None, alias="evaluation")
    absence_reason_id: Optional[int] = Field(None, alias="absence_reason_id")
    nonattendance_reason_id: Optional[int] = Field(None, alias="nonattendance_reason_id")
    disease_status_type: Optional[Any] = Field(None, alias="disease_status_type")
    bell_id: Optional[int] = Field(None, alias="bell_id")
    replaced: Optional[bool] = None
    homework_count: Optional[HomeworkCount] = Field(None, alias="homework_count")
    esz_field_id: Optional[Any] = Field(None, alias="esz_field_id")
    is_cancelled: Optional[bool] = Field(None, alias="is_cancelled")
    is_missed_lesson: Optional[bool] = Field(None, alias="is_missed_lesson")
    is_virtual: Optional[bool] = Field(None, alias="is_virtual")


class Activity(Type):
    type: Optional[str] = None  # "LESSON" или "BREAK"
    info: Optional[str] = None
    begin_utc: Optional[int] = Field(None, alias="begin_utc")
    end_utc: Optional[int] = Field(None, alias="end_utc")
    begin_time: Optional[str] = Field(None, alias="begin_time")
    end_time: Optional[str] = Field(None, alias="end_time")
    room_number: Optional[str] = Field(None, alias="room_number")
    room_name: Optional[str] = Field(None, alias="room_name")
    building_name: Optional[str] = Field(None, alias="building_name")
    lesson: Optional[Lesson] = None
    duration: Optional[int] = None  # для перемен
    homework_presence_status_id: Optional[int] = Field(None, alias="homework_presence_status_id")


class ScheduleResponse(Type):
    summary: Optional[str] = None
    date: Optional[DT] = None
    activities: Optional[List[Activity]] = None
    has_homework: Optional[bool] = Field(None, alias="has_homework")
