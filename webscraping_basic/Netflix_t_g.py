import csv
import pandas as pd
f_name = ['Netflix_genre_kr.csv','Netflix_genre_usa.csv','Netflix_genre_os.csv','Netflix_genre_awd.csv',
'Netflix_genre_inde.csv','Netflix_genre_chil.csv','Netflix_genre_ani.csv','Netflix_genre_act.csv',
'Netflix_genre_cmd.csv','Netflix_genre_rmc.csv','Netflix_genre_thril.csv','Netflix_genre_horr.csv',
'Netflix_genre_sf.csv','Netflix_genre_fant.csv','Netflix_genre_dram.csv','Netflix_genre_crim.csv',
'Netflix_genre_docu.csv','Netflix_genre_music.csv','Netflix_genre_clasc.csv','Netflix_genre_shorts.csv']

def Csv2list(filename):
    genre_f = open(filename, 'r', encoding='utf-8-sig')
    g_reader = csv.reader(genre_f)
    g_name = next(g_reader)

    g_num = 0   # 헤더를 제외한 타이틀 갯수
    g_list = []
    for movie in g_reader:
        if len(movie) < 1 : continue
        else:
            g_list.append(movie)
            g_num += 1
    genre_f.close()
    return g_name, g_list, g_num

def Add_g(t_list, tem_list, t_num, tem_num, tem_name):
    temp_o = []
    fead = []
    g_add = False
    for i in range(t_num):
        for j in range(tem_num):
            if t_list[i][0] == tem_list[j][0]:
                g_add = True
                temp_o.append(i)
                # fead.append(t_list[i])
                fead.append(tem_name)
        if g_add == False:
            fead.append(" ")
        else : g_add = False
    return temp_o, fead


t_name, t_list, t_num = Csv2list('Netflix_t_h.csv')
df_t_list = pd.DataFrame(t_list)
for i in range(20):
    tem_name, tem_list, tem_num = Csv2list(f_name[i])
    temp, fead = Add_g(t_list,tem_list,t_num,tem_num,tem_name)
    
    df_fead = pd.DataFrame(fead)
    # df_fead.transpose()
    # df_fead.T
    df_t_list = pd.concat([df_t_list,df_fead], axis=1)

print(df_t_list)
df_t_list.to_csv("test.csv", encoding="utf-8-sig", header=False)


# print(Add_g(t_list,tem_list,t_num,tem_num,tem_name))
# temp_o = Add_g(t_list,tem_list,t_num,tem_num,tem_name)

# f = open("test.csv",'w',encoding='utf-8-sig')
# writer = csv.writer(f)
# for i in df_fead:
#     writer.writerow(i)
# f.close()

# f = open("test.csv",'w',encoding='utf-8-sig')
# writer = csv.writer(f)
# for test in t_list:
#     data = [test]
#     writer.writerow(data)

                


# Netflix_title = open('Netflix_title.csv','r', encoding='utf-8-sig')
# Netflix_title_r = csv.reader(Netflix_title)
# t_header = next(Netflix_title_r)

# Netflix_history = open('NetflixViewingHistory.csv','r', encoding='utf-8-sig')
# Netflix_history_r = csv.reader(Netflix_history)
# h_header = next(Netflix_history_r)

# history_t = []
# history_h = []
# history_num_t = 0
# history_num_h = 0

# for t_row in Netflix_title_r:
#     history_t.append(t_row)
#     history_num_t = history_num_t + 1
# print(history_num_t)

# for h_row in Netflix_history_r:
#     history_h.append(h_row)
#     history_num_h = history_num_h + 1
# print(history_num_h)

# for i in range(history_num_t):
#     for j in range(history_num_h):
#         if history_t[i][0] == history_h[j][0]:
#             history_t[i][2] = int(history_t[i][2]) + 1     # history 부분 수정
#             print(history_t[i])

# Netflix_title.close()
# Netflix_history.close()

# Netflix_t_h = open('Netflix_t_h.csv','w', encoding='utf-8-sig')
# writer = csv.writer(Netflix_t_h)
# writer.writerow(t_header)
# for t_h in history_t:
#     writer.writerow(t_h)
# Netflix_t_h.close()