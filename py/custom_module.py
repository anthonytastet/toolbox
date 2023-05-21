def get_filePermissions(file):
    from os import access, stat, F_OK

    file_exists = access(file, F_OK)
    f_e = ""
    u_r = ""
    u_w = ""
    u_x = ""
    g_r = ""
    g_w = ""
    g_x = ""
    o_r = ""
    o_w = ""
    o_x = ""

    permission_mask = str(oct(stat(file).st_mode)[-3:])

    if file_exists == True:
        f_e = "-"

        # user
        if permission_mask[0] == "0":
            u_r = "-"
            u_w = "-"
            u_x = "-"
        if permission_mask[0] == "1":
            u_r = "-"
            u_w = "-"
            u_x = "x"
        if permission_mask[0] == "2":
            u_r = "-"
            u_w = "w"
            u_x = "-"
        if permission_mask[0] == "3":
            u_r = "-"
            u_w = "w"
            u_x = "x"
        if permission_mask[0] == "4":
            u_r = "r"
            u_w = "-"
            u_x = "-"
        if permission_mask[0] == "5":
            u_r = "r"
            u_w = "-"
            u_x = "x"
        if permission_mask[0] == "6":
            u_r = "r"
            u_w = "w"
            u_x = "-"
        if permission_mask[0] == "7":
            u_r = "r"
            u_w = "w"
            u_x = "x"

        # group
        if permission_mask[1] == "0":
            g_r = "-"
            g_w = "-"
            g_x = "-"
        if permission_mask[1] == "1":
            g_r = "-"
            g_w = "-"
            g_x = "x"
        if permission_mask[1] == "2":
            g_r = "-"
            g_w = "w"
            g_x = "-"
        if permission_mask[1] == "3":
            g_r = "-"
            g_w = "w"
            g_x = "x"
        if permission_mask[1] == "4":
            g_r = "r"
            g_w = "-"
            g_x = "-"
        if permission_mask[1] == "5":
            g_r = "r"
            g_w = "-"
            g_x = "x"
        if permission_mask[1] == "6":
            g_r = "r"
            g_w = "w"
            g_x = "-"
        if permission_mask[1] == "7":
            g_r = "r"
            g_w = "w"
            g_x = "x"

        # others
        if permission_mask[2] == "0":
            o_r = "-"
            o_w = "-"
            o_x = "-"
        if permission_mask[2] == "1":
            o_r = "-"
            o_w = "-"
            o_x = "x"
        if permission_mask[2] == "2":
            o_r = "-"
            o_w = "w"
            o_x = "-"
        if permission_mask[2] == "3":
            o_r = "-"
            o_w = "w"
            o_x = "x"
        if permission_mask[2] == "4":
            o_r = "r"
            o_w = "-"
            o_x = "-"
        if permission_mask[2] == "5":
            o_r = "r"
            o_w = "-"
            o_x = "x"
        if permission_mask[2] == "6":
            o_r = "r"
            o_w = "w"
            o_x = "-"
        if permission_mask[2] == "7":
            o_r = "r"
            o_w = "w"
            o_x = "x"

    permission_mask_humanreadable = f"{f_e}{u_r}{u_w}{u_x}{g_r}{g_w}{g_x}{o_r}{o_w}{o_x}"
    # print("permission mask: ", permission_mask_humanreadable)
    return permission_mask_humanreadable

def get_currentLocation():
    from os import curdir
    return curdir

def get_childItems(location: str):
    from os import listdir
    return listdir(location)

def get_fileBaseName(file: str):
    from os import path
    file_fullName = file
    file_baseName = str(path.splitext(file_fullName)[0]).split("/")[-1]
    # print(f"file base name: {file_baseName}")
    return file_baseName

def get_fileExtension(file: str):
    file_extension = ""
    extension_exists = "." in file
    if(extension_exists):
        file_extension = file.split(".")[-1]
    else:
        file_extension = "no-extension"
    return file_extension

def clean_fileName(file_name: str, word_separator: str):
    file_extension = get_fileExtension(file_name)

    # should_useUnderscores = ("py", "js")
    # if file_extension in should_useUnderscores:
    #     word_separator = "_"
    # else:
    #     word_separator = "-"

    file_name = file_name.strip()
    file_name.lstrip("-_,")
    file_name = file_name.lower()
    file_name = file_name.replace(" ", word_separator)
    file_name = file_name.replace("-", word_separator)
    file_name = file_name.replace("_", word_separator)
    file_name = file_name.replace("'", word_separator)
    file_name = file_name.replace("-", word_separator)
    file_name = file_name.replace(",", word_separator)
    file_name = file_name.replace("é", "e")
    file_name = file_name.replace("è", "e")
    file_name = file_name.replace("ê", "e")
    file_name = file_name.replace("à", "a")
    file_name = file_name.replace("â", "a")

    return file_name
