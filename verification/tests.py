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
    ["encode('I am going', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','weasel')", 'DXGAXAAXXVDDFGFX'],
    ["decode('DXGAXAAXXVDDFGFX', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','weasel')", 'iamgoing'],
    ["encode('attack at 12:00 am','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','privacy')", 'DGDDDAGDDGAFADDFDADVDVFAADVX'],
    ["decode('DGDDDAGDDGAFADDFDADVDVFAADVX','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','privacy')", 'attackat1200am'],
    ["encode('ditiszeergeheim','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','piloten')", 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA'],
    ["decode('DFGGXXAAXGAFXGAFXXXGFFXFADDXGA','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','piloten')", 'ditiszeergeheim'],
]

ENCODE_TESTS = []

DECODE_TESTS = []

for t in BASIC_TESTS:
    TESTS["Basics"].append(prepare_test(t[0], t[1]))

for t in ENCODE_TESTS:
    TESTS["Encode"].append(prepare_test(t[0], t[1]))

for t in DECODE_TESTS:
    TESTS["Decode"].append(prepare_test(t[0], t[1]))

for _ in range(5):
    length = random.randint(20, 30)
	message = "".join(random.choice(string.ascii_lowercase+string.digits) for _ in range(length))
	key1 = list(string.ascii_lowercase+string.digits)
	random.shuffle(key1)
	key2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
    TESTS["Random"].append(prepare_test('decode(encode("{0}", "{1}", "{2}"), "{1}", "{2}")'.format(message, key1, key2), message))