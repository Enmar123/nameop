# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:15:39 2019

@author: Jason
"""

class filename:
    """
    This class serves as a container. Use it to store operation descriptors
    and build your file name. 
    
    Variables:
        self.dir     = directory
        self.desc    = original file descriptor
        self.pre_op  = pre operations
        self.op      = operations
        self.post_op = post operations
        self.ext     = file extension
        self.sep     = descriptor separator
    
    Format: 
        <self.dir><self.name><self.pre_op><self.op><self.post_op><self.ext>
    """
    
    def __init__(self, filepath=None):
        self.dir = None
        self.pre_op = None
        self.desc = None
        self.op = None
        self.post_op = None
        self.ext = None
        self.sep = '_'
        
        self.original = filepath
        self.path = None
        self.name = None
        
        self._class_driver(filepath)
        self._update()
        
        
    def __getitem__(self, item):
        return #'Do i need one?'
    
    def __repr__(self):
        return 'filepath(' + repr(self.path) + ')'
    
    # Controls how class input data is handeled
    def _class_driver(self, data):
        if data is None:
            return
        elif isinstance(data, str):
            fileparts = data.split('/')
            if len(fileparts) > 1:
                if isinstance(fileparts[0:-1], str):
                    self.dir = [fileparts[0:-1]]
                else:
                    self.dir = fileparts[0:-1]
            fileparts = fileparts[-1].split('.')
            if len(fileparts) > 1:
                self.desc = ['.'.join(fileparts[0:-1])]
                self.ext  = [fileparts[-1]]
            else:
                self.desc = fileparts
        else:
            raise TypeError('Expected input of type string')
            
    # unsure if a function driver is needed, meh.
    def _fcn_driver(self, data):
        if isinstance(data, str):
            return data
        else:
            raise TypeError('Expected input of type string')
    
    # Updates self.name and self.path with proper strings
    def _update(self):
        self.name = self.get_name()
        filepath_parts = [self.get_dir(), self.get_name()]
        filepath = []
        for part in filepath_parts:
            if part is not None:
                filepath.append(part)
        if len(filepath) == 0:
            return
        else:
            self.path = '/'.join(filepath) 
            
    ###########################################################################
    # --- ADD Functions --- #
    ###########################################################################
    
    def add_pre(self, string):
        """
        Add a pre-operation in the form of a string to your filename.
        """
        if self.pre_op is None:
            self.pre_op = [string]
        else:
            self.pre_op.append(string)
        self._update()
    
    
    def add_op(self, string):
        """
        Add a standard operation in the form of a string to your filename.
        """
        self._fcn_driver(string)
        if self.op is None:
            self.op = [string]
        else:
            self.op.append(string)
        self._update()
    
    def add_post(self, string):
        """
        Add a post operation in the form of a string to your filename.
        """
        if self.post_op is None:
            self.post_op = [string]
        else:
            self.post_op.append(string)
        self._update()
        
    def add_dir(self, string):
        """
        Add a sub directory to your filename.
        """
        if self.dir is None:
            # Special case for the root directory
            if string is '/':
                self.dir = ['']
            else:
                self.dir = [string]
        else:
            self.dir.append(string)
        self._update()
        
    ###########################################################################
    # --- POP Functions --- #
    ###########################################################################
    
    def pop_dir(self):
        """
        Remove the latest folder from the file directory.
        """
        self.dir.pop()
        # reset an empy self.dir to None
        if len(self.dir) == 0:
            self.dir = None
        self._update()
        
    ###########################################################################
    # --- REP Functions --- #
    ###########################################################################
    
    def rep_ext(self, string):
        """
        Replace the file extension with the input string.
        """
        self.ext = [string]
        self._update
        
    def rep_sep(self, string):
        """
        Replace the descriptor separator with the input string.
        """
        self.sep = string
        self._update()
            
    ###########################################################################
    # --- GET Functions --- #
    ###########################################################################    
    
    def get_dir(self):
        if self.dir is not None:
            return '/'.join(self.dir)
        else:
            return None
    
    def get_name(self):
        constructor = [self.get_preop(), self.get_desc(), 
                       self.get_op(), self.get_postop()]
        filename_parts=[]    
        for part in constructor:
            if part is not None:
                filename_parts.append(part)
        filename = self.sep.join(filename_parts)
        if self.get_ext() is not None:
            filename = filename + '.' + self.get_ext()
        return filename
                
    def get_preop(self):
        if self.pre_op is not None:
            return self.sep.join(self.pre_op)
        else:
            return None
    
    def get_desc(self):
        if self.desc is not None:
            return self.sep.join(self.desc)
        else:
            return None
    
    def get_op(self):
        if self.op is not None:
            return self.sep.join(self.op)
        else:
            return None
    
    def get_postop(self):
        if self.post_op is not None:
            return self.sep.join(self.post_op)
        else:
            return None
    
    def get_ext(self):
        if self.ext is not None:
            return self.sep.join(self.ext)
        else:
            return None
    
             
    
        
        