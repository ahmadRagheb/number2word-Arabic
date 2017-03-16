# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import locale

class number2word(object):






    def __init__(self, number):
        self.number = number


    def validate(self):
        returnmsg=""
        # // convert number into array of(string) number each case
        # // -------number: 121210002876 - ---------- //
        # //   0          1          2          3 //
        # // '121'      '210'      '002'      '876'

        #to format number like 10012 became 100,12
        my_number=self.number
        english_format_number=self.convert_number(my_number)
        #we split it into array
        array_number= english_format_number.split(',')
        #array_number is type of list
            # frappe.throw(array_number)
        #convert each number(hundred) to arabic
        for i in xrange(len(array_number)):
            place=len(array_number)-i
            returnmsg=returnmsg+self.convert(array_number[i], place)
            # if (array_number[i+1]) and (array_number[i+1] > 0):
            if (0 <= i) and (i < len(array_number)-1):
                returnmsg= returnmsg+' و '
        print(returnmsg)

    def convert_number(self,number):
        locale.setlocale(locale.LC_ALL, '')
        x = self.number
        x= int(float(x))
        x1 = locale.format("%d", x, grouping=True)
        # frappe.throw(type(x).__name__)
        if (x < 0 or x > 999999999999):
            print ("العدد خارج النطاق")
        else:
             return x1

    def convert(self,number, place):
        # take in charge the sex of NUMBERED
        #  sex =self.sex
        returnmsg=""

        sex = 'male'
        # // the number word in arabic for masculine and feminine

        # words = list[{'male':list[{
			# 	'0': '' ,'1': 'واحد' ,'2': 'اثنان' ,'3' : 'ثلاثة','4' : 'أربعة','5' : 'خمسة',
			# 	'6' : 'ستة','7' : 'سبعة','8' : 'ثمانية','9' : 'تسعة','10' : 'عشرة',
			# 	'11' : 'أحد عشر','12' : 'اثنا عشر','13' : 'ثلاثة عشر','14' : 'أربعة عشر','15' : 'خمسة عشر',
			# 	'16' : 'ستة عشر','17' : 'سبعة عشر','18' : 'ثمانية عشر','19' : 'تسعة عشر','20' : 'عشرون',
			# 	'30' : 'ثلاثون','40' : 'أربعون','50' : 'خمسون','60' : 'ستون','70' : 'سبعون',
			# 	'80' : 'ثمانون','90' : 'تسعون', '100':'مئة', '200':'مئتان', '300':'ثلاثمئة', '400':'أربعمئة', '500':'خمسمئة',
			# 	'600':'ستمئة', '700':'سبعمئة', '800':'ثمانمئة', '900':'تسعمئة'}],
			# 'female':list[{
			# 	'0': '' ,'1': 'واحدة' ,'2': 'اثنتان' ,'3' : 'ثلاث','4' : 'أربع','5' : 'خمس',
			# 	'6' : 'ست','7' : 'سبع','8' : 'ثمان','9' : 'تسع','10' : 'عشر',
			# 	'11' : 'إحدى عشرة','12' : 'ثنتا عشرة','13' : 'ثلاث عشرة','14' : 'أربع عشرة','15' : 'خمس عشرة',
			# 	'16' : 'ست عشرة','17' : 'سبع عشرة','18' : 'ثمان عشرة','19' : 'تسع عشرة','20' : 'عشرون',
			# 	'30' : 'ثلاثون','40' : 'أربعون','50' : 'خمسون','60' : 'ستون','70' : 'سبعون',
			# 	'80' : 'ثمانون','90' : 'تسعون', '100':'مئة', '200':'مئتان', '300':'ثلاثمئة', '400':'أربعمئة', '500':'خمسمئة',
			# 	'600':'ستمئة', '700':'سبعمئة', '800':'ثمانمئة', '900':'تسعمئة'
        #     }]
        #               }]
        words = {
            'male': {
                '0': '', '1': 'واحد', '2': 'اثنان', '3': 'ثلاثة', '4': 'أربعة', '5': 'خمسة',
                '6': 'ستة', '7': 'سبعة', '8': 'ثمانية', '9': 'تسعة', '10': 'عشرة',
                '11': 'أحد عشر', '12': 'اثنا عشر', '13': 'ثلاثة عشر', '14': 'أربعة عشر', '15': 'خمسة عشر',
                '16': 'ستة عشر', '17': 'سبعة عشر', '18': 'ثمانية عشر', '19': 'تسعة عشر', '20': 'عشرون',
                '30': 'ثلاثون', '40': 'أربعون', '50': 'خمسون', '60': 'ستون', '70': 'سبعون',
                '80': 'ثمانون', '90': 'تسعون', '100': 'مئة', '200': 'مئتان', '300': 'ثلاثمئة', '400': 'أربعمئة',
                '500': 'خمسمئة',
                '600': 'ستمئة', '700': 'سبعمئة', '800': 'ثمانمئة', '900': 'تسعمئة'},
            'female': {
                '0': '', '1': 'واحدة', '2': 'اثنتان', '3': 'ثلاث', '4': 'أربع', '5': 'خمس',
                '6': 'ست', '7': 'سبع', '8': 'ثمان', '9': 'تسع', '10': 'عشر',
                '11': 'إحدى عشرة', '12': 'ثنتا عشرة', '13': 'ثلاث عشرة', '14': 'أربع عشرة', '15': 'خمس عشرة',
                '16': 'ست عشرة', '17': 'سبع عشرة', '18': 'ثمان عشرة', '19': 'تسع عشرة', '20': 'عشرون',
                '30': 'ثلاثون', '40': 'أربعون', '50': 'خمسون', '60': 'ستون', '70': 'سبعون',
                '80': 'ثمانون', '90': 'تسعون', '100': 'مئة', '200': 'مئتان', '300': 'ثلاثمئة', '400': 'أربعمئة',
                '500': 'خمسمئة',
                '600': 'ستمئة', '700': 'سبعمئة', '800': 'ثمانمئة', '900': 'تسعمئة'
            }
        }
        #	//take in charge the different way of writing the thousands and millions ...
        # mil = list[
        #     '2' : list['1' : 'ألف', '2' : 'ألفان', '3' : 'آلاف'],
        #     '3' : list['1' : 'مليون', '2' : 'مليونان', '3' : 'ملايين'],
        #     '4' : list['1' : 'مليار', '2' : 'ملياران', '3' : 'مليارات'] ]


        mf = {'1' : 'male', '2' : 'male', '3' : 'male', '4' : 'male'}
        number_length = len(str(number))

        #we are dealing with 3 digits number in each loop the main method calls convert methode
        #and pass a string with tree digit in it ... for example 123 or 19 or 3 ..



        # we will clean left zero for example 001 will be 1 ,,
        # 012 will be 12


        if (int(number) == 0):
            return ''
        elif number[0] == 0:
            if number[1] == 0:
                number=int(number[:-1])
                return number
            else:
                number=int(number[:-2])
                return number


        #switching number length
        #if number have on digits like "1"
        returnmsg = ""
        number=str(number)
        if(number_length == 1):
            # number=number+'one'
            if (place==1):
                returnmsg = returnmsg+ words[mf[str(place)]][number]
            if (place==2):
                if (int(number) == 1):
                    returnmsg =u' ألف'
                elif (int(number) == 2):
                    returnmsg=u' ألفان'
                else:
                    returnmsg = returnmsg + words[mf[str(place)]][number]+u' آلاف'
            if (place==3):
                if (int(number) == 1):
                    returnmsg =returnmsg +u' مليون'
                elif (int(number) == 2):
                    returnmsg=returnmsg+u' مليونان'
                else:
                    returnmsg = returnmsg + words[mf[str(place)]][number]+u' ملايين'
            if (place==4):
                if (int(number) == 1):
                    returnmsg =returnmsg +u' مليار'
                elif (int(number) == 2):
                    returnmsg=returnmsg+u' ملياران'
                else:
                    returnmsg = returnmsg + words[mf[str(place)]][number]+u' مليارات'


        elif(number_length == 2):
            # number=number+'two'

            # if (words[mf[str(place)]][number]):
            if (words[mf[str(place)]].has_key(number)):
                returnmsg = returnmsg + words[mf[str(place)]][number]
            else:
                twoy=int(number[0]) * 10
                ony=number[1]
                returnmsg = returnmsg + words[mf[str(place)]][ony]+' و'+words[mf[str(place)]][str(twoy)]

            if (place==2):
                    returnmsg =returnmsg +u' ألف'
            if (place==3):
                    returnmsg =returnmsg +u' مليون'
            if (place==4):
                    returnmsg =returnmsg +u' مليار'







        elif(number_length== 3):
            # number=number+'three'
            # if (words[mf[str(place)]][number]):
            if (words[mf[str(place)]].has_key(str(number))):
                returnmsg = returnmsg+ words[mf[str(place)]][str(number)]

                if (int(number) == 200):
                    returnmsg = u' مئتا'

                if (place == 2):
                    returnmsg = returnmsg + u' ألف'
                if (place == 3):
                    returnmsg = returnmsg + u' مليون'
                if (place == 4):
                    returnmsg = returnmsg + u' مليار'

                return returnmsg


            else:
                threey =int(number[0]) * 100
                threey=str(threey)
                if (words[mf[str(place)]][threey]):
                    returnmsg = returnmsg + words[mf[str(place)]][threey]

                twoyony =((int(number[1]) * 10) + int(number[2]))
                if (int(twoyony) == 2):
                    if (place == 1):
                        twoyony = words[mf[str(place)]]['2']
                    if (place == 2):
                        twoyony = u' ألفان'
                    if (place == 3):
                        twoyony = u' مليونان'
                    if (place == 4):
                        twoyony = u' ملياران'

                    if (int(threey) != 0):
                        twoyony='و'+str(twoyony)

                    returnmsg =returnmsg+' '+twoyony

                elif (int(twoyony) == 1):
                    twoyony=str(twoyony)
                    if (place == 1):
                        twoyony = words[mf[str(place)]]['1']
                    if (place == 2):
                        twoyony = u'ألف'
                    if (place == 3):
                        twoyony = u'مليون'
                    if (place == 4):
                        twoyony = u'مليار'

                    if (int(threey) != 0):
                        twoyony='و'+str(twoyony)

                    returnmsg = returnmsg+' '+twoyony




                else:
                    # if ((words[mf[str(place)]][twoyony])):
                    twoyony=str(twoyony)
                    if (words[mf[str(place)]].has_key(twoyony)):
                    # if words.has_key(twoyony):
                        twoyony = words[mf[str(place)]][twoyony]
                    else:
                        twoy=int(number[1]) * 10
                        twoy=str(twoy)
                        ony=number[2]
                        twoyony = words[mf[str(place)]][ony]+' و'+words[mf[str(place)]][twoy]
                    if ((twoyony!= '') and ( int(threey) != 0)):
                        returnmsg =  returnmsg+' و'+twoyony
                    else:
                        returnmsg =  returnmsg+' '+twoyony


                    if (place == 2):
                        returnmsg =returnmsg+ u' ألف'
                    if (place == 3):
                        returnmsg = returnmsg+ u' مليون'
                    if (place == 4):
                        returnmsg =returnmsg+ u' مليار'


        return returnmsg





number=11231233
numb=number2word(number)
numb.validate()
