import csv
import pandas as pd

Netflix_title = pd.read_csv('Netflix_title.csv', encoding='utf-8')
Netflix_history = pd.read_csv('NetflixViewingHistory.csv', encoding='utf-8')

# 두 csv에서 title만 가져오기
title = Netflix_title.iloc[:,[0]]
hist = Netflix_history.iloc[:,[0]]

# dataframe -> list
title = title.values.tolist()
hist = hist.values.tolist()
# print(title)
viewcount = []
for temp_t in title:
    counter = 0
    for temp_h in hist:
        if temp_t == temp_h:
            print(temp_t)
            counter += 1 
        else:
            counter += 0
    viewcount.append(counter)

# list -> dataframe
title = pd.DataFrame(title)
viewcount = pd.DataFrame(viewcount)

# title 파일에 history 칼럼을 추가, 열에 viewcount를 추가
title['history'] = viewcount
# csv파일 생성
title.to_csv(f'Netflix_t_h.csv', mode='w', encoding='utf-8-sig', header=True, index=False)





"""
Netflix_title = open('Netflix_title.csv','r', encoding='utf-8-sig')
Netflix_title_r = csv.reader(Netflix_title)
t_header = next(Netflix_title_r)

Netflix_history = open('NetflixViewingHistory.csv','r', encoding='utf-8-sig')
Netflix_history_r = csv.reader(Netflix_history)
h_header = next(Netflix_history_r)

history_t = []
history_h = []
history_num_t = 0
history_num_h = 0

for t_row in Netflix_title_r:
    history_t.append(t_row)
    history_num_t = history_num_t + 1
print(history_num_t)

for h_row in Netflix_history_r:
    history_h.append(h_row)
    history_num_h = history_num_h + 1
print(history_num_h)

for i in range(history_num_t):
    for j in range(history_num_h):
        if history_t[i][0] == history_h[j][0]:
            history_t[i][2] = int(history_t[i][2]) + 1     # history 부분 수정
            print(history_t[i])

Netflix_title.close()
Netflix_history.close()

Netflix_t_h = open('Netflix_t_h.csv','w', encoding='utf-8-sig')
writer = csv.writer(Netflix_t_h)
writer.writerow(t_header)
for t_h in history_t:
    # print(t_h[0])
    # print(t_h[1])
    # print(t_h[2])
    data = [t_h[0],t_h[1],t_h[2]]
    writer.writerow(data)
Netflix_t_h.close()
"""