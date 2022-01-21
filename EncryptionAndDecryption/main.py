"""
Programming Project 1: Affine/Substitution Cipher Implementation
Author: Sam Hoag
Date: January 12, 2022
Instructor: Dr. Cutter

This program provides functions to encrypt and decrypt a string using the affine and substitution ciphers and a provided key.
"""

from AffineCipher import AffineCipher
from Alphabet import Alphabet
from SubstitutionCipher import SubstitutionCipher
from CodeCracking.SmartCracker import SmartCracker


def affine_cipher_test(alphabet, key, text):
    """
    For testing the affine cipher.
    Prints plain, ciphered, and deciphered text.

    :param alphabet: Dictionary[character, integer] - The alphabet of the text to be used for the cipher and
                                                      corresponding integer values
    :param key: List of 2 Integers - Values to be used as the key. Ensure they comply with the rules of the
                                     affine cipher.
    :param text: String - The text to be used for the cipher.
    """
    affine_cipher = AffineCipher(key, alphabet)

    ciphered = affine_cipher.affine_cipher_encrypt(text)

    print("Plaintext in: " + text)
    print("Ciphered text: " + ciphered)
    print("Deciphered out: " + affine_cipher.affine_cipher_decrypt(ciphered))


def substitution_cipher_test(alphabet, text):
    """
    For testing the substitution cipher.
    Prints plain alphabet, ciphered alphabet, plaintext, ciphered, and deciphered text.

    :param alphabet: List of characters - The alphabet of the text to be used for the cipher
    :param text: String - The text to be used for the cipher
    """
    substitution_cipher = SubstitutionCipher(alphabet)
    ciphered_text = substitution_cipher.encrypt_decrypt(True, text)
    deciphered_text = substitution_cipher.encrypt_decrypt(False, ciphered_text)

    print("Plain alphabet in: " + str(alphabet.alphabet))
    print("Ciphered alphabet out: " + str(alphabet.substitution_alphabet))
    print("Plaintext in: " + text)
    print("Ciphered text out: " + ciphered_text)
    print("Ciphered text in: " + ciphered_text)
    print("Plaintext out: " + deciphered_text)


def main():
    """
    Main function for the program.
    For the time being, edit alpha_dict to edit the alphabet, edit k to alter the key used to encipher,
    and edit text to edit the plaintext to be enciphered.
    """

    text_simple = "hello world."
    hobbes = "Whatsoever therefore is consequent to a time of Warre, where every man " \
             "is Enemy to every man; the same is consequent to the time, wherein men " \
             "live without other security, than what their own strength, and their " \
             "own invention shall furnish them withall. In such condition, there is " \
             "no place for Industry; because the fruit thereof is uncertain; and " \
             "consequently no Culture of the Earth; no Navigation, nor use of the " \
             "commodities that may be imported by Sea; no commodious Building; no " \
             "Instruments of moving, and removing such things as require much force; " \
             "no Knowledge of the face of the Earth; no account of Time; no Arts; no " \
             "Letters; no Society; and which is worst of all, continuall feare, and " \
             "danger of violent death; And the life of man, solitary, poore, nasty, " \
             "brutish, and short."

    jefferson = "THE DECLARATION OF INDEPENDENCE OF THE UNITED STATES OF AMERICA   When in the Course of human " \
                "events, it becomes necessary for one people to dissolve the political bands which have connected " \
                "them with another, and to assume, among the Powers of the earth, the separate and equal station to " \
                "which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of " \
                "mankind requires that they should declare the causes which impel them to the separation.  We hold " \
                "these truths to be self-evident, that all men are created equal, that they are endowed by their " \
                "Creator with certain unalienable Rights, that among these are Life, Liberty, and the pursuit of " \
                "Happiness. That to secure these rights, Governments are instituted among Men, deriving their just " \
                "powers from the consent of the governed, That whenever any Form of Government becomes destructive of " \
                "these ends, it is the Right of the People to alter or to abolish it, and to institute new " \
                "Government, laying its foundation on such principles and organizing its powers in such form, " \
                "as to them shall seem most likely to effect their Safety and Happiness.  Prudence, indeed, " \
                "will dictate that Governments long established should not be changed for light and transient causes; " \
                "and accordingly all experience hath shown, that mankind are more disposed to suffer, while evils are " \
                "sufferable, than to right themselves by abolishing the forms to which they are accustomed.  But when " \
                "a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to " \
                "reduce them under absolute Despotism, it is their right, it is their duty, to throw off such " \
                "Government, and to provide new Guards for their future security. --Such has been the patient " \
                "sufferance of these Colonies; and such is now the necessity which constrains them to alter their " \
                "former Systems of Government. The history of the present King of Great Britain is a history of " \
                "repeated injuries and usurpations, all having in direct object the establishment of an absolute " \
                "Tyranny over these States.  To prove this, let Facts be submitted to a candid world.  He has refused " \
                "his Assent to Laws, the most wholesome and necessary for the public good.  He has forbidden his " \
                "Governors to pass Laws of immediate and pressing importance, unless suspended in their operation " \
                "till his Assent should be obtained; and when so suspended, he has utterly neglected to attend to " \
                "them.  He has refused to pass other Laws for the accommodation of large districts of people, " \
                "unless those people would relinquish the right of Representation in the Legislature, " \
                "a right inestimable to them and formidable to tyrants only.  He has called together legislative " \
                "bodies at places unusual, uncomfortable, and distant from the depository of their Public Records, " \
                "for the sole purpose of fatiguing them into compliance with his measures.  He has dissolved " \
                "Representative Houses repeatedly, for opposing with manly firmness his invasions on the rights of " \
                "the people.  He has refused for a long time, after such dissolutions, to cause others to be elected; " \
                "whereby the Legislative Powers, incapable of Annihilation, have returned to the People at large for " \
                "their exercise; the State remaining in the mean time exposed to all the dangers of invasion from " \
                "without, and convulsions within.  He has endeavoured to prevent the population of these States; for " \
                "that purpose obstructing the Laws of Naturalization of Foreigners; refusing to pass others to " \
                "encourage their migration hither, and raising the conditions of new Appropriations of Lands.  He has " \
                "obstructed the Administration of Justice, by refusing his Assent to Laws for establishing Judiciary " \
                "Powers.  He has made judges dependent on his Will alone, for the tenure of their offices, " \
                "and the amount and payment of their salaries.  He has erected a multitude of New Offices, " \
                "and sent hither swarms of Officers to harass our People, and eat out their substance.  He has kept " \
                "among us, in times of peace, Standing Armies without the Consent of our legislatures.  He has " \
                "affected to render the Military independent of and superior to the Civil Power.  He has combined " \
                "with others to subject us to a jurisdiction foreign to our constitution, and unacknowledged by our " \
                "laws; giving his Assent to their Acts of pretended legislation:  For quartering large bodies of " \
                "armed troops among us:  For protecting them, by a mock Trial, from Punishment for any Murders which " \
                "they should commit on the Inhabitants of these States:  For cutting off our Trade with all parts of " \
                "the world:  For imposing taxes on us without our Consent:  For depriving us, in many cases, " \
                "of the benefits of Trial by Jury:  For transporting us beyond Seas to be tried for pretended " \
                "offences:  For abolishing the free System of English Laws in a neighbouring Province, establishing " \
                "therein an Arbitrary government, and enlarging its Boundaries so as to render it at once an example " \
                "and fit instrument for introducing the same absolute rule into these Colonies:  For taking away our " \
                "Charters, abolishing our most valuable Laws, and altering fundamentally the Forms of our " \
                "Governments:  For suspending our own Legislatures, and declaring themselves invested with Power to " \
                "legislate for us in all cases whatsoever.  He has abdicated Government here, by declaring us out of " \
                "his Protection and waging War against us.  He has plundered our seas, ravaged our Coasts, " \
                "burnt our towns, and destroyed the lives of our people.  He is at this time transporting large " \
                "armies of foreign mercenaries to compleat the works of death, desolation and tyranny, already begun " \
                "with circumstances of Cruelty & perfidy scarcely paralleled in the most barbarous ages, and totally " \
                "unworthy of the Head of a civilized nation.  He has constrained our fellow Citizens taken Captive on " \
                "the high Seas to bear Arms against their Country, to become the executioners of their friends and " \
                "Brethren, or to fall themselves by their Hands.  He has excited domestic insurrections amongst us, " \
                "and has endeavoured to bring on the inhabitants of our frontiers, the merciless Indian Savages, " \
                "whose known rule of warfare, is an undistinguished destruction of all ages, sexes and conditions.  " \
                "In every stage of these Oppressions We have Petitioned for Redress in the most humble terms:  Our " \
                "repeated Petitions have been answered only by repeated injury.  A Prince, whose character is thus " \
                "marked by every act which may define a Tyrant, is unfit to be the ruler of a free People.  Nor have " \
                "We been wanting in attention to our British brethren. We have warned them from time to time of " \
                "attempts by their legislature to extend an unwarrantable jurisdiction over us. We have reminded them " \
                "of the circumstances of our emigration and settlement here.  We have appealed to their native " \
                "justice and magnanimity, and we have conjured them by the ties of our common kindred to disavow " \
                "these usurpations, which would inevitably interrupt our connections and correspondence.  They too " \
                "have been deaf to the voice of justice and of consanguinity.  We must, therefore, acquiesce in the " \
                "necessity, which denounces our Separation, and hold them, as we hold the rest of mankind, " \
                "Enemies in War, in Peace Friends.  We, therefore, the Representatives of the United States of " \
                "America, in General Congress, Assembled, appealing to the Supreme Judge of the world for the " \
                "rectitude of our intentions, do, in the Name, and by the Authority of the good People of these " \
                "Colonies, solemnly publish and declare, That these United Colonies are, and of Right ought to be " \
                "Free and Independent States; that they are Absolved from all Allegiance to the British Crown, " \
                "and that all political connection between them and the State of Great Britain, is and ought to be " \
                "totally dissolved; and that as Free and Independent States, they have full Power to levy War, " \
                "conclude Peace, contract Alliances, establish Commerce, and to do all other Acts and Things which " \
                "Independent States may of right do.  And for the support of this Declaration, with a firm reliance " \
                "on the Protection of Divine Providence, we mutually pledge to each other our Lives, our Fortunes and " \
                "our sacred Honor. "

    alphabet_source_string = '`1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,.' \
                             '/!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?\" '

    alphabet = Alphabet(alphabet_source_string)

    affine_key = [27, 9]

    print("=============================")
    print("Affine Cipher Test")
    print("-----------------------------")
    affine_cipher_test(alphabet.affine_alphabet, affine_key, hobbes)
    print("=============================")
    print("Substitution Cipher Test")
    print("-----------------------------")
    substitution_cipher_test(alphabet, hobbes)

    # encrypted_message = SubstitutionCipher(alphabet).encrypt_decrypt(True, jefferson)
    # print(encrypted_message)
    # code_breaker = SmartCracker(encrypted_message)
    # code_breaker.freq_analysis()
    # code_breaker.freq_swap()


if __name__ == '__main__':
    main()
