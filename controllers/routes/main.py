from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    at.bar1.custom.data = [{"x":2010, "category1":40, "category2":50}, 
                           {"x":2011, "category1":30, "category2":60}]
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    at.Dropdown1.custom.values = ['Apple', 'Banana', 'Orange', 'Papaya']
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    at.Dropdown1.custom.selectedValue = 'Apple'
    pass


def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    if at.upload1.onChange:
        # sanity check if user has successfully uploaded a file
        if at.upload1.io.files != None:
            files = at.upload1.io.files
            # check if user has uploaded one or more files
            if len(files) > 0:
                # grab the first file
                # Note: files[0].file is a starlette.UploadFile object
                # It has some information like content_type that can be used
                # to identify the type of file.
                uploadFile = files[0]
                # get the python's BinaryIO file from starlette.UploadFile
                binaryFile = uploadFile.file
                # read the bytes in file
                data = files.read()
                # optional - convert bytes into utf-8 format
                data_utf8 = data.decode()
            """for i, uploadFile in enumerate(files):
                # get the python's BinaryIO file from starlette.UploadFile
                binaryFile = uploadFile.file
                # read the bytes in file
                data = binaryFile.read()
                # optional - convert bytes into utf-8 format
                data_utf8 = data.decode()"""
    pass