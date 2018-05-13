# encoding: utf-8

import xlrd


class ExcelUtil(object):
    def __init__(self, excel_path, sheet_name='Sheet1'):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print('没有数据获取！')
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行开始取对于values的值
                s['rowNum'] = i + 2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r



if __name__ == '__main__':
    filepath = 'D:\\test\\testcase.xlsx'
    sheetName = 'Sheet1'
    data = ExcelUtil(filepath, sheetName)
    print(data.rowNum)
    print(data.colNum)
    print(data.dict_data())

