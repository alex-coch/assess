def m_get(i_item, i_list):
    k = 0
    for ii in m_list:
        if i_item[2] == ii[0]:
            k = 1
            if ii[2] not in i_list:
                m_get(i[:4]+str(int(int(float(i[4:]))*int(float(i_item[4:]))/100)), i_list+i_item[2])
            else:
                for k in m_list:
                    if ii[0] == k[0]:
                        for ij in m_list_end:
                            if k[2] == ij[2]:
                                m_list_end.pop()
                break
    if k == 0:
        m_list_end.append('a' + item[1:])


m_list_end = []
with open('sample\\in_17.txt') as file:
    m_list = []
    for line in file.readlines():
        m_list.append(line.strip())

for item in m_list:
    if item[0] == 'a':
        m_get(item, item[2])

summa = 0
for i in m_list_end:
    summa += int(i[4:])
if summa < 100:
    m_list_end.append('a ? ' + str(100 - summa))
for i in range(len(m_list_end) - 1):
    for j in range(i + 1, len(m_list_end)):
        if m_list_end[i][2] == m_list_end[j][2]:
            m_list_end[i] = m_list_end[i][:4] + str(int(m_list_end[i][4:]) + int(m_list_end[j][4:]))
            m_list_end[j] = m_list_end[j][:2] + '.' + m_list_end[j][3:]
for c, i in enumerate(m_list_end):
    if i[2] == '.':
        m_list_end.pop(c)

for i in m_list_end:
    print(i)
