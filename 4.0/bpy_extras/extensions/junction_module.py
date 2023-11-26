import sys
import typing

GenericType = typing.TypeVar("GenericType")


class JunctionModuleHandle:
    def register_module(self):
        ''' 

        '''
        pass

    def register_submodule(self, submodule_name, dirpath):
        ''' 

        '''
        pass

    def rename_directory(self, submodule_name, dirpath):
        ''' 

        '''
        pass

    def rename_submodule(self, submodule_name_src, submodule_name_dst):
        ''' 

        '''
        pass

    def submodule_items(self):
        ''' 

        '''
        pass

    def unregister_module(self):
        ''' 

        '''
        pass

    def unregister_submodule(self, submodule_name):
        ''' 

        '''
        pass
