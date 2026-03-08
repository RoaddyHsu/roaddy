"""
行銷助手模組
"""

from .base_assistant import BaseAssistant
from .manager import ManagerAssistant
from .personnel_a import PersonnelAAssistant
from .personnel_b import PersonnelBAssistant
from .personnel_c import PersonnelCAssistant
from .personnel_d import PersonnelDAssistant
from .personnel_e import PersonnelEAssistant
from .asana_assistant import AsanaAssistant

__all__ = [
    "BaseAssistant",
    "ManagerAssistant",
    "PersonnelAAssistant",
    "PersonnelBAssistant",
    "PersonnelCAssistant",
    "PersonnelDAssistant",
    "PersonnelEAssistant",
    "AsanaAssistant",
]
