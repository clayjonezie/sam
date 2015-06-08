import hlp, datetime, random, xlrd, sys

def headings_from(sheet):
    headings = sheet.row(0)
    return [h.value for h in headings]

def values_from_sheet(heading, sheet):
    headings = sheet.row(0)
    col_i = next((i for i, v in enumerate(headings)
                       if v.value == heading), -1)
    if (col_i < 0):
        print "couldn't find heading", heading
        exit()

    vals = [c.value for c in sheet.col(col_i)[1:]]
    return vals

def dates_from_sheet(sheet):
    dates = values_from_sheet("Date", sheet)
    datetimes = [datetime.datetime.strptime(date, "%d-%m-%Y") for date in dates]
    return datetimes

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print "python", sys.argv[0], "<name of file>", "[<name of parameter>]"
        exit()

    filename = sys.argv[1]

    try:
        book = xlrd.open_workbook(filename)
    except IOError:
        print "no file:", filename
        exit()

    sheet = book.sheet_by_index(0) # gets first sheet
    headings = headings_from(sheet) # returns names in first row

    if (len(sys.argv) < 3):
        for heading in headings:
            print '*' + heading + '*'
        exit()
    else:
        parameter = sys.argv[2]
        if parameter not in headings:
            print "parameter not in sheet", parameter
            exit()

    dates = dates_from_sheet(sheet)
    print dates
    vals = values_from_sheet(parameter, sheet)
    print vals
    if (len(dates) != len(vals)):
        print "bad dimensions of date and vals"
        exit()
    else:
        hlp.plot_number_by_time(vals, dates, parameter, "", "fooo.png")
