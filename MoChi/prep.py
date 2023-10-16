#!/usr/bin/env python3
from binascii import hexlify

key = b'moo{w4rabim0ch1}'
# the plaintext is super long so that it's easier to break
plaintext = b'''Mochi is a Japanese rice cake made of mochigome, a short-grain japonica glutinous rice, and sometimes other ingredients such as water, sugar, and cornstarch. The steamed rice is pounded into paste and molded into the desired shape. In Japan, it is traditionally made in a ceremony called mochitsuki. While eaten year-round, mochi is a traditional food for the Japanese New Year, and is commonly sold and eaten during that time. Mochi is a multicomponent food consisting of polysaccharides, lipids, protein, and water. Mochi has a heterogeneous structure of amylopectin gel, starch grains, and air bubbles. The rice used for mochi has a negligible amylose content and a high amylopectin level, producing a gel-like consistency. The protein content of the japonica rice used to make mochi is higher than that of standard short-grain rice. Mochi is similar to dango, which is made with rice flour instead of pounded rice grains. History Red rice was the original variant used in the production of mochi. The cultural significance of mochi in Japan is unique, though it has elements in common with other auspicious foods in other Asian countries. According to archaeological research, the homemade production of mochi increased beginning in the 6th century (Kofun period), when earthenware steamers became popular in every household, mainly in eastern Japan. In the Bungo no kuni fudoki, compiled in the late 8th century in the Nara period, a legend concerning mochi was described. According to the book, when a rich man made a flat mochi from leftover rice and shot an arrow at it, the mochi transformed into a white bird and flew away, and after that, the man's rice field became desolate and barren. This legend shows that round white mochi was historically held to have spiritual power. In the Heian period, mochi was often used in Shinto events to celebrate childbirth and marriage. According to the okagami compiled in the 12th century, emperors and nobilities used to put mochi into the mouths of babies that were 50 days old. In this period, it became customary in the aristocratic society for the bride and groom to eat mochi together at the bride's house three days after the wedding. The first recorded accounts of mochi being used as a part of New Year's festivities are from the Heian period. The nobles of the Imperial court believed that long strands of freshly made mochi symbolized long life and well-being, while dried mochi helped strengthen one's teeth. Accounts of it can also be found in The Tale of Genji. The custom of kagami mochi (mirror mochi) began among the samurai class during the Muromachi period. Kagami mochi are composed of two spheres of mochi stacked on top of one another, topped with a bitter orange (daidai). In welcoming the New Year, samurai decorated kagami mochi with Japanese armour and Japanese swords and would place them in the tokonoma (alcove in a traditional Japanese room where art or flowers are displayed) to pray for the prosperity of their families in the New Year. When people ate kagami mochi after the New Year period, they avoided cutting it with a hocho (knife) so as not to violate the kami, and smashed it with a wooden hammer after it naturally dried and cracked. Mochi continues to be one of the traditional foods eaten around Japanese New Year and is sold and consumed in abundance around this time. A kagami mochi is placed on family altars (kamidana) on December 28 each year.'''

def encrypt(m: bytes, k: bytes) -> bytes:
    return bytes([ch ^ k[i % len(k)] for i, ch in enumerate(m)])

ciphertext = encrypt(plaintext, key)
print(hexlify(ciphertext))