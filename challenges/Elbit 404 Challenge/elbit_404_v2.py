#%%
import colorama
colorama.init()

def gotoxy(c, x,y):
    print("\033[%d;%dH%s" % (y,x,c))
    # print ("%c[%d;%df" % (0x1B, y, x), end='')

#%%
fn = r"elbitsystems_modified.elbit"
with open(fn, "rb") as f:
    data = f.read()


op_gotox = int("0x3f", 16)
op_gotoy = int("0x40", 16)
op_print = int("0x24", 16) 
sop_space = int("0x00", 16)
sop_comma = int("0x01", 16)

characters = {0:' ', 1:',', 2:'%', 4:',', 16:"#", 32:"(", 64:"/", 128:'*'}


#%% Validate
x = None
y = None
for i in range(0, len(data), 2):
    if data[i]==op_gotox:
        x = data[i+1]
    elif data[i]==op_gotoy:
        y = data[i+1]
    elif data[i]==op_print:
        ci = data[i+1]
        if ci not in characters:
            print(f"Position {i+1} : invalid character")
            break
        c = characters[ci]
    else:
        print(f"Position {i} : invalid opcode")
        break

#%% Print
x = None
y = None
for i in range(0, len(data), 2):
    if data[i]==op_gotox:
        x = data[i+1]
    elif data[i]==op_gotoy:
        y = data[i+1]
    elif data[i]==op_print:
        ci = data[i+1]
        c = characters[ci]
        gotoxy(c, x, y)
        # print(c)

#%% plot
# x = None
# y = None
# import matplotlib.pyplot as plt
# plt.figure()
# for i in range(0, len(data), 2):
#     if data[i]==op_gotox:
#         x = data[i+1]
#     elif data[i]==op_gotoy:
#         y = data[i+1]
#     elif data[i]==op_print:
#         if data[i+1]==sop_comma:
#             plt.text(x,y,",")
# plt.xlim((0,200))
# plt.ylim((0,65))
# plt.gca().invert_yaxis()
# plt.show()

# # #%% Numpy
# x = None
# y = None
# import numpy as np
# text = np.zeros((65,200), 'U1')
# for i in range(0, len(data), 2):
#     if data[i]==op_gotox:
#         x = data[i+1]
#     elif data[i]==op_gotoy:
#         y = data[i+1]
#     elif data[i]==op_print:
#         c = " " if data[i+1]==sop_space else ","
#         text[y][x] = c

# for row in text:
#     print("")
#     for c in row:
#         if c=="":
#             print(" ", end="")
#         elif c==" ":
#             print("X", end="")
#         elif c==",":
#             print(",", end="")