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
        
        self.path = None
        self.name = None
        
        self._driver(filepath)
        
    def __getitem__(self, item):
        return #'TODO'
    
    def __repr__(self):
        return repr(self.path)
    
    def _driver(self, filepath):
        # <TODO>
        # add support for missing directory
        # add case for missing file extension
        if filepath is None:
            return
        elif isinstance(filepath, str):
            filepath_parts = filepath.split('/')
            if len(filepath_parts) >= 2:
                self.dir = filepath_parts[0:-1]
                
            filename_parts = filepath_parts[-1].split('.')
            if len(filepath_parts) >= 2:
                self.desc = filename_parts[0:-1]
                self.ext = [filename_parts[-1]]
            self._update()
        else:
            raise ValueError('Input is not string')
            
    def add_op(self, string):
        """
        Add a standard operation in the form of a string to your filename.
        """
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
            self.post_op.append()
        self._update()
            
    def get_dir(self):
        if self.op is not None:
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
        filename = '_'.join(filename_parts)
        if self.get_ext() is not None:
            filename = filename + '.' + self.get_ext()
        return filename
                
    def get_preop(self):
        if self.pre_op is not None:
            return '_'.join(self.pre_op)
        else:
            return None
    
    def get_desc(self):
        if self.desc is not None:
            return '_'.join(self.desc)
        else:
            return None
    
    def get_op(self):
        if self.op is not None:
            return '_'.join(self.op)
        else:
            return None
    
    def get_postop(self):
        if self.post_op is not None:
            return '_'.join(self.post_op)
        else:
            return None
    
    def get_ext(self):
        if self.ext is not None:
            return '_'.join(self.ext)
        else:
            return None
    
        
            
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
                
    
        
        