# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:15:39 2019

@author: Jason
"""

class nameop:
    """
    This class serves as a container. Use it to store operation descriptors
    and build your file name. 
    
    Variables:
        self.dir     = directory
        self.name    = original file descriptor
        self.pre_op  = pre operations
        self.op      = operations
        self.post_op = post operations
        self.ext     = file extension
    
    Format: 
        <self.dir><self.name><self.pre_op><self.op><self.post_op><self.ext>
    """
    
    def __init__(self, filepath=None):
        self.dir = None
        self.name = None
        self.pre_op = None
        self.op = None
        self.post_op = None
        self.ext = None
        
        self._driver(filepath)
        
    def __getitem__(self, item):
        return #'TODO'
    
    def __repr__(self):
        if self.name is None:
            self.name = repr(None)
        filename =  self.name
        if self.dir is not None:
            filename = '/'.join([self.dir, filename])
        if self.pre_op is not None:
            filename = '_'.join([filename, self.pre_op])
        if self.op is not None:
            filename = '_'.join([filename, self.op])
        if self.post_op is not None:
            filename = '_'.join([filename, self.post_op])
        if self.ext is not None:
            filename = '.'.join([filename, self.ext])
        return filename
    
    def _driver(self, filepath):
        # <TODO>
        # add support for missing directory
        # add case for missing file extension
        if filepath is None:
            return
        elif isinstance(filepath, str):
            self.dir = '/'.join(filepath.split('/')[0:-1])
            self.name = filepath.split('/')[-1].split('.')[0]
            self.ext = filepath.split('.')[-1]
        else:
            raise ValueError('Input is not string')
            
    def add_op(self, string):
        """
        Add a standard operation in the form of a string to your filename.
        """
        if self.op is None:
            self.op = string
        else:
            ops = self.op.split('_')
            ops.append(string)
            '_'.join(ops)
    
    def add_post(self, string):
        """
        Add a post operation in the form of a string to your filename.
        """
        if self.post_op is None:
            self.post_op = string
        else:
            ops = self.op.split('_')
            ops.append(string)
            '_'.join(ops)