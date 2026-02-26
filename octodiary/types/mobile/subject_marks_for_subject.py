#                 © Copyright 2023
#          Licensed under the MIT License
#        https://opensource.org/licenses/MIT
#           https://github.com/OctoDiary

from typing import Any, Optional, Union
from pydantic import field_validator
from datetime import date, datetime

from octodiary.types.model import DT, Type


class Mark(Type):
    id: Optional[int] = None
    value: Optional[str] = None
    values: Optional[list] = None
    comment: Optional[str] = None
    weight: Optional[int] = None
    point_date: Optional[DT] = None
    control_form_name: Optional[str] = None
    comment_exists: Optional[bool] = None
    created_at: Optional[DT] = None
    updated_at: Optional[DT] = None
    criteria: Optional[Any] = None
    date: Optional[DT] = None
    is_exam: Optional[bool] = None
    is_point: Optional[bool] = None
    original_grade_system_type: Optional[str] = None


class Path(Type):
    value: Optional[int] = None
    remain: Optional[int] = None
    weight: Optional[int] = None


class Target(Type):
    value: Optional[int] = None
    remain: Optional[int] = None
    round: Optional[str] = None
    paths: Optional[list[Path]] = []


class Period(Type):
    start: Optional[Union[datetime, date, str]] = None
    end: Optional[Union[datetime, date, str]] = None
    title: Optional[str] = None
    dynamic: Optional[str] = None
    value: Optional[str] = None
    marks: Optional[list[Mark]] = []
    count: Optional[int] = None
    target: Optional[Target] = None
    fixed_value: Optional["str | int"] = None
    
    @field_validator('start', 'end', mode='before')
    @classmethod
    def parse_period_date(cls, v: Any) -> Any:
        """Преобразует строки вида 'dd.mm' в datetime объекты"""
        if v is None:
            return v
            
        if isinstance(v, (datetime, date)):
            return v
            
        if isinstance(v, str):
            try:
                return datetime.fromisoformat(v.replace('Z', '+00:00'))
            except (ValueError, TypeError):
                pass
            
            if '.' in v and len(v.split('.')) == 2:
                try:
                    day, month = map(int, v.split('.'))
                    current_year = datetime.now().year
                    
                    if month >= 9:
                        if datetime.now().month < 9:
                            year = current_year - 1
                        else:
                            year = current_year
                    else:
                        if datetime.now().month >= 9:
                            year = current_year + 1
                        else:
                            year = current_year
                    
                    return datetime(year, month, day)
                except (ValueError, TypeError):
                    pass
            
            return v
        
        return v


class SubjectMarksForSubject(Type):
    average: Optional[str] = None
    dynamic: Optional[str] = None
    periods: Optional[list[Period]] = None
    subject_name: Optional[str] = None
    subject_id: Optional[int] = None
    average_by_all: Optional[str] = None
