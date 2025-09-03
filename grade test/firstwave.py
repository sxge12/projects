import math
import wave

sampleRate = 44100   # hertz
duration = 1.0       # seconds
frequency = 440.0    # 440 hertz corresponds to note A

# initialize wave file
wavef = wave.open('sound.wav','wb')
wavef.setnchannels(1) # mono
wavef.setsampwidth(2)
wavef.setframerate(sampleRate)

# generate signal and save to file
for i in range(int(duration * sampleRate)):
    value = int(32767.0*math.cos(frequency*math.pi*i/sampleRate))
    data = value.to_bytes(2, 'little', signed=True)
    wavef.writeframesraw( data )

# close wave file
wavef.writeframes(b'')
wavef.close()


