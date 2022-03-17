#入力された西暦を和暦に変換する。

int_input = int(input("西暦を入力してください。\n"))

#飛鳥時代(大化)
if(int_input >=645 and int_input <=649):
    str_nengo = '大化'
    int_year = int_input - 644
    if(int_year ==1):
        print("西暦", int_input, "年は",str_nengo, int_year,"年です。\n",sep='' )
    else:
        print("西暦",int_input,"年は", str_nengo, int_year, "年です。", sep='')

#飛鳥時代(白雉)
#明治
if(int_input >= 1868 and int_input <= 1911):
    str_nengo = "明治"
    int_year = int_input -1867
    if(int_year == 1):
        int_lastYear = int_input - 1864
        str_lastYear = "慶応"
        print("西暦", int_input, "年は", str_nengo,"元年(", str_lastYear, int_lastYear,"年)です。\n", sep='')
    else:
        print("西暦",int_input, "年は", str_nengo, int_year, "年です。\n", sep='')

#大正
elif(int_input >= 1912 and int_input <=1925):
    str_nengo = "大正"
    int_year = int_input -1911
    if(int_year==1):
        iint_lastYear = int_input -1867
        str_lastYeat = '明治'
        print("西暦", int_input, "年は", str_nengo, "元年(", str_lastYear, int_lastYear,"年)です。\n", sep='')
    else:
        print("西暦", int_input,"年は", str_nengo,int_year, "年です。\n", sep='')

#昭和
elif(int_input >= 1926 and int_input <= 1988):
    str_nengo = "昭和"
    int_year = int_input - 1925
    if(int_year == 1):
        int_lastYear = int_input - 1911
        str_lastYear = "大正"
        print("西暦", int_input,"年は", str_nengo, "元年(", str_lastYear, int_lastYear, "年)です。\n", sep='' )
    else:
        print("西暦", int_input, "年は", str_nengo, int_year, "年です。\n", sep='')

#平成
elif(int_input >= 1989 and int_input <= 2018):
    str_nengo = "平成"
    int_year = int_input - 1988
    if(int_year == 1):
        intlastYear = int_input -1925
        str_lastYear = "昭和"
        print("西暦", int_input, "年は", str_nengo, "元年は(", str_lastYear, int_lastYear, "年)です。\n", sep='')
    else:
        print("西暦", int_input, "年は", str_nengo, int_year, "年です。\n", sep='')

#令和
elif(int_input >= 2019):
    str_nengo = "令和"
    int_year = int_input - 2018
    if(int_year == 1):
        int_lastYear = int_input - 1988
        str_lastYear = "平成"
        print("西暦", int_input, "年は", str_nengo, "元年は(", str_lastYear, int_lastYear, "年)です。\n", sep='')
    else:
        print("西暦", int_input, "年は", str_nengo, int_year, "年です。\n", sep='')

else:
    print("西暦", int_input, "年は、かなり古い時代です。\n", sep='')