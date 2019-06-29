# Example: Sound

from wave import open
from struct import Struct
from math import floor

frame_rate = 44100

def encode(x):
    """Encode float x between -1 and 1 as two bytes.
    (See https://docs.python.org/3/library/struct.html)
    """
    i = int(((2**15)-1) * x) ## Signed 16-bit values
    return Struct('h').pack(i)

def decode(two_bytes):
    """Decode two bytes signed 16-bit value as [-1,1] float"""
    max_signed_16bit = (2**15)-1
    return Struct('h').unpack(two_bytes)[0] / ((2**15)-1.0)

def play(sampler, name='song.wav', seconds=2):
    """Write the output of a sampler function as a wav file.
    (See https://docs.python.org/3/library/wave.html)
    """
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()

def open_close(mapper, in_name = 'in.wav', out_name='out.wav'):
    """Read input wav file, process it through mapper, 
    write the output as a new wav file.
    """
    inp = open(in_name, 'rb')
    #print("channels  = "+str(inp.getnchannels()))
    #print("sampwidth = "+str(inp.getsampwidth()))
    #print("frame rate= "+str(inp.getframerate()))
    #print("frames    = "+str(inp.getnframes()))
    this_framerate = inp.getframerate()
    nframes = inp.getnframes()
    b = inp.readframes(nframes)
    L=[]
    for i in range(0,nframes*2,2):
        L.append(decode(b[i:i+2]))
    inp.close()

    out = open(out_name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(this_framerate)
    everyother = False
    for sample in L:  ### If L, normal order. If L[::-1], reversed
        """
        ### If this is the body of the for, it's every other
        ### sample, so it sounds "sped up", double frequency
        if everyother:
            out.writeframes(encode(mapper(sample)))
        everyother = not everyother
        """
        """
        ### If this is the body of the for, it doubles every sample
        ### so it sounds "slowed down", half frequency
        out.writeframes(encode(mapper(sample)))
        out.writeframes(encode(mapper(sample)))
        """
        out.writeframes(encode(mapper(sample)))
    out.close()
    
### Write in.wav to out.wav in which every sample is passed
### through the lambda function below. Why doesn't it change
### if the function is "lambda sample: -sample" ?
open_close(lambda sample: sample/4)

def tri(frequency, amplitude=0.3):
    """A continuous triangle wave."""
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

#play(tri(e_freq))

def note(f, start, end, fade=.01):
    """Play f for a fixed duration."""
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler

#play(note(tri(e_freq), 1, 1.5))

def both(f, g):
    return lambda t: f(t) + g(t)

c = tri(c_freq)
e = tri(e_freq)
g = tri(g_freq)
low_g = tri(g_freq / 2)

#play(both(note(e, 0, 1/8), note(low_g, 1/8, 3/8)))

#play(both(note(c, 0, 1), both(note(e, 0, 1), note(g, 0, 1))))

def mario(c, e, g, low_g):
    z = 0
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/4))
    return song

def mario_at(octave):
    c = tri(octave * c_freq)
    e = tri(octave * e_freq)
    g = tri(octave * g_freq)
    low_g = tri(octave * g_freq / 2)
    return mario(c, e, g, low_g)

#play(both(mario_at(1), mario_at(1/2)))



        




