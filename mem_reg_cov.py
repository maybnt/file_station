import re
pattern = r"//Trans .{1,2} Byte .:"
i=0
with open('source/imx258_rom_lmmi_data.mem','r',encoding='utf-8') as mem_file,\
     open('source/iic_cfg_mem.txt','w',encoding='utf-8') as write_file:
    for line in mem_file:
        match=re.search(pattern,line.rstrip())
        if match:
            i=i+1
            write_file.write(line[-5:])
            print(line.rstrip()[-4:],i)