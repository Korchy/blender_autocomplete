import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums

def rule_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.BoidruleTypeItems | None = "GOAL",
):
    """Add a boid rule to the current boid state

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy._typing.rna_enums.BoidruleTypeItems | None
    """

def rule_del(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete current boid rule

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def rule_move_down(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Move boid rule down in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def rule_move_up(execution_context: int | str | None = None, undo: bool | None = None):
    """Move boid rule up in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def state_add(execution_context: int | str | None = None, undo: bool | None = None):
    """Add a boid state to the particle system

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def state_del(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete current boid state

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def state_move_down(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Move boid state down in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def state_move_up(execution_context: int | str | None = None, undo: bool | None = None):
    """Move boid state up in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    """
