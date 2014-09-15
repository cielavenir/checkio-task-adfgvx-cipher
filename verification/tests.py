import random
import string

init_code = """
if not "encode" in USER_GLOBAL:
    raise NotImplementedError("Where is 'encode'?")
if not "decode" in USER_GLOBAL:
    raise NotImplementedError("Where is 'decode'?")

encode = USER_GLOBAL['encode']
decode = USER_GLOBAL['decode']
"""

run_test = """RET['code_result'] = {}
"""


def prepare_test(test, answer):
    return {
        "test_code": {"python-3": init_code + run_test.format(test), "python-27": init_code + run_test.format(test)},
        "show": {"python-3": test, "python-27": test},
        "answer": answer}


TESTS = {
    "Basics": [

    ],
    "Encode": [

    ],
    "Decode": [

    ],
    "Random": [

    ]
}

BASIC_TESTS = [
    ['encode("I am going", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "cipher")', 'FXGAFVXXAXDDDXGA'],
    ['decode("FXGAFVXXAXDDDXGA", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "cipher")', 'iamgoing'],
    ['encode("attack at 12:00 am", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz", "privacy")', 'DGDDDAGDDGAFADDFDADVDVFAADVX'],
    ['decode("DGDDDAGDDGAFADDFDADVDVFAADVX", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz", "privacy")', 'attackat1200am'],
    ['encode("ditiszeergeheim", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz", "piloten")', 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA'],
    ['decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz", "piloten")', 'ditiszeergeheim'],
]

ENCODE_TESTS = [
    [
        'encode("One 1, Two 2, Three 3, Four 4, Five 5, Six 6, Seven 7, Eight 8, Nine 9, Zero 0", "vcpguojhkl01t7mbs2d4nqfx9y5wz8ria63e", "monty")',
        'AXVXXXAAXXXGAFXDGFVAGXAAXVADAFGVXDAAXXXXXDGFAXXGDVDFAFDFFXVAFFXDXGVGAFXXXXGVDVXDXAFDXVXVXVXXGXDXGAXV'],
    [
        'encode("Your highness, when I said that you are like a stream of bat\'s piss, I only mean that you shine out like a shaft of gold when all around it is dark", "tlw9i8r1v3sh7ck56fb0ydux2oeqjmpzg4an", "python")',
        'DXXVXVVXFVDFAVXAVVDFAAVVDDFXAFGFDAXAGFVVXVFVGVDAVVAXAVVDFVXFVXVVVVDDFXDDGVVGAXDVDGXVDAXDVGDDVGXDGDXGAXXVVAXAVGAXGDXVAXXAAGVFDVVXXDXVXXVDVAFDFFADXXGADDVDDDDAADGXAVAXFAAAAVAAGAVAVDAXGVADXAGFFAFFFXVAAVFFVFDVAVXXXVDXFAFVXXDXVVVVVA'],
    [
        'encode("I don\'t wanna talk to you no more, you empty headed animal food trough wiper! I fart in your general direction! You mother was a hamster and your father smelt of elderberries!", "axn68hz14wotvukdgp57rljeym0s9qb3fc2i", "daily")',
        'XAGAXFVFVGAGXAAFFAFFFFGGXGXDFAFFFDVDDAFVXVXAAGAGGGVGXGFVXVDFDGDVDVVDFAAXADXVGDDXXAXAGXGGGGDAVXGAADGAVDAXVXDXGAGXFFAFAFVDVFDXDXFGXADGDVXXXFAVFFAGGXAVDXDGAGGFDFDXVGXGGXXGGDAAADAADGVVXGGAXGVDVAXGFDFFVGAXXXFFVGGAADFFVXXGDDFFFGXDXAAGXDFDXFDVXGAVGDXFXFFAXVDGXGXXXVDDXAAVXAGFFAFGXGGXFG'],
    [
        'encode("My philosophy, like color television, is all there in black and white", "s2nb85veyufpc6kriwqxjh9d7314azm0lgot", "checkio")',
        'XGXDXDXXDAAVXFAVVFXDFAGFFXDDFFXGDAFAGDAGVXFDFXDAFVXGFVVXXDXXDFXFXFXAXDFXFGFFVAGVAVDAVVFGDGAFGDXFVFFVGFVVAFDVFFXV'],
    [
        'encode("Strange women lying in ponds distributing swords is no basis for a system of government!", "59ghwyslm1j8ti07n234aofrb6zdukpxeqcv", "world")',
        'GVAFDDFAVGFDFVAXFVGDGFDFGGGFFAFFDVFFXVVAFVFAGAFAFVGXXGGFDVAGFGFAVFGDDGAFFGGDGDAGAFFAXFFFFXGFXAVFADXVDDGDAVAGXAAGFXVFDXAVXDFDGGFAVAAVVDGFDGDADVXXXA'],
    [
        'encode("We are no longer the knights who say ni! We are now the knights who say ekki-ekki-ekki-pitang-zoom-boing!", "345bcgxa6p79z8svo01ty2hkueiljfqwrmnd", "ubermonty")',
        'DXVGFXDVVVXGFVDVXAXVVAVADGDFDGVVDGFFGDVVDGVXDXXGVGXGDFVXGXXGVVFGVFFGXVDFFDVDGVFVXDXDFXGXDVVDFXVXGFDVGVFDGXGAFFFFXDFFVDVFDXVFXVXXDXDVFDDXVADGFVGAGAVVGVFFXDGFXDVFDVXV'],
    [
        'encode("Nudge, nudge, wink, wink. Know what I mean?", "upcvxad80n3j6ohkfwiy5s71et2qlrb94mzg", "yep")',
        'GDXDAXAGGFAFGFXFXGGAGAAVGDXFAFXDGDDFFVAVXDAXAAAVXDGGGFGFXADXAD'],

]

DECODE_TESTS = [
    [
        'decode("DGFGDVVGFXDDGFADGGAGAXXFXVVFFFFDDXFVVGVDFDVVAXXGXFAVFGFGXAVXXGDGADAFFVAGAAGFAFXVXFVXFGXFGFXVDFXFAFAG", "yozmhbrk3085691qlixje2w7dcustavpn4fg", "yep")',
        'one1two2three3four4five5six6seven7eight8nine9zero0'],
    [
        'decode("AGFAAXAGGVAGDXAGFGGGVFAGGGFGFGAXFFDFGXAFGGFVDGDAVGDAGDGFAFADGGVDVFDFXVDAGFXAFDFFAAFAVFFVFGFFFVAVVDFAAVGGVVAAAVGGAFAGAAAFGXDFADFGFFFAXFGFGVFFVDXFVVXAGVAFGGFGFXFXXGDVDFFXVGFXAGAVFAFXFDVGAXFFFXAAVGFXFXDGFVDVGVDXAXXGDAFDDXAFDAVFFX", "r0e83zu15w62gntj4pqoisd7ymh9fxackvlb", "ubermonty")',
        'yourhighnesswhenisaidthatyouarelikeastreamofbatspissionlymeanthatyoushineoutlikeashaftofgoldwhenallarounditisdark'],
    [
        'decode("XFXFAFXVXGXVVGGFGFXFXGFAFFVGGGAXVXVGVGFFGFFDXVAAGFGDXAGDVFFFVXXVGAGFGDFXAAVAAXGVVVXDGFGGGVXAGVFFVAGAAFGVVVGAGXXXVXFFAXAGXGDAFGVFVGAVVGXGXXAXAGAVAXVAADGDGXXGFGXAAAGGADGVFVFXVGGAXGVGGDGFXDXDGGAAXAVVFDGFXAXGFXFXGVXAVGGFAFGGGXGAFVVFXAXAVGFXFGXVAAGGFDGFGXGGGFGGXXGFGFAVGFVGFGDGXGGFGG", "j4lhf1682z0s7paqwkrdxemi3gtc5yo9bunv", "world")',
        'idontwannatalktoyounomoreyouemptyheadedanimalfoodtroughwiperifartinyourgeneraldirectionyoumotherwasahamsterandyourfathersmeltofelderberries'],
    [
        'decode("XFXXAGADGXDXDGDXXVDAGXFGGXGGGGAFGFGDFGXDVGXDXVDDGFVFGFFFVXAXADXGAGXXAGGADXGDXDDXGVDAXXXDDAGGDDGXVDXVFXXVDXDXXXAX", "gy3zul5j8ntkbhf610verc7ix2wq49dsapom", "checkio")',
        'myphilosophylikecolortelevisionisallthereinblackandwhite'],
    [
        'decode("VXXFADFXGVGVAVXFXVGVVVVADGDXAVDGGVXXGFXVGAGGGFGFXVGVVDFXDVGAXVGXFGFXVVDDGVGVVAVADDGFXVFXGXADFVXFFFVVVXVVVXAVFXFVGFADFVFXDVGVAFXAGAFXDVFXGFXVAAGVDA", "b4ft7z0my8ucpx6o2dj591hgerkisl3vnwqa", "daily")',
        'strangewomenlyinginpondsdistributingswordsisnobasisforasystemofgovernment'],
    [
        'decode("VVXDVFDFFDGVFGDGGFVGFFFDFDGDDFVGDGGFDVVGVGVGDFVGFGDFADXGVFGGGFAGFFFFXVGXDFXDXGVFGFXVGXFXVGXXXGVDDAVADDFXVDVVDFFADVDDAVAFXVGGGFAFXDDGXXVXGVFDVVGVGDGDDVFDFFDFFVGVDFFD", "xysj4l6gk5v8bq1wec3nph70fmo9tudazir2", "python")',
        'wearenolongertheknightswhosayniwearenowtheknightswhosayekkiekkiekkipitangzoomboing'],
    [
        'decode("VFVFVFAAGXFDVGFGFAAVAVXAVFGFGXXAXDGDVFAVAVAVFVXFAFAVAVVXXFVADA", "isdz78bm269fat0rx3uogc4h5lnvewkjpy1q", "monty")',
        'nudgenudgewinkwinkknowwhatimean'],

]

for t in BASIC_TESTS:
    TESTS["Basics"].append(prepare_test(t[0], t[1]))

for t in ENCODE_TESTS:
    TESTS["Encode"].append(prepare_test(t[0], t[1]))

for t in DECODE_TESTS:
    TESTS["Decode"].append(prepare_test(t[0], t[1]))

for dummy_counter in range(5):
    length = random.randint(20, 30)
    message = "".join(random.choice(string.ascii_lowercase + string.digits) for dummy_j in range(length))
    key1 = list(string.ascii_lowercase + string.digits)
    random.shuffle(key1)
    key = "".join(key1)
    key1 = ''.join(key1)
    key2 = list(string.ascii_lowercase*2)
    random.shuffle(key2)
    key2 = ''.join(key2[:7])
    TESTS["Random"].append(
        prepare_test('decode(encode("{0}", "{1}", "{2}"), "{1}", "{2}")'.format(message, key1, key2), message))