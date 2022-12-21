import math

class library(): 

    def __init__(self) -> None:
        self.dictionary, self.reverse_dictionary = self.get_dictionaries()
        self.vocab_size = len(self.dictionary.items())
        self.p = 1655894692317271730103668502307561173694843054437131243711687423073180483650245638903341421046693617743
        self.big_int = 957732584718123583502973967164235564300890376886669516777288105363974772912376162814322448314533273933
        self.mod_inv = pow(self.big_int, -1, self.p)

    def get_dictionaries(self):
        dictionary = {0 : 'a',1 : 'b',2 : 'c',3 : 'd',4 : 'e',
            5 : 'f',6 : 'g',7 : 'h',8 : 'i',9 : 'j',10 : 'k',
            11 : 'l',12 : 'm',13 : 'n',14 : 'o',15 : 'p',
            16 : 'q',17 : 'r',18 : 's',19 : 't',20 : 'u',
            21 : 'v',22 : 'w',23 : 'x',24 : 'y', 25 : 'z',
            26 : '.',27 : ',',28 : ' ',}
        dictionary[0]
        reverse_dictionary = {item[1]: item[0] for item in dictionary.items()}
        return dictionary, reverse_dictionary


    def id_to_text(self, text_id):
        text = ''
        while text_id > 0:
            digit = text_id % self.vocab_size
            text = self.dictionary[digit] + text
            text_id = math.floor(text_id / self.vocab_size)
        return text

    def page_num_to_text_id(self, page_num):
        return page_num * self.big_int % self.p

    def text_id_to_page_num(self, text_id):
        return text_id * self.mod_inv % self.p

    def get_page(self, page_num):
        id = self.page_num_to_text_id(page_num)
        text = self.id_to_text(id)
        return text

    