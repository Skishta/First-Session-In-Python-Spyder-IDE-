              
#اولا البايثون هي أحدث اللغات المستخدمة للبرمجة
#In this training program
#you will learn how to collect
#analyze and visualize any size of data
#Learn ٍsome-NOT ALL- Python basics.
#Learn simplest way in OOP (Object-Oriented Programming) and data structures in python
#Be able to implement some algorithms or program using python
#Learn the most needed data science algorithms

                   '''FIRST SESSION In How to use Python on Spyder IDE'''
#print() function يتم استخدمها لاظهار الكلمات على الشاشة للمستخدم
#أما بالمسبة لل () الاقواس دى فتتم فقط للFunctions
#وعشان تظهر الكلمة للمستخدم لازم تستخدم علامات التنصيص وهى "" وتسمى بال Double quotation
print("hello world")
#معلومة: اى حاجة بين علامات التنصيص تعتبر نص بمعنى (string)
print("28")
#طيب انا لو عايز اطبع رقم والبرنامج يعتبرة رقم مش نص (عشان اعرف اعمل علية عمليات حسابية مثلا) ساعتها بنكتب الرقم بدون علامة التنصيص
print(28)
#بالنسبة للعمليات الحسابية فى البايثون فهى بكل بساطة داخل function print()and write the formula
print(9+2)
print(9-2)
print(9*2)
print(9/2)
#طيب توجد عمليات حسابية اخري اعرف اجيب بيهاباقى القسمة 
#باقى القسمة:هى مثلا لو قسمت 9 / 2 يساوى رقم 4 + رقم 4 وهيتبقى معانا رقم 1 : هنا رقم 1 دة بنسمية باقى القسمة
print(9%2)
#طيب توجد عمليات حسابية اخري بنسميها القسمة الصحيحة
#القسمة الصحيحة:هى مثلا لو قسمت 9 / 2 يساوى رقم 4.5 ..هنا رقم 4 بنسمية هيا القسمة الصحيحة..بمعنى انة بيلغى اى رقم عشري ويظهرلى الرقم الصحيح
print(9//2)
#بالنسبة للعمليات الحسابية على النصوص 
#نعرف نجمع نص على نص
print("Ahmed" + "Mahmooud")
#طيب لو عايز بينهم مسافة يبقى :
print("Ahmed" + " " + "Mahmoud" )
#ونعرف نضرب نص فى رقم
print("Ahmed"*5)
#Boolian Expression(True OR False)
#Is 2 equal to 2
print(2==2)
#Is 2 Not Equal 2
print(2!=2)
#is 2 larger than 3
#Is 2 smaller than 3
print(2<3)
print(2>3)
#is 2 larger than or equal 3
#Is 2 smaller than or equal 3
print(2<=3)
print(2>=3)
#طيب دلوقتى لو عايز اطلب من اليوزر انة يدخل ليا قيمة او نص معين
print(input("plz enter ur name: "))
#طيب دلوقتى بالنسبة للمتغيرات
#اذا اردت ان تسجل متغير معين و1الك لاستعمالة قدام الكود
#وطبعا عشان بتسجل متغير (نصى) فبتسجل المتغير بعلامات وتنصيص
myname="Ahmed"
#وعند الطباعة بتطلب print بدون علامات تنصيص
#عشان البايثون بيكون عارف ساعتها ان دة متغير وهيدور علية عندة فى قاعدة بياناتة
print(myname)
#هطلب من اليوزر يدخل اسمعة وهسجلة فى متغير
my_name=input("plz enter ur number: ")
#وبعدين هطبع المتغير اللى تم تخزينة للمستخدم
print(my_name)
#by default any input by INPUT function is string, whether its word or number
print(int(my_name) +8)
#طيب لو حابب اغير الtype بفتح قوس الfunction واكتب الinput بداخل الاقواس
#to delete space in the leading and trailing of the value (مسح اى مسافات اضافية فى بداية ونهاية الكلمة)
text= " Hello world "
text.strip()
#Convert the value of txt to upper case
text.upper()
text.lower()
#replace Letter H with J in the text 
text.replace("H","J")


int()
bool()
float()
str()
#مثلا
num1=int(input("plz enter num1: "))
print(num1 +5)