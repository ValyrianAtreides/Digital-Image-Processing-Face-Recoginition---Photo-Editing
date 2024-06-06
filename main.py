from tkinter import Tk
from interface import PhotoEditorInterface
from photo_editor import PhotoEditor

window = Tk()
photo_editor = PhotoEditor()
interface = PhotoEditorInterface(window, photo_editor)
photo_editor.interface = interface
window.mainloop()
