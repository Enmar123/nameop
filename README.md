# nameop
Make naming files easy.

Ever found yourself in a situation where you are generating a lots of files but have no way to uniquely name them?
Introducing nameop!

#### Concept
Somewhere in your methods just insert the easy to remmeber `add_op()` function to add an operation to your filename. When it comes time to save your file just use the `self.path` variable and it will be automatically saved with the filename that includes all operations you performed on the file! If you need titles for graphs just use the `self.desc` variable, which strips directory and file extension info, leaving only the descripptive information.

### Examples
If you want an example of how this package can be used take a look at the `examples.py`file. 
