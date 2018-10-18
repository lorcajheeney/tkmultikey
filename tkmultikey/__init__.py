"""
tkmultikey is a python library intended to make the process of binding actions to key combinations easier in tkinter.
tkmultikey redefines tkinter's core binding functions to allow commands to be bound to key strokes such as "<Ctrl>+<Left>".
Example Usage:
---------------------
import tkinter
import tkmultikey

window = tkinter.Tk()
tkmultikey.config(window)

def say_hello():
    print("Hi user!")
window.bind("h+i",say_hello)

while True:
    window.update()
---------------------
The above program will then print out its greeting message when both 'h' and 'i' keys are pressed.
For more information please visit www.github.com/lorcajheeney/tkmultikey to see example usage and installtion instructions.
"""
import types
def config(widget):
    """Configurates the widget argument to add properties and override methods allowing additional functionality to be built into it."""
    widget.keyhistory = [
    widget.activekeys = {}
    def __handle_key_press(event):
        """Private function which handles tkinter key presses by adding them onto queue."""
        if not (event.keysym in widget.keyhistory):
            widget.keyhistory.append(event.keysym)
    def __handle_key_release(event):
        """Private function which handles tkinter key releases by removing the key press from the queue."""
        if (event.keysym in widget.keyhistory):
            widget.keyhistory.pop(widget.keyhistory.index(event.keysym))
    widget.bind("<KeyPress>",__handle_key_press)
    widget.bind("<KeyRelease>",__handle_key_release)
    def __handle_add_keys(self,keysequence, action):
        """Private function which overrides widget's bind function, handles the user adding key binds by adding them onto an active keys structure."""
        keys = list(keysequence.split("+"))
        widget.activekeys[action] = keys
    widget.bind = types.MethodType(__handle_add_keys,widget)
    windowupdate = widget.update
    def __handle_win_update(self):
        """Private function which overrides widget's update function, checks to see if any matching key presses then runs standard update function."""
        for action, keys in widget.activekeys.items():
            if all([(key in widget.keyhistory) for key in keys]) and len(widget.keyhistory) > 0:
                print(widget.keyhistory,widget.activekeys)
                try:
                    action(keys)
                except TypeError: action()
        windowupdate()
    widget.update = types.MethodType(__handle_win_update, widget)
        