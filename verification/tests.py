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
    ['encode("attack at 12:00 am", "na1c3h8tb2ome5wrpd4f6g7i9j0klqsuvxyz", "privacy")', 'DGDDDAGDDGAFADDFDADVDVFAADVX'],
    ['decode("DGDDDAGDDGAFADDFDADVDVFAADVX", "na1c3h8tb2ome5wrpd4f6g7i9j0klqsuvxyz", "privacy")', 'attackat1200am'],
    ['encode("ditiszeergeheim", "na1c3h8tb2ome5wrpd4f6g7i9j0klqsuvxyz", "piloten")', 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA'],
    ['decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA", "na1c3h8tb2ome5wrpd4f6g7i9j0klqsuvxyz", "piloten")', 'ditiszeergeheim'],
    ['encode("I am going", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "weasel")', 'DXGAXAAXXVDDFGFX'],
    ['decode("DXGAXAAXXVDDFGFX", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "weasel")', 'iamgoing'],


]

ENCODE_TESTS = [
    [
        'encode("One 1, Two 2, Three 3, Four 4, Five 5, Six 6, Seven 7, Eight 8, Nine 9, Zero 0", "d9sr4qxvaz75yu2hkwpm8j63b1legot0ifnc", "monty")',
        'VGFFAGVGXGXVDVXGXVDGXDVAVXFVDXDFVVVAXGVXXVXXGGXAFDFADDFXVVGVVXXFGXDXDAAVGVVGFAGXVAFGVGAGVFGGXGFFXDAD'],
    [
        'encode("Your highness, when I said that you are like a stream of bat\'s piss, I only mean that you shine out like a shaft of gold when all around it is dark", "xk4wre5o1l0fyhmja62n7qc8it9dsv3gzbpu", "python")',
        'DDDVDAADAVGXDVXDAAGXDDXADGXDDDGXGVDDGDXADVXVGVDVAVVFGVVDAVDAVDXAVVDDGDGDGAVXVGVAVVFDAVFAFXVVDFFFFVGXVFFDDAGDDVVFFAXAAGFVVXAAVADFXVGFGFDFAVAVDDDFFFXVVADFFVFVVFFFDAVFDVVVDAVVXVDDAFVXVADAGVVAAVDXGDVDDXXDVXDVVVDFDVDDXDDVXXGDVVXAVV'],
    [
        'encode("I don\'t wanna talk to you no more, you empty headed animal food trough wiper! I fart in your general direction! You mother was a hamster and your father smelt of elderberries!", "chtqrlz0fxdj61wgesi5kya4n7uv93o2p8mb", "daily")',
        'AVFVFGAVAAGFFAVDAGFDVFFFAAAXVVVDVAAXVAVFDFVVGAVFXAAAVFVFGAFAAXXAXAGFXGGVVVDAAFFFGVGGAVAXAAXGXFAVAVFVGFGDFVXVFXAVDAGAGFGFXVXVADDVGVXVXGGVDVVAFAGVFFVAXDFXGXAAXVAVXXDXAVGXVAVGVAGVVFAXFFVGAAAAAAAAFAAVGFVGVGAVAFFGVAVDADFAVAFDVAAXFVVAFXAXVVVGVFVXXXFVDXVGFGFFVAAAAGFAVGVXFGVVFAVFFFVXVF'],
    [
        'encode("My philosophy, like color television, is all there in black and white", "gxy3dft2qis8zljen0o4671kwabuhmc5r9vp", "checkio")',
        'VVGXFFFDFDFVDXFVVVDADDVDXGFXDDFVFVXFVFXVAXDGDAGVVDAFVDDAAXFGAGGXFDGDFFDFGADFGVVGAAGVGGDVGFAVVGXDAFXAFDGAVDGGDXVG'],
    [
        'encode("Strange women lying in ponds distributing swords is no basis for a system of government!", "la159r6ng4vetycs20xfwzkdbp7ohquj8im3", "world")',
        'ADGVAGXDGXFGFDGXXDAGVDFXGGAVFADXXDXFVDGGXADGAGDAXDADDGVXXDGAFVXFDDGFGAAXFVXFGFGAGFVDVDXFDDGDDDDDGFXXGFGFGVGGXFAVFDDDFXDFDADGVXXAVADFGGVDFGFGXDDXDA'],
    [
        'encode("We are no longer the knights who say ni! We are now the knights who say ekki-ekki-ekki-pitang-zoom-boing!", "3rktdiz9805hujnswgp16lfcvm2x4oqa7ybe", "ubermonty")',
        'VFFDXFDXFXXDGXXAXXXXFFXFVXXVXDXXXAXDVXXXXDXFDFFAXAFAGVXAGAFAXADAFFGAFADVXDGXAXVFAVFGFFAFXXAXVXXXDGXXAXVXAFAAVDVDFGFXXGAGXFAXFXFFXFGAGXVFXFVXXXAFDFXXAFFGFXDXFDAXGFVF'],
    ['encode("Nudge, nudge, wink, wink. Know what I mean?", "ojc35lab407zsrqev1tkhp9yi6wu2gnxfd8m", "yep")',
     'AXXXGVGVAVAGDAFGAVXDAVGFAXXVAGFXDXAVFGAFAXGVGVGFFXDVAGAVFDAXGX'],


]

DECODE_TESTS = [
    [
        'decode("DXDXDGVXFXDVVDXXXFAXXGDDGGDDGDAVDGFGGVVVFAVGGXFXADFAFXGXFAVGFXVXGVXGGVXFAGXFXAFVGFAFDXGFFFDVDGGFAFXX", "zm3ahs68ig9bc7xy4pu1jntvld2rk05oewfq", "yep")',
        'one1two2three3four4five5six6seven7eight8nine9zero0'],
    [
        'decode("AAGAXFAAGDXFAFXFGAGAFAXDGAFFGAXFFXDXGFXXGAFDDDAGXDXDFADDGAGDFGGAGVXAFGFXAFFGVFFXAAGAGAFDDAFXGGDDFXDGADGAXGDADGGAAXAAAAXFVFDXXDFGAFXXVDADFFADDDVVGXFDAXDAVFDAGFGDXADDDADFGAVFAADGVAVFVXFFXFFAGFAAFFDFGFAFADADGDDFXFFADAVXAFXXDAFAFV", "noieqp9mbxhd7glswayr4f21kz5jc0ut8v36", "ubermonty")',
        'yourhighnesswhenisaidthatyouarelikeastreamofbatspissionlymeanthatyoushineoutlikeashaftofgoldwhenallarounditisdark'],
    [
        'decode("FFGDXFFVFAGAVAVDFXFFGDGXAFVAVAXGGGVAGAADFFAFGVDXVFVFDXVFGDADGVGAVVFFVFAGXVGVDGAVGVGDVDXAXVGVVAADGXVVDFAAGVVXAGGGAGFXVGVAVVDDDVVAVVXVAVGAGFXGXVXGVFADXADAAGVADVVXVXAVXAVVAVAFVAFXFAGDVFXDFFFDXADXGVVVAFVFGVFDDVAVAVFXGAFXDXAAXVXVDVGXFVFVVAGVAAGADVAADDXDXVAAAXAXFVFFADDAVDVAADAAFAVFAA", "8a62srwhbzf3m04joquptxncegd1y97vki5l", "world")',
        'idontwannatalktoyounomoreyouemptyheadedanimalfoodtroughwiperifartinyourgeneraldirectionyoumotherwasahamsterandyourfathersmeltofelderberries'],
    [
        'decode("XVFDGFGGFAAVGVAVVDGGXAVXAFFGXXGVFXAAVFDGGDDADXAAGVXXGVVFXDGFGFFVGXFAGFXGFDXAAAGADGAFAADGAXDGGADDGADGXDAGADAADDVA", "sc7nq45pw6d9ek3of8ylv2utz10harimxgjb", "checkio")',
        'myphilosophylikecolortelevisionisallthereinblackandwhite'],
    [
        'decode("DFFXXXXDVFVVDDFXAFVFDVDGXFFDXFXFVADDVXADXDXFVDVXAFVFDFVXXAXGAAVDXFXDDFXXVFVFDDDGXXXXFAXDXDXFXDFXXDDDDDDVDDDDVFXAVXXFXVXAXGVDADAGVGXAXDXFVXAFXGVVXG", "hz1qwedb78inasg3km6l49ft52x0crpuvjoy", "daily")',
        'strangewomenlyinginpondsdistributingswordsisnobasisforasystemofgovernment'],
    [
        'decode("AAVXFVXADGVFDGDGVAAAVVGDGVADDDAGDGVADAAVAAFGDVAAVADDXDFDAXADAAFDXXAXGAAFDXGDGDAXDAGADGXGAAFGFDADFFAFDDXGAFAAFXXXFADFFAFAGAADAAFXGDDVFDGGVFDDFAAFGDADDFVXADGVVAAFXDDX", "xothwv1nuzkfsa9y2gicrdm8q37p54e6j0lb", "python")',
        'wearenolongertheknightswhosayniwearenowtheknightswhosayekkiekkiekkipitangzoomboing'],
    [
        'decode("FAFADVGXFXXDFAVAVGXFXDVGDVDVDXGDGAAGVVFVFVDDVFXADAXDXDFXGVDAXA", "a9uch1sq5rgwo6vyn73ilb8k4ef0xjdmptz2", "monty")',
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
    secret_alphabet = list(string.ascii_lowercase + string.digits)
    random.shuffle(secret_alphabet)
    secret_alphabet = ''.join(secret_alphabet)
    # Key doesn't have repeated letters
    key = list(string.ascii_lowercase * 2)
    random.shuffle(key)
    key = ''.join(key[:7])
    TESTS["Random"].append(
        prepare_test('decode(encode("{0}", "{1}", "{2}"), "{1}", "{2}")'.format(message, secret_alphabet, key),
                     message))
