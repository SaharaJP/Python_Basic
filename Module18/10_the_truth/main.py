def decoded_text():
    decoded = ''.join(
        [alphabet[alphabet.index(sym) - 1]
         if sym in alphabet
         else sym
         for sym in text]
    )
    return decoded

def shifting_text():
    shifted = ''
    shift = 3

    for word in decoded.split():
        new_word = ''.join(
            [word[index - shift % len(word)]
             for index in range(len(word))]
        )
        if new_word.endswith('/'):
            shift += 1

        shifted += new_word + ' '

    return shifted

def replacing_sym(result):
    result = result.replace('/', '\n')
    result = result.replace('(', "'")
    result = result.replace('+', '')

    return result


text = 'vujgvmCfb tj ufscfu ouib z/vhm ' \
       'jdjuFyqm jt fscfuu uibo jdju/jnqm ' \
       'fTjnqm tj scfuuf ibou fy/dpnqm ' \
       'yDpnqmf jt cfuufs boui dbufe/dpnqmj ' \
       'uGmb tj fuufsc ouib oftufe/ ' \
       'bstfTq jt uufscf uibo otf/ef ' \
       'uzSfbebcjmj vout/dp ' \
       'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
       'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj ' \
       'Fsspst tipvme wfsof qbtt foumz/tjm ' \
       'omfttV mjdjumzfyq odfe/tjmf ' \
       'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
       'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
       'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud ' \
       'xOp tj scfuuf ibou /ofwfs ' \
       'uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
       'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb ' \
       'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'


decoded = decoded_text()
shifted = shifting_text()
result = replacing_sym(shifted)

print(result)