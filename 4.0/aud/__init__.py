import sys
import typing

GenericType = typing.TypeVar("GenericType")


class Device:
    ''' Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.
    '''

    channels = None
    ''' The channel count of the device.'''

    distance_model = None
    ''' The distance model of the device.'''

    doppler_factor = None
    ''' The doppler factor of the device. This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity.'''

    format = None
    ''' The native sample format of the device.'''

    listener_location = None
    ''' The listeners's location in 3D space, a 3D tuple of floats.'''

    listener_orientation = None
    ''' The listener's orientation in 3D space as quaternion, a 4 float tuple.'''

    listener_velocity = None
    ''' The listener's velocity in 3D space, a 3D tuple of floats.'''

    rate = None
    ''' The sampling rate of the device in Hz.'''

    speed_of_sound = None
    ''' The speed of sound of the device. The speed of sound in air is typically 343.3 m/s.'''

    volume = None
    ''' The overall volume of the device.'''

    def lock(self):
        ''' Locks the device so that it's guaranteed, that no samples are read from the streams until :meth:`unlock` is called. This is useful if you want to do start/stop/pause/resume some sounds at the same time.

        '''
        pass

    def play(self, sound: 'Sound', keep: bool = False) -> 'Handle':
        ''' Plays a sound.

        :param sound: The sound to play.
        :type sound: 'Sound'
        :param keep: `Handle.keep`.
        :type keep: bool
        :rtype: 'Handle'
        :return: The playback handle with which playback can be controlled with.
        '''
        pass

    def stopAll(self):
        ''' Stops all playing and paused sounds.

        '''
        pass

    def unlock(self):
        ''' Unlocks the device after a lock call, see :meth:`lock` for details.

        '''
        pass


class DynamicMusic:
    ''' The DynamicMusic object allows to play music depending on a current scene, scene changes are managed by the class, with the possibility of custom transitions. The default transition is a crossfade effect, and the default scene is silent and has id 0
    '''

    fadeTime = None
    ''' The length in seconds of the crossfade transition'''

    position = None
    ''' The playback position of the scene in seconds.'''

    scene = None
    ''' The current scene'''

    status = None
    ''' Whether the scene is playing, paused or stopped (=invalid).'''

    volume = None
    ''' The volume of the scene.'''

    def addScene(self, scene: 'Sound') -> int:
        ''' Adds a new scene.

        :param scene: The scene sound.
        :type scene: 'Sound'
        :rtype: int
        :return: The new scene id.
        '''
        pass

    def addTransition(self, ini: int, end: int, transition: 'Sound') -> bool:
        ''' Adds a new scene.

        :param ini: the initial scene foor the transition.
        :type ini: int
        :param end: The final scene for the transition.
        :type end: int
        :param transition: The transition sound.
        :type transition: 'Sound'
        :rtype: bool
        :return: false if the ini or end scenes don't exist, true othrwise.
        '''
        pass

    def pause(self) -> bool:
        ''' Pauses playback of the scene.

        :rtype: bool
        :return: Whether the action succeeded.
        '''
        pass

    def resume(self) -> bool:
        ''' Resumes playback of the scene.

        :rtype: bool
        :return: Whether the action succeeded.
        '''
        pass

    def stop(self) -> bool:
        ''' Stops playback of the scene.

        :rtype: bool
        :return: Whether the action succeeded.
        '''
        pass


class HRTF:
    ''' An HRTF object represents a set of head related transfer functions as impulse responses. It's used for binaural sound
    '''

    def loadLeftHrtfSet(self, extension: str, directory: typing.Any) -> 'HRTF':
        ''' Loads all HRTFs from a directory.

        :param extension: The file extension of the hrtfs.
        :type extension: str
        :param extension: The file extension of the hrtfs.
        :type extension: str
        :param directory:  The path to where the HRTF files are located.
        :type directory: typing.Any
        :rtype: 'HRTF'
        :return: `HRTF` object.
        '''
        pass

    def loadLeftHrtfSet(self, extension: str, directory: typing.Any) -> 'HRTF':
        ''' Loads all HRTFs from a directory.

        :param extension: The file extension of the hrtfs.
        :type extension: str
        :param extension: The file extension of the hrtfs.
        :type extension: str
        :param directory:  The path to where the HRTF files are located.
        :type directory: typing.Any
        :rtype: 'HRTF'
        :return: `HRTF` object.
        '''
        pass

    def addImpulseResponseFromSound(self, sound: 'Sound', azimuth: float,
                                    elevation: float) -> bool:
        ''' Adds a new hrtf to the HRTF object

        :param sound: The sound that contains the hrtf.
        :type sound: 'Sound'
        :param azimuth: The azimuth angle of the hrtf.
        :type azimuth: float
        :param elevation: The elevation angle of the hrtf.
        :type elevation: float
        :rtype: bool
        :return: Whether the action succeeded.
        '''
        pass


class Handle:
    ''' Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.
    '''

    attenuation = None
    ''' This factor is used for distance based attenuation of the source.'''

    cone_angle_inner = None
    ''' The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the :attr:`location` of the source and with infinite height, heading in the direction of the source's :attr:`orientation`. In the inner cone the volume is normal. Outside the outer cone the volume will be :attr:`cone_volume_outer` and in the area between the volume will be interpolated linearly.'''

    cone_angle_outer = None
    ''' The opening angle of the outer cone of the source.'''

    cone_volume_outer = None
    ''' The volume outside the outer cone of the source.'''

    distance_maximum = None
    ''' The maximum distance of the source. If the listener is further away the source volume will be 0.'''

    distance_reference = None
    ''' The reference distance of the source. At this distance the volume will be exactly :attr:`volume`.'''

    keep = None
    ''' Whether the sound should be kept paused in the device when its end is reached. This can be used to seek the sound to some position and start playback again.'''

    location = None
    ''' The source's location in 3D space, a 3D tuple of floats.'''

    loop_count = None
    ''' The (remaining) loop count of the sound. A negative value indicates infinity.'''

    orientation = None
    ''' The source's orientation in 3D space as quaternion, a 4 float tuple.'''

    pitch = None
    ''' The pitch of the sound.'''

    position = None
    ''' The playback position of the sound in seconds.'''

    relative = None
    ''' Whether the source's location, velocity and orientation is relative or absolute to the listener.'''

    status = None
    ''' Whether the sound is playing, paused or stopped (=invalid).'''

    velocity = None
    ''' The source's velocity in 3D space, a 3D tuple of floats.'''

    volume = None
    ''' The volume of the sound.'''

    volume_maximum = None
    ''' The maximum volume of the source.'''

    volume_minimum = None
    ''' The minimum volume of the source.'''

    def pause(self) -> bool:
        ''' Pauses playback.

        :rtype: bool
        :return: Whether the action succeeded.
        '''
        pass

    def resume(self) -> bool:
        ''' Resumes playback.

        :rtype: bool
        :return: Whether the action succeeded.
        '''
        pass

    def stop(self) -> bool:
        ''' Stops playback.

        :rtype: bool
        :return: Whether the action succeeded.
        '''
        pass


class ImpulseResponse:
    ''' An ImpulseResponse object represents a filter with which to convolve a sound.
    '''

    pass


class PlaybackManager:
    ''' A PlabackManager object allows to easily control groups os sounds organized in categories.
    '''

    def addCategory(self, volume: float) -> int:
        ''' Adds a category with a custom volume.

        :param volume: The volume for ther new category.
        :type volume: float
        :rtype: int
        :return: The key of the new category.
        '''
        pass

    def clean(self):
        ''' Cleans all the invalid and finished sound from the playback manager.

        '''
        pass

    def getVolume(self, catKey: int) -> float:
        ''' Retrieves the volume of a category.

        :param catKey: the key of the category.
        :type catKey: int
        :rtype: float
        :return: The volume of the cateogry.
        '''
        pass

    def pause(self, catKey: int) -> bool:
        ''' Pauses playback of the category.

        :param catKey: the key of the category.
        :type catKey: int
        :rtype: bool
        :return: Whether the action succeeded.
        '''
        pass

    def play(self, sound: 'Sound', catKey: int) -> 'Handle':
        ''' Plays a sound through the playback manager and assigns it to a category.

        :param sound: The sound to play.
        :type sound: 'Sound'
        :param catKey: the key of the category in which the sound will be added, if it doesn't exist, a new one will be created.
        :type catKey: int
        :rtype: 'Handle'
        :return: The playback handle with which playback can be controlled with.
        '''
        pass

    def resume(self, catKey: int) -> bool:
        ''' Resumes playback of the catgory.

        :param catKey: the key of the category.
        :type catKey: int
        :rtype: bool
        :return: Whether the action succeeded.
        '''
        pass

    def setVolume(self, volume: float, catKey: int) -> int:
        ''' Changes the volume of a category.

        :param volume: the new volume value.
        :type volume: float
        :param catKey: the key of the category.
        :type catKey: int
        :rtype: int
        :return: Whether the action succeeded.
        '''
        pass

    def stop(self, catKey: int) -> bool:
        ''' Stops playback of the category.

        :param catKey: the key of the category.
        :type catKey: int
        :rtype: bool
        :return: Whether the action succeeded.
        '''
        pass


class Sequence:
    ''' This sound represents sequenced entries to play a sound sequence.
    '''

    channels = None
    ''' The channel count of the sequence.'''

    distance_model = None
    ''' The distance model of the sequence.'''

    doppler_factor = None
    ''' The doppler factor of the sequence. This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity.'''

    fps = None
    ''' The listeners's location in 3D space, a 3D tuple of floats.'''

    muted = None
    ''' Whether the whole sequence is muted.'''

    rate = None
    ''' The sampling rate of the sequence in Hz.'''

    speed_of_sound = None
    ''' The speed of sound of the sequence. The speed of sound in air is typically 343.3 m/s.'''

    def add(self) -> 'SequenceEntry':
        ''' Adds a new entry to the sequence.

        :param sound: The sound this entry should play.
        :type sound: 'Sound'
        :param begin: The start time.
        :type begin: float
        :param end: The end time or a negative value if determined by the sound.
        :type end: float
        :param skip: How much seconds should be skipped at the beginning.
        :type skip: float
        :rtype: 'SequenceEntry'
        :return: The entry added.
        '''
        pass

    def remove(self):
        ''' Removes an entry from the sequence.

        :param entry: The entry to remove.
        :type entry: 'SequenceEntry'
        '''
        pass

    def setAnimationData(self):
        ''' Writes animation data to a sequence.

        :param type: The type of animation data.
        :type type: int
        :param frame: The frame this data is for.
        :type frame: int
        :param data: The data to write.
        :type data: typing.List[float]
        :param animated: Whether the attribute is animated.
        :type animated: bool
        '''
        pass


class SequenceEntry:
    ''' SequenceEntry objects represent an entry of a sequenced sound.
    '''

    attenuation = None
    ''' This factor is used for distance based attenuation of the source.'''

    cone_angle_inner = None
    ''' The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the :attr:`location` of the source and with infinite height, heading in the direction of the source's :attr:`orientation`. In the inner cone the volume is normal. Outside the outer cone the volume will be :attr:`cone_volume_outer` and in the area between the volume will be interpolated linearly.'''

    cone_angle_outer = None
    ''' The opening angle of the outer cone of the source.'''

    cone_volume_outer = None
    ''' The volume outside the outer cone of the source.'''

    distance_maximum = None
    ''' The maximum distance of the source. If the listener is further away the source volume will be 0.'''

    distance_reference = None
    ''' The reference distance of the source. At this distance the volume will be exactly :attr:`volume`.'''

    muted = None
    ''' Whether the entry is muted.'''

    relative = None
    ''' Whether the source's location, velocity and orientation is relative or absolute to the listener.'''

    sound = None
    ''' The sound the entry is representing and will be played in the sequence.'''

    volume_maximum = None
    ''' The maximum volume of the source.'''

    volume_minimum = None
    ''' The minimum volume of the source.'''

    def move(self):
        ''' Moves the entry.

        :param begin: The new start time.
        :type begin: float
        :param end: The new end time or a negative value if unknown.
        :type end: float
        :param skip: How many seconds to skip at the beginning.
        :type skip: float
        '''
        pass

    def setAnimationData(self):
        ''' Writes animation data to a sequenced entry.

        :param type: The type of animation data.
        :type type: int
        :param frame: The frame this data is for.
        :type frame: int
        :param data: The data to write.
        :type data: typing.List[float]
        :param animated: Whether the attribute is animated.
        :type animated: bool
        '''
        pass


class Sound:
    ''' Sound objects are immutable and represent a sound that can be played simultaneously multiple times. They are called factories because they create reader objects internally that are used for playback.
    '''

    length = None
    ''' The sample specification of the sound as a tuple with rate and channel count.'''

    specs = None
    ''' The sample specification of the sound as a tuple with rate and channel count.'''

    @classmethod
    def buffer(cls, data: typing.Any, rate: float) -> 'Sound':
        ''' Creates a sound from a data buffer.

        :param data: The data as two dimensional numpy array.
        :type data: typing.Any
        :param rate: The sample rate.
        :type rate: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    @classmethod
    def file(cls, filename: str) -> 'Sound':
        ''' Creates a sound object of a sound file.

        :param filename: Path of the file.
        :type filename: str
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    @classmethod
    def list(cls) -> 'Sound':
        ''' Creates an empty sound list that can contain several sounds.

        :param random: whether the playback will be random or not.
        :type random: int
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    @classmethod
    def sawtooth(cls, frequency: float, rate: int = 48000) -> 'Sound':
        ''' Creates a sawtooth sound which plays a sawtooth wave.

        :param frequency: The frequency of the sawtooth wave in Hz.
        :type frequency: float
        :param rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping.
        :type rate: int
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    @classmethod
    def silence(cls, rate: int = 48000) -> 'Sound':
        ''' Creates a silence sound which plays simple silence.

        :param rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping.
        :type rate: int
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    @classmethod
    def sine(cls, frequency: float, rate: int = 48000) -> 'Sound':
        ''' Creates a sine sound which plays a sine wave.

        :param frequency: The frequency of the sine wave in Hz.
        :type frequency: float
        :param rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping.
        :type rate: int
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    @classmethod
    def square(cls, frequency: float, rate: int = 48000) -> 'Sound':
        ''' Creates a square sound which plays a square wave.

        :param frequency: The frequency of the square wave in Hz.
        :type frequency: float
        :param rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping.
        :type rate: int
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    @classmethod
    def triangle(cls, frequency: float, rate: int = 48000) -> 'Sound':
        ''' Creates a triangle sound which plays a triangle wave.

        :param frequency: The frequency of the triangle wave in Hz.
        :type frequency: float
        :param rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping.
        :type rate: int
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def ADSR(self, attack: float, decay: float, sustain: float,
             release: float) -> 'Sound':
        ''' Attack-Decay-Sustain-Release envelopes the volume of a sound. Note: there is currently no way to trigger the release with this API.

        :param attack: The attack time in seconds.
        :type attack: float
        :param decay: The decay time in seconds.
        :type decay: float
        :param sustain: The sustain level.
        :type sustain: float
        :param release: The release level.
        :type release: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def accumulate(self, additive: typing.Any = False) -> 'Sound':
        ''' Accumulates a sound by summing over positive input differences thus generating a monotonic sigal. If additivity is set to true negative input differences get added too, but positive ones with a factor of two. Note that with additivity the signal is not monotonic anymore.

        :param time: 
        :type time: bool
        :param additive:  Whether the accumulation should be additive or not.
        :type additive: typing.Any
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def addSound(self, sound: 'Sound'):
        ''' Adds a new sound to a sound list.

        :param sound: The sound that will be added to the list.
        :type sound: 'Sound'
        '''
        pass

    def binaural(self) -> 'Sound':
        ''' Creates a binaural sound using another sound as source. The original sound must be mono

        :param hrtf: 
        :type hrtf: 'HRTF'
        :param source: An object representing the source position of the sound.
        :type source: 'Source'
        :param threadPool: A thread pool used to parallelize convolution.
        :type threadPool: 'ThreadPool'
        :param hrtfs:  An HRTF set.
        :type hrtfs: typing.Any
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def cache(self) -> 'Sound':
        ''' Caches a sound into RAM. This saves CPU usage needed for decoding and file access if the underlying sound reads from a file on the harddisk, but it consumes a lot of memory.

        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def convolver(self) -> 'Sound':
        ''' Creates a sound that will apply convolution to another sound.

        :param impulseResponse: The filter with which convolve the sound.
        :type impulseResponse: 'ImpulseResponse'
        :param threadPool: A thread pool used to parallelize convolution.
        :type threadPool: 'ThreadPool'
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def data(self) -> typing.Any:
        ''' Retrieves the data of the sound as numpy array.

        :rtype: typing.Any
        :return: A two dimensional numpy float array.
        '''
        pass

    def delay(self, time: float) -> 'Sound':
        ''' Delays by playing adding silence in front of the other sound's data.

        :param time: How many seconds of silence should be added before the sound.
        :type time: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def envelope(self, attack: float, release: float, threshold: float,
                 arthreshold: float) -> 'Sound':
        ''' Delays by playing adding silence in front of the other sound's data.

        :param attack: The attack factor.
        :type attack: float
        :param release: The release factor.
        :type release: float
        :param threshold: The general threshold value.
        :type threshold: float
        :param arthreshold: The attack/release threshold value.
        :type arthreshold: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def fadein(self, start: float, length: float) -> 'Sound':
        ''' Fades a sound in by raising the volume linearly in the given time interval.

        :param start: Time in seconds when the fading should start.
        :type start: float
        :param length: Time in seconds how long the fading should last.
        :type length: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def fadeout(self, start: float, length: float) -> 'Sound':
        ''' Fades a sound in by lowering the volume linearly in the given time interval.

        :param start: Time in seconds when the fading should start.
        :type start: float
        :param length: Time in seconds how long the fading should last.
        :type length: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def filter(self, b: typing.List[float], a=(1)) -> 'Sound':
        ''' Filters a sound with the supplied IIR filter coefficients. Without the second parameter you'll get a FIR filter. If the first value of the a sequence is 0, it will be set to 1 automatically. If the first value of the a sequence is neither 0 nor 1, all filter coefficients will be scaled by this value so that it is 1 in the end, you don't have to scale yourself.

        :param b: The nominator filter coefficients.
        :type b: typing.List[float]
        :param a: The denominator filter coefficients.
        :type a: typing.List[float]
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def highpass(self, frequency: float, Q: float = 0.5) -> 'Sound':
        ''' Creates a second order highpass filter based on the transfer function :math:`H(s) = s^2 / (s^2 + s/Q + 1)`

        :param frequency: The cut off trequency of the highpass.
        :type frequency: float
        :param Q: Q factor of the lowpass.
        :type Q: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def join(self, sound: 'Sound') -> 'Sound':
        ''' Plays two factories in sequence.

        :param sound: The sound to play second.
        :type sound: 'Sound'
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def limit(self, start: float, end: float) -> 'Sound':
        ''' Limits a sound within a specific start and end time.

        :param start: Start time in seconds.
        :type start: float
        :param end: End time in seconds.
        :type end: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def loop(self, count: typing.Any) -> 'Sound':
        ''' Loops a sound.

        :param count: How often the sound should be looped. Negative values mean endlessly.
        :type count: typing.Any
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def lowpass(self, frequency: float, Q: float = 0.5) -> 'Sound':
        ''' Creates a second order lowpass filter based on the transfer function :math:`H(s) = 1 / (s^2 + s/Q + 1)`

        :param frequency: The cut off trequency of the lowpass.
        :type frequency: float
        :param Q: Q factor of the lowpass.
        :type Q: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def mix(self, sound: 'Sound') -> 'Sound':
        ''' Mixes two factories.

        :param sound: The sound to mix over the other.
        :type sound: 'Sound'
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def modulate(self, sound: 'Sound') -> 'Sound':
        ''' Modulates two factories.

        :param sound: The sound to modulate over the other.
        :type sound: 'Sound'
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def mutable(self) -> 'Sound':
        ''' Creates a sound that will be restarted when sought backwards. If the original sound is a sound list, the playing sound can change.

        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def pingpong(self) -> 'Sound':
        ''' Plays a sound forward and then backward. This is like joining a sound with its reverse.

        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def pitch(self, factor: float) -> 'Sound':
        ''' Changes the pitch of a sound with a specific factor.

        :param factor: The factor to change the pitch with.
        :type factor: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def rechannel(self, channels: int) -> 'Sound':
        ''' Rechannels the sound.

        :param channels: The new channel configuration.
        :type channels: int
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def resample(self, rate: float, high_quality: bool) -> 'Sound':
        ''' Resamples the sound.

        :param rate: The new sample rate.
        :type rate: float
        :param high_quality: When true use a higher quality but slower resampler.
        :type high_quality: bool
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def reverse(self) -> 'Sound':
        ''' Plays a sound reversed.

        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def sum(self) -> 'Sound':
        ''' Sums the samples of a sound.

        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def threshold(self, threshold=' 0') -> 'Sound':
        ''' Makes a threshold wave out of an audio wave by setting all samples with a amplitude >= threshold to 1, all <= -threshold to -1 and all between to 0.

        :param threshold: Threshold value over which an amplitude counts non-zero.
        :type threshold: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def volume(self, volume: float) -> 'Sound':
        ''' Changes the volume of a sound.

        :param volume: The new volume..
        :type volume: float
        :rtype: 'Sound'
        :return: `Sound` object.
        '''
        pass

    def write(self, filename: str, rate: int, channels: int, format: int,
              container: int, codec: int, bitrate: int, buffersize: int):
        ''' Writes the sound to a file.

        :param filename: The path to write to.
        :type filename: str
        :param rate: The sample rate to write with.
        :type rate: int
        :param channels: The number of channels to write with.
        :type channels: int
        :param format: The sample format to write with.
        :type format: int
        :param container: The container format for the file.
        :type container: int
        :param codec: The codec to use in the file.
        :type codec: int
        :param bitrate: The bitrate to write with.
        :type bitrate: int
        :param buffersize: The size of the writing buffer.
        :type buffersize: int
        '''
        pass


class Source:
    ''' The source object represents the source position of a binaural sound.
    '''

    azimuth = None
    ''' The azimuth angle.'''

    distance = None
    ''' The distance value. 0 is min, 1 is max.'''

    elevation = None
    ''' The elevation angle.'''


class ThreadPool:
    ''' A ThreadPool is used to parallelize convolution efficiently.
    '''

    pass


class error:
    pass


AP_LOCATION = None
''' Constant value 3
'''

AP_ORIENTATION = None
''' Constant value 4
'''

AP_PANNING = None
''' Constant value 1
'''

AP_PITCH = None
''' Constant value 2
'''

AP_VOLUME = None
''' Constant value 0
'''

CHANNELS_INVALID = None
''' Constant value 0
'''

CHANNELS_MONO = None
''' Constant value 1
'''

CHANNELS_STEREO = None
''' Constant value 2
'''

CHANNELS_STEREO_LFE = None
''' Constant value 3
'''

CHANNELS_SURROUND4 = None
''' Constant value 4
'''

CHANNELS_SURROUND5 = None
''' Constant value 5
'''

CHANNELS_SURROUND51 = None
''' Constant value 6
'''

CHANNELS_SURROUND61 = None
''' Constant value 7
'''

CHANNELS_SURROUND71 = None
''' Constant value 8
'''

CODEC_AAC = None
''' Constant value 1
'''

CODEC_AC3 = None
''' Constant value 2
'''

CODEC_FLAC = None
''' Constant value 3
'''

CODEC_INVALID = None
''' Constant value 0
'''

CODEC_MP2 = None
''' Constant value 4
'''

CODEC_MP3 = None
''' Constant value 5
'''

CODEC_OPUS = None
''' Constant value 8
'''

CODEC_PCM = None
''' Constant value 6
'''

CODEC_VORBIS = None
''' Constant value 7
'''

CONTAINER_AC3 = None
''' Constant value 1
'''

CONTAINER_FLAC = None
''' Constant value 2
'''

CONTAINER_INVALID = None
''' Constant value 0
'''

CONTAINER_MATROSKA = None
''' Constant value 3
'''

CONTAINER_MP2 = None
''' Constant value 4
'''

CONTAINER_MP3 = None
''' Constant value 5
'''

CONTAINER_OGG = None
''' Constant value 6
'''

CONTAINER_WAV = None
''' Constant value 7
'''

DISTANCE_MODEL_EXPONENT = None
''' Constant value 5
'''

DISTANCE_MODEL_EXPONENT_CLAMPED = None
''' Constant value 6
'''

DISTANCE_MODEL_INVALID = None
''' Constant value 0
'''

DISTANCE_MODEL_INVERSE = None
''' Constant value 1
'''

DISTANCE_MODEL_INVERSE_CLAMPED = None
''' Constant value 2
'''

DISTANCE_MODEL_LINEAR = None
''' Constant value 3
'''

DISTANCE_MODEL_LINEAR_CLAMPED = None
''' Constant value 4
'''

FORMAT_FLOAT32 = None
''' Constant value 36
'''

FORMAT_FLOAT64 = None
''' Constant value 40
'''

FORMAT_INVALID = None
''' Constant value 0
'''

FORMAT_S16 = None
''' Constant value 18
'''

FORMAT_S24 = None
''' Constant value 19
'''

FORMAT_S32 = None
''' Constant value 20
'''

FORMAT_U8 = None
''' Constant value 1
'''

RATE_11025 = None
''' Constant value 11025
'''

RATE_16000 = None
''' Constant value 16000
'''

RATE_192000 = None
''' Constant value 192000
'''

RATE_22050 = None
''' Constant value 22050
'''

RATE_32000 = None
''' Constant value 32000
'''

RATE_44100 = None
''' Constant value 44100
'''

RATE_48000 = None
''' Constant value 48000
'''

RATE_8000 = None
''' Constant value 8000
'''

RATE_88200 = None
''' Constant value 88200
'''

RATE_96000 = None
''' Constant value 96000
'''

RATE_INVALID = None
''' Constant value 0
'''

STATUS_INVALID = None
''' Constant value 0
'''

STATUS_PAUSED = None
''' Constant value 2
'''

STATUS_PLAYING = None
''' Constant value 1
'''

STATUS_STOPPED = None
''' Constant value 3
'''
