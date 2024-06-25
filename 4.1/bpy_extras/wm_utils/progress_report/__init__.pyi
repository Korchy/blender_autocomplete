import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class ProgressReport:
    curr_step: typing.Any
    running: typing.Any
    start_time: typing.Any
    steps: typing.Any
    wm: typing.Any

    def enter_substeps(self, nbr, msg=""):
        """

        :param nbr:
        :param msg:
        """
        ...

    def finalize(self): ...
    def initialize(self, wm=None):
        """Initialize self.  See help(type(self)) for accurate signature.

        :param wm:
        """
        ...

    def leave_substeps(self, msg=""):
        """

        :param msg:
        """
        ...

    def start(self): ...
    def step(self, msg="", nbr=1):
        """

        :param msg:
        :param nbr:
        """
        ...

    def update(self, msg=""):
        """

        :param msg:
        """
        ...

class ProgressReportSubstep:
    """A sub-step context manager for ProgressReport.It can be used to generate other sub-step contexts too, and can act as a (limited) proxy of its real ProgressReport.Its exit method always ensure ProgressReport is back on 'level' it was before entering this context.
    This means it is especially useful to ensure a coherent behavior around code that could return/continue/break
    from many places, without having to bother to explicitly leave sub-step in each and every possible place!
    """

    final_msg: typing.Any
    level: typing.Any
    msg: typing.Any
    nbr: typing.Any
    progress: typing.Any

    def enter_substeps(self, nbr, msg=""):
        """

        :param nbr:
        :param msg:
        """
        ...

    def leave_substeps(self, msg=""):
        """

        :param msg:
        """
        ...

    def step(self, msg="", nbr=1):
        """

        :param msg:
        :param nbr:
        """
        ...
