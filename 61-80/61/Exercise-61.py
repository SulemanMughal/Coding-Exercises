def century(year):
    century_no = str((year + 99 ) // 100)
    return '21st century' if century_no == '21' else century_no + 'the century'