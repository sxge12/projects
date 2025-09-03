import math
import wave
import simpledate

sampleRate = 44100   # hertz
duration = 1.0       # seconds

frequencies = {'c': 523.25,
               'e': 659.25,
               'f': 698.46,
               'g': 783.99,
               'a': 880.00}
         

def initwavefile(name):
    '''opens a new wav file with specified name and 
    returns a handle to this new file'''
    wavef = wave.open(name,'wb')
    wavef.setnchannels(1) # mono
    wavef.setsampwidth(2) 
    wavef.setframerate(sampleRate)
    return wavef


def generatenote(noteletter, duration):
    '''writes data to open wave file (in global var wavef) to 
    synthesize the specified note for the specified duration.
    Does not return a value'''
    for i in range(int(duration * sampleRate)):
        frequency = frequencies[noteletter]
        value = int(32767.0*math.cos(frequency*math.pi*i/sampleRate))
        data = value.to_bytes(2, 'little', signed=True)
        wavef.writeframesraw( data )
    return



def finish(f):
    '''null-terminates then closes an open wave file handle.
    Does not return a value'''
    f.writeframes(b'')
    f.close()
    return

def silent(duration):
    '''insert duration seconds of silence into wav output'''
    for i in range(int(duration * sampleRate)):
            value = 0  # i.e. silence
            data = value.to_bytes(2, 'little', signed=True)
            wavef.writeframesraw( data )


def hourlydongs(hours):
    '''one dong for each hour, with a short silence in between dongs 
    (otherwise it sounds like one continuous note)'''
    for dong in range(hours):
        generatenote('e', 1.5) # big ben plays 'E' for dong
        silent(0.5) # space in between dongs


# main code (should properly wrap up in a function too!)
wavef = initwavefile('chimes.wav')
for note in 'fagcfgafafgccgaf':
    generatenote(note, duration)

num_dongs = (simpledate.currenthour()+12) % 12  # current hour is in range 0 to 23
hourlydongs(num_dongs)
finish(wavef)

