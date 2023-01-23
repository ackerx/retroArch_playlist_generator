#coding:utf-8
import os
import json

#目录结构是这样的
#  $TOP_PATH / fc / roms...
#  $TOP_PATH / gba / roms...
#switch里rom的目录，建议就放在 /rom/ 下

def main():
    #rom所在的顶级目录
    rom_top_path = "H:/game/retroArch/test/"

    #switch sd卡里rom的顶级目录
    switch_top_path = "/rom/"

    #你需要先修改上述目录
    if rom_top_path == "H:/game/retroArch/test/":
        print("你修改rom所在顶层目录了吗？")
        exit(0)

    directorys = os.listdir(rom_top_path)
    platform_list = []

    for platform in directorys:
        #print(file)
        if os.path.isdir(rom_top_path+platform) == False:
            continue

        print(f'found platform {platform}')
        counter = 0
        playlist = {
            "version" : "1.0",
            "items" : []
        }

        path = rom_top_path + platform
        roms = os.listdir(path)
        for rom in roms:
            suffix = rom.split(".")[-1]
            counter = counter + 1

            rom_new_name = "%s_%03d.%s" % (platform, counter, suffix)

            #print(platform, rom, rom_new_name)
            tmp = {
                "path" : switch_top_path+platform+"/"+rom_new_name,
                "label" : rom,
                "core_path" : "DETECT",
                "core_name" : "DETECT",
                "crc32": "DETECT",
                "db_name": platform+".lpl"
            }
            playlist["items"].append(tmp);
            print("rename", path+"/"+rom, path+"/"+rom_new_name)

            #如果需要重命名文件，注释这句话
            #os.rename(path+"/"+rom, path+"/"+rom_new_name)

        #print(playlist)
        lplfile_name = platform+".lpl"
        lplfile_path = rom_top_path + "/" + lplfile_name
        lplfile = open(lplfile_path, "w")
        print(f"write lpl file {lplfile_path}")
        json.dump(playlist, lplfile, indent = 4)

if __name__ == '__main__':
    print("Switch RetroArch Playlist Generator")
    main()