import xlwt
import os

def save_to_execl(data,name,head):
    try:
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.bold=True
        style.font = font

        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet(name)
        for h in range(len(head)):
            sheet.write(0, h, head[h],style)

        i = 1
        for obj in data:
            j = 0
            for v in (obj.values()):
                sheet.write(i, j, v)
                j += 1
            i += 1
        workbook.save('%s\execl\\%s.xls' % (os.getcwd(),name))
        print('写入excel成功')
    except Exception:
        print('写入execl失败')

def my_print(v):
    print(v)