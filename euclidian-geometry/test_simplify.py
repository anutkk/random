import polygon_simplification
import matplotlib.pyplot as plt

points = [
[48.056121878025415, 133.41119448586684] ,
[39.4575616931798, 110.25505133863523]   ,
[2.32496094951693, 94.07932644982493]    ,
[28.064670235007227, 63.61420269325953]  ,
[76.73792951737678, 89.08746934863518]   ,
[42.916453205549, 51.16115747576866]     ,
[112.61923860127784, 113.46132719294717] ,
[44.527455361489324, 45.98216934077342]  ,
[57.157259708622355, 48.690400675238756] ,
[54.8674627411398, 45.53048608125157]    ,
 [121.25102646897845, 115.31092428549883],
 [130.47378217507648, 124.5361512617571] ,
 [120.473905862864, 109.40222219937085]  ,
 [90.70693903001619, 68.35882121926178]  ,
 [50.794602960874855, 10.513690194164816],
 [110.0445681440966, 81.9656535627703]   ,
 [120.35920820047632, 85.8960368309179]  ,
 [124.5819682979002, 54.5239484273893]   ,
 [137.81976587517988, 71.41871296903406] ,
 [147.91734692934327, 59.10468769189321] ,
 [153.59137730483772, 86.75637052209481] ,
 [155.05933649213864, 93.74304436882164] ,
 [157.87735337861128, 65.29434330127751] ,
 [167.15475190742853, 4.156879203784092] ,
 [159.6374900537337, 69.3931247688808]   ,
 [152.9977446521573, 131.2423361535524]  ,
 [168.3028809878587, 58.63592333723171]  ,
 [200.7655854996833, 7.226769827649937]  ,
 [204.99009766502948, 14.890553040321963],
 [186.14998421089052, 66.0664051080131]  ,
 [203.02655874655454, 73.87347138228408] ,
 [249.48584436291154, 22.170154733286008],
 [279.6751995848352, 0.3365967492489519] ,
 [277.70001049558925, 14.846171599793712],
 [250.6229509043064, 47.590748464668394] ,
 [206.60524876167457, 95.49744940074774] ,
 [257.69220510881235, 62.769164411281395],
 [250.2502483986794, 74.20048111683066]  ,
 [182.03903375697828, 126.70071321289944],
 [296.42551691719603, 51.67820505492393] ,
 [182.25107088912657, 131.78763443003376],
 [288.00442512383285, 72.89923174416862] ,
 [241.18115597695112, 105.17000189325456],
 [206.22948874427297, 126.6125731583673] ,
 [262.3575399046136, 104.86558337903008] ,
 [299.51726904657187, 90.0009950788099]  ,
 [236.409621261635, 122.14060378500626]  ,
 [202.8473672384145, 143.3251255143341]  ,
 [204.83244361477995, 161.16146394366766],
 [197.47022015108578, 161.90270192554405],
 [234.81243483568733, 173.2246100444355] ,
 [261.8684254279086, 180.6543192308179]  ,
 [291.14456484335903, 190.35764107039935],
 [281.1166464814341, 197.89734208900282] ,
 [265.66626740452347, 219.98753553393513],
 [288.57365406236073, 242.43419163421646],
 [239.32954783668202, 229.09532345587286],
 [288.6380177960715, 287.5428335914548]  ,
 [209.31030285220277, 210.022063295211]  ,
 [182.22601229730859, 188.76824670627767],
 [251.10605609725354, 283.23072539463965],
 [253.09576566319592, 296.58786262062785],
 [154.5433088922742, 156.8917375720399]  ,
 [209.538677824048, 252.3448936616814]   ,
 [175.73541797379758, 197.84370122067727],
 [198.9025895704854, 246.67963017897162] ,
 [170.80621556682246, 194.71878568679847],
 [168.35859107300465, 198.60223359738475],
 [183.35546112693953, 249.2500733409746] ,
 [186.0730714784971, 278.6756969099644]  ,
 [175.75189615975276, 244.0133469176749] ,
 [164.57991592442175, 230.81347867196644],
 [164.0501455228796, 279.9799927191983]  ,
 [150.6850205107241, 164.10844845878128] ,
 [141.83786484033664, 278.6907351517459] ,
 [139.02484940658604, 265.90181843120365],
 [148.78213423725487, 161.0834477818252] ,
 [127.10548527023109, 284.9941178164485] ,
 [123.18123547868632, 287.2795860156861] ,
 [125.17460583577385, 225.92977468546567],
 [97.94857626518969, 285.25125035849595] ,
 [95.04558868496953, 292.3916790754178]  ,
 [121.88273101795622, 210.79716534343228],
 [118.06278663220012, 209.58276320766157],
 [120.58197949738698, 196.80922521466695],
 [73.96435249416567, 269.89880501538295] ,
 [59.81473003420559, 250.0642043814337]  ,
 [35.38105173084685, 275.98881484177264] ,
 [95.24440318145821, 207.7513335101694]  ,
 [74.83459077801848, 222.3144267079754]  ,
 [25.89530226896177, 264.0585536218564]  ,
 [22.002407374030362, 256.9146148604643] ,
 [143.77562244240042, 155.1746497988737] ,
 [0.21922633571853645, 267.5247454858486],
 [133.87606964322748, 157.23696438053193],
 [42.80731020520312, 175.93140307910738] ,
 [75.57216559994424, 161.5774221873462]  ,
 [78.74146043715061, 157.64944480007938] ,
 [27.53837112007249, 160.42659323316894] ,
 [32.287829088126706, 150.0606298508805] ,
]

x,y = zip(*points)

out = polygon_simplification.simplify_pts(points, 50, 50)
x_val = [x[0] for x in out]
y_val = [x[1] for x in out]

print(len(x_val))

plt.plot(x_val,y_val, '-bo')
plt.plot(x,y,'or--')
plt.show()