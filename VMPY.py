import easygui
from tkinter import filedialog

def vm():
    dangerous = ["os.","subprocess.","shutil.","pickle.","eval(","exec(","compile(","execfile.","ctypes.","multiprocessing.","socket.","tempfile.mktemp"]
    file_path = filedialog.askopenfilename(title="Select a File for your Virtual Machine", filetypes=[("Text Files", "*.vmpy")])
    file = open(str(file_path), "r")
    file = file.readlines()
    for i in range(len(file)):
        for j in range(len(dangerous)):
            if dangerous[j] in file[i]:
                file[i] = "REMOVEDLINE"
            else:
                pass
    for i in range(file.count("REMOVEDLINE")):
        file.remove("REMOVEDLINE")

    exec("".join(file), globals(), locals())

option = easygui.buttonbox('Pick an option! VM.PY is a free Python virtual machine. This program was made by SeafoodStudios.', 'VM.PY', ('Learn More About VM.PY', 'Upload VM.PY File'))

if option == "Learn More About VM.PY":
    easygui.msgbox("PY.VM is a Python virtual machine.\nThis is just a fun experiment, and this has no real use.\nTo program VM.PY programs, make your Python file ending '.vmpy'.","Learn More")
elif option == "Upload VM.PY File":
    vm()
else:
    pass
