import os

def edit_file(file_path, new_content, line_number):
    with open(file_path, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        lines[line_number-1] = new_content
        f.writelines(lines)

def restart_gnome_shell():
    inpoot = input("Restart gnome shell? [Y/n] ")
    # create a default answer of yes
    if inpoot == "":
        inpoot = "y"
    if inpoot.lower() == "y":
        try:
            os.system("killall -3 gnome-shell")
        except:
            print("Unable to restart GNOME shell, please restart manually.")
            exit()
    else:
        print("Exiting...")
        # kill the script
        exit()




def main():
    file_path = r"/usr/share/gnome-shell/extensions/pop-shell@system76.com/launcher.js"
    # Used for formatting
    spaces = " " * 20
    new_content = spaces + "ext.overlay.visible = false;\n"
    line_number = 49
    try:
        edit_file(file_path, new_content, line_number)
    except Exception as e:
        print(e)
        print("There was an error whilst trying to edit the file.")
        print("Please check that the file at {0} is not read-only.".format(file_path))
        print("Also check that you are running this script as sudo.")
    restart_gnome_shell()

if __name__ == "__main__":
    main()

