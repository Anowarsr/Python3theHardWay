class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print(" "+"_" * 29)
        for line in self.lyrics:
            line= " ".join(["|",line])
            for count in range(len(line), 31):
                if count == 30:
                    line = "".join([line,"|"])
                else:
                    line = "".join([line," "])
            print(line)
        print(" "+"-" * 29)

happy_bday = Song(["Happy birthday to you", "From good friends and true,", "From old friends and new"])

bulls_on_parade = Song(["May good luck go with you", "And happiness too"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()