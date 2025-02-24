"""
Audaspace (pronounced "outer space") is a high level audio library.


--------------------

This script shows how to use the classes: Device, Sound and
Handle.

```../examples/aud.py```

"""

import typing
import collections.abc
import typing_extensions

class Device:
    """Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output."""

    channels: typing.Any
    """ The channel count of the device."""

    distance_model: typing.Any
    """ The distance model of the device.`OpenAL Documentation <https://www.openal.org/documentation/>`__"""

    doppler_factor: typing.Any
    """ The doppler factor of the device.
This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity."""

    format: typing.Any
    """ The native sample format of the device."""

    listener_location: typing.Any
    """ The listeners's location in 3D space, a 3D tuple of floats."""

    listener_orientation: typing.Any
    """ The listener's orientation in 3D space as quaternion, a 4 float tuple."""

    listener_velocity: typing.Any
    """ The listener's velocity in 3D space, a 3D tuple of floats."""

    rate: typing.Any
    """ The sampling rate of the device in Hz."""

    speed_of_sound: typing.Any
    """ The speed of sound of the device.
The speed of sound in air is typically 343.3 m/s."""

    volume: typing.Any
    """ The overall volume of the device."""

    def lock(self):
        """Locks the device so that it's guaranteed, that no samples are
        read from the streams until `unlock` is called.
        This is useful if you want to do start/stop/pause/resume some
        sounds at the same time.

        """

    def play(self, sound: Sound, keep: bool = False) -> Handle:
        """Plays a sound.

                :param sound: The sound to play.
                :type sound: Sound
                :param keep: See `Handle.keep`.
                :type keep: bool
                :return: The playback handle with which playback can be
        controlled with.
                :rtype: Handle
        """

    def stopAll(self):
        """Stops all playing and paused sounds."""

    def unlock(self):
        """Unlocks the device after a lock call, see `lock` for
        details.

        """

class DynamicMusic:
    """The DynamicMusic object allows to play music depending on a current scene, scene changes are managed by the class, with the possibility of custom transitions.
    The default transition is a crossfade effect, and the default scene is silent and has id 0
    """

    fadeTime: typing.Any
    """ The length in seconds of the crossfade transition"""

    position: typing.Any
    """ The playback position of the scene in seconds."""

    scene: typing.Any
    """ The current scene"""

    status: typing.Any
    """ Whether the scene is playing, paused or stopped (=invalid)."""

    volume: typing.Any
    """ The volume of the scene."""

    def addScene(self, scene: Sound) -> int:
        """Adds a new scene.

        :param scene: The scene sound.
        :type scene: Sound
        :return: The new scene id.
        :rtype: int
        """

    def addTransition(self, ini: int, end: int, transition: Sound) -> bool:
        """Adds a new scene.

        :param ini: the initial scene foor the transition.
        :type ini: int
        :param end: The final scene for the transition.
        :type end: int
        :param transition: The transition sound.
        :type transition: Sound
        :return: false if the ini or end scenes don't exist, true othrwise.
        :rtype: bool
        """

    def pause(self) -> bool:
        """Pauses playback of the scene.

        :return: Whether the action succeeded.
        :rtype: bool
        """

    def resume(self) -> bool:
        """Resumes playback of the scene.

        :return: Whether the action succeeded.
        :rtype: bool
        """

    def stop(self) -> bool:
        """Stops playback of the scene.

        :return: Whether the action succeeded.
        :rtype: bool
        """

class HRTF:
    """An HRTF object represents a set of head related transfer functions as impulse responses. It's used for binaural sound"""

    def loadLeftHrtfSet(self, extension: str, directory) -> typing_extensions.Self:
        """Loads all HRTFs from a directory.

        :param extension: The file extension of the hrtfs.
        :type extension: str
        :param directory: The path to where the HRTF files are located.
        :return: The loaded `HRTF` object.
        :rtype: typing_extensions.Self
        """

    def loadRightHrtfSet(self, extension: str, directory) -> typing_extensions.Self:
        """Loads all HRTFs from a directory.

        :param extension: The file extension of the hrtfs.
        :type extension: str
        :param directory: The path to where the HRTF files are located.
        :return: The loaded `HRTF` object.
        :rtype: typing_extensions.Self
        """

    def addImpulseResponseFromSound(
        self, sound: Sound, azimuth: float, elevation: float
    ) -> bool:
        """Adds a new hrtf to the HRTF object

        :param sound: The sound that contains the hrtf.
        :type sound: Sound
        :param azimuth: The azimuth angle of the hrtf.
        :type azimuth: float
        :param elevation: The elevation angle of the hrtf.
        :type elevation: float
        :return: Whether the action succeeded.
        :rtype: bool
        """

class Handle:
    """Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles."""

    attenuation: typing.Any
    """ This factor is used for distance based attenuation of the source.:attr:`Device.distance_model`"""

    cone_angle_inner: typing.Any
    """ The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the `location` of the source and with infinite height, heading in the direction of the source's `orientation`.
In the inner cone the volume is normal. Outside the outer cone the volume will be `cone_volume_outer` and in the area between the volume will be interpolated linearly."""

    cone_angle_outer: typing.Any
    """ The opening angle of the outer cone of the source.:attr:`cone_angle_inner`"""

    cone_volume_outer: typing.Any
    """ The volume outside the outer cone of the source.:attr:`cone_angle_inner`"""

    distance_maximum: typing.Any
    """ The maximum distance of the source.
If the listener is further away the source volume will be 0.:attr:`Device.distance_model`"""

    distance_reference: typing.Any
    """ The reference distance of the source.
At this distance the volume will be exactly `volume`.:attr:`Device.distance_model`"""

    keep: typing.Any
    """ Whether the sound should be kept paused in the device when its end is reached.
This can be used to seek the sound to some position and start playback again."""

    location: typing.Any
    """ The source's location in 3D space, a 3D tuple of floats."""

    loop_count: typing.Any
    """ The (remaining) loop count of the sound. A negative value indicates infinity."""

    orientation: typing.Any
    """ The source's orientation in 3D space as quaternion, a 4 float tuple."""

    pitch: typing.Any
    """ The pitch of the sound."""

    position: typing.Any
    """ The playback position of the sound in seconds."""

    relative: typing.Any
    """ Whether the source's location, velocity and orientation is relative or absolute to the listener."""

    status: typing.Any
    """ Whether the sound is playing, paused or stopped (=invalid)."""

    velocity: typing.Any
    """ The source's velocity in 3D space, a 3D tuple of floats."""

    volume: typing.Any
    """ The volume of the sound."""

    volume_maximum: typing.Any
    """ The maximum volume of the source.:attr:`Device.distance_model`"""

    volume_minimum: typing.Any
    """ The minimum volume of the source.:attr:`Device.distance_model`"""

    def pause(self) -> bool:
        """Pauses playback.

        :return: Whether the action succeeded.
        :rtype: bool
        """

    def resume(self) -> bool:
        """Resumes playback.

        :return: Whether the action succeeded.
        :rtype: bool
        """

    def stop(self) -> bool:
        """Stops playback.

        :return: Whether the action succeeded.
        :rtype: bool
        """

class ImpulseResponse:
    """An ImpulseResponse object represents a filter with which to convolve a sound."""

class PlaybackManager:
    """A PlabackManager object allows to easily control groups os sounds organized in categories."""

    def addCategory(self, volume: float) -> int:
        """Adds a category with a custom volume.

        :param volume: The volume for ther new category.
        :type volume: float
        :return: The key of the new category.
        :rtype: int
        """

    def clean(self):
        """Cleans all the invalid and finished sound from the playback manager."""

    def getVolume(self, catKey: int) -> float:
        """Retrieves the volume of a category.

        :param catKey: the key of the category.
        :type catKey: int
        :return: The volume of the cateogry.
        :rtype: float
        """

    def pause(self, catKey: int) -> bool:
        """Pauses playback of the category.

        :param catKey: the key of the category.
        :type catKey: int
        :return: Whether the action succeeded.
        :rtype: bool
        """

    def play(self, sound: Sound, catKey: int) -> Handle:
        """Plays a sound through the playback manager and assigns it to a category.

                :param sound: The sound to play.
                :type sound: Sound
                :param catKey: the key of the category in which the sound will be added,
        if it doesn't exist, a new one will be created.
                :type catKey: int
                :return: The playback handle with which playback can be controlled with.
                :rtype: Handle
        """

    def resume(self, catKey: int) -> bool:
        """Resumes playback of the catgory.

        :param catKey: the key of the category.
        :type catKey: int
        :return: Whether the action succeeded.
        :rtype: bool
        """

    def setVolume(self, volume: float, catKey: int) -> int:
        """Changes the volume of a category.

        :param volume: the new volume value.
        :type volume: float
        :param catKey: the key of the category.
        :type catKey: int
        :return: Whether the action succeeded.
        :rtype: int
        """

    def stop(self, catKey: int) -> bool:
        """Stops playback of the category.

        :param catKey: the key of the category.
        :type catKey: int
        :return: Whether the action succeeded.
        :rtype: bool
        """

class Sequence:
    """This sound represents sequenced entries to play a sound sequence."""

    channels: typing.Any
    """ The channel count of the sequence."""

    distance_model: typing.Any
    """ The distance model of the sequence.`OpenAL Documentation <https://www.openal.org/documentation/>`__"""

    doppler_factor: typing.Any
    """ The doppler factor of the sequence.
This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity."""

    fps: typing.Any
    """ The listeners's location in 3D space, a 3D tuple of floats."""

    muted: typing.Any
    """ Whether the whole sequence is muted."""

    rate: typing.Any
    """ The sampling rate of the sequence in Hz."""

    speed_of_sound: typing.Any
    """ The speed of sound of the sequence.
The speed of sound in air is typically 343.3 m/s."""

    def add(self) -> SequenceEntry:
        """Adds a new entry to the sequence.

        :return: The entry added.
        :rtype: SequenceEntry
        """

    def remove(self):
        """Removes an entry from the sequence."""

    def setAnimationData(self):
        """Writes animation data to a sequence."""

class SequenceEntry:
    """SequenceEntry objects represent an entry of a sequenced sound."""

    attenuation: typing.Any
    """ This factor is used for distance based attenuation of the source.:attr:`Device.distance_model`"""

    cone_angle_inner: typing.Any
    """ The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the `location` of the source and with infinite height, heading in the direction of the source's `orientation`.
In the inner cone the volume is normal. Outside the outer cone the volume will be `cone_volume_outer` and in the area between the volume will be interpolated linearly."""

    cone_angle_outer: typing.Any
    """ The opening angle of the outer cone of the source.:attr:`cone_angle_inner`"""

    cone_volume_outer: typing.Any
    """ The volume outside the outer cone of the source.:attr:`cone_angle_inner`"""

    distance_maximum: typing.Any
    """ The maximum distance of the source.
If the listener is further away the source volume will be 0.:attr:`Device.distance_model`"""

    distance_reference: typing.Any
    """ The reference distance of the source.
At this distance the volume will be exactly `volume`.:attr:`Device.distance_model`"""

    muted: typing.Any
    """ Whether the entry is muted."""

    relative: typing.Any
    """ Whether the source's location, velocity and orientation is relative or absolute to the listener."""

    sound: typing.Any
    """ The sound the entry is representing and will be played in the sequence."""

    volume_maximum: typing.Any
    """ The maximum volume of the source.:attr:`Device.distance_model`"""

    volume_minimum: typing.Any
    """ The minimum volume of the source.:attr:`Device.distance_model`"""

    def move(self):
        """Moves the entry."""

    def setAnimationData(self):
        """Writes animation data to a sequenced entry."""

class Sound:
    """Sound objects are immutable and represent a sound that can be played simultaneously multiple times. They are called factories because they create reader objects internally that are used for playback."""

    length: typing.Any
    """ The sample specification of the sound as a tuple with rate and channel count."""

    specs: typing.Any
    """ The sample specification of the sound as a tuple with rate and channel count."""

    @classmethod
    def buffer(cls, data, rate: float) -> typing_extensions.Self:
        """Creates a sound from a data buffer.

        :param data: The data as two dimensional numpy array.
        :param rate: The sample rate.
        :type rate: float
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    @classmethod
    def file(cls, filename: str) -> typing_extensions.Self:
        """Creates a sound object of a sound file.

        :param filename: Path of the file.
        :type filename: str
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    @classmethod
    def list(cls) -> typing_extensions.Self:
        """Creates an empty sound list that can contain several sounds.

        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    @classmethod
    def sawtooth(cls, frequency: float, rate: int = 48000) -> typing_extensions.Self:
        """Creates a sawtooth sound which plays a sawtooth wave.

                :param frequency: The frequency of the sawtooth wave in Hz.
                :type frequency: float
                :param rate: The sampling rate in Hz. It's recommended to set this
        value to the playback device's samling rate to avoid resamping.
                :type rate: int
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    @classmethod
    def silence(cls, rate: int = 48000) -> typing_extensions.Self:
        """Creates a silence sound which plays simple silence.

                :param rate: The sampling rate in Hz. It's recommended to set this
        value to the playback device's samling rate to avoid resamping.
                :type rate: int
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    @classmethod
    def sine(cls, frequency: float, rate: int = 48000) -> typing_extensions.Self:
        """Creates a sine sound which plays a sine wave.

                :param frequency: The frequency of the sine wave in Hz.
                :type frequency: float
                :param rate: The sampling rate in Hz. It's recommended to set this
        value to the playback device's samling rate to avoid resamping.
                :type rate: int
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    @classmethod
    def square(cls, frequency: float, rate: int = 48000) -> typing_extensions.Self:
        """Creates a square sound which plays a square wave.

                :param frequency: The frequency of the square wave in Hz.
                :type frequency: float
                :param rate: The sampling rate in Hz. It's recommended to set this
        value to the playback device's samling rate to avoid resamping.
                :type rate: int
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    @classmethod
    def triangle(cls, frequency: float, rate: int = 48000) -> typing_extensions.Self:
        """Creates a triangle sound which plays a triangle wave.

                :param frequency: The frequency of the triangle wave in Hz.
                :type frequency: float
                :param rate: The sampling rate in Hz. It's recommended to set this
        value to the playback device's samling rate to avoid resamping.
                :type rate: int
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def ADSR(
        self, attack: float, decay: float, sustain: float, release: float
    ) -> typing_extensions.Self:
        """Attack-Decay-Sustain-Release envelopes the volume of a sound.
        Note: there is currently no way to trigger the release with this API.

                :param attack: The attack time in seconds.
                :type attack: float
                :param decay: The decay time in seconds.
                :type decay: float
                :param sustain: The sustain level.
                :type sustain: float
                :param release: The release level.
                :type release: float
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def accumulate(self, additive=False) -> typing_extensions.Self:
        """Accumulates a sound by summing over positive input
        differences thus generating a monotonic sigal.
        If additivity is set to true negative input differences get added too,
        but positive ones with a factor of two.Note that with additivity the signal is not monotonic anymore.

                :param additive: Whether the accumulation should be additive or not.
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def addSound(self, sound: typing_extensions.Self):
        """Adds a new sound to a sound list.

        :param sound: The sound that will be added to the list.
        :type sound: typing_extensions.Self
        """

    def binaural(self) -> typing_extensions.Self:
        """Creates a binaural sound using another sound as source. The original sound must be mono

        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def cache(self) -> typing_extensions.Self:
        """Caches a sound into RAM.This saves CPU usage needed for decoding and file access if the
        underlying sound reads from a file on the harddisk,
        but it consumes a lot of memory.

                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def convolver(self) -> typing_extensions.Self:
        """Creates a sound that will apply convolution to another sound.

        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def data(self):
        """Retrieves the data of the sound as numpy array.

        :return: A two dimensional numpy float array.
        """

    def delay(self, time: float) -> typing_extensions.Self:
        """Delays by playing adding silence in front of the other sound's data.

        :param time: How many seconds of silence should be added before the sound.
        :type time: float
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def envelope(
        self, attack: float, release: float, threshold: float, arthreshold: float
    ) -> typing_extensions.Self:
        """Delays by playing adding silence in front of the other sound's data.

        :param attack: The attack factor.
        :type attack: float
        :param release: The release factor.
        :type release: float
        :param threshold: The general threshold value.
        :type threshold: float
        :param arthreshold: The attack/release threshold value.
        :type arthreshold: float
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def fadein(self, start: float, length: float) -> typing_extensions.Self:
        """Fades a sound in by raising the volume linearly in the given
        time interval.

                :param start: Time in seconds when the fading should start.
                :type start: float
                :param length: Time in seconds how long the fading should last.
                :type length: float
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def fadeout(self, start: float, length: float) -> typing_extensions.Self:
        """Fades a sound in by lowering the volume linearly in the given
        time interval.

                :param start: Time in seconds when the fading should start.
                :type start: float
                :param length: Time in seconds how long the fading should last.
                :type length: float
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def filter(self, b: list[float], a: list[float] = 1) -> typing_extensions.Self:
        """Filters a sound with the supplied IIR filter coefficients.
        Without the second parameter you'll get a FIR filter.If the first value of the a sequence is 0,
        it will be set to 1 automatically.
        If the first value of the a sequence is neither 0 nor 1, all
        filter coefficients will be scaled by this value so that it is 1
        in the end, you don't have to scale yourself.

                :param b: The nominator filter coefficients.
                :type b: list[float]
                :param a: The denominator filter coefficients.
                :type a: list[float]
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def highpass(self, frequency: float, Q: float = 0.5) -> typing_extensions.Self:
        """Creates a second order highpass filter based on the transfer
        function H(s) = s^2 / (s^2 + s/Q + 1)

                :param frequency: The cut off trequency of the highpass.
                :type frequency: float
                :param Q: Q factor of the lowpass.
                :type Q: float
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def join(self, sound: typing_extensions.Self) -> typing_extensions.Self:
        """Plays two factories in sequence.

        :param sound: The sound to play second.
        :type sound: typing_extensions.Self
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def limit(self, start: float, end: float) -> typing_extensions.Self:
        """Limits a sound within a specific start and end time.

        :param start: Start time in seconds.
        :type start: float
        :param end: End time in seconds.
        :type end: float
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def loop(self, count: int) -> typing_extensions.Self:
        """Loops a sound.

                :param count: How often the sound should be looped.
        Negative values mean endlessly.
                :type count: int
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def lowpass(self, frequency: float, Q: float = 0.5) -> typing_extensions.Self:
        """Creates a second order lowpass filter based on the transfer    function H(s) = 1 / (s^2 + s/Q + 1)

        :param frequency: The cut off trequency of the lowpass.
        :type frequency: float
        :param Q: Q factor of the lowpass.
        :type Q: float
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def mix(self, sound: typing_extensions.Self) -> typing_extensions.Self:
        """Mixes two factories.

        :param sound: The sound to mix over the other.
        :type sound: typing_extensions.Self
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def modulate(self, sound: typing_extensions.Self) -> typing_extensions.Self:
        """Modulates two factories.

        :param sound: The sound to modulate over the other.
        :type sound: typing_extensions.Self
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def mutable(self) -> typing_extensions.Self:
        """Creates a sound that will be restarted when sought backwards.
        If the original sound is a sound list, the playing sound can change.

                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def pingpong(self) -> typing_extensions.Self:
        """Plays a sound forward and then backward.
        This is like joining a sound with its reverse.

                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def pitch(self, factor: float) -> typing_extensions.Self:
        """Changes the pitch of a sound with a specific factor.

        :param factor: The factor to change the pitch with.
        :type factor: float
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def rechannel(self, channels: int) -> typing_extensions.Self:
        """Rechannels the sound.

        :param channels: The new channel configuration.
        :type channels: int
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def resample(self, rate: float, quality: int) -> typing_extensions.Self:
        """Resamples the sound.

        :param rate: The new sample rate.
        :type rate: float
        :param quality: Resampler performance vs quality choice (0=fastest, 3=slowest).
        :type quality: int
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def reverse(self) -> typing_extensions.Self:
        """Plays a sound reversed.

        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def sum(self) -> typing_extensions.Self:
        """Sums the samples of a sound.

        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def threshold(self, threshold: float = 0) -> typing_extensions.Self:
        """Makes a threshold wave out of an audio wave by setting all samples
        with a amplitude >= threshold to 1, all <= -threshold to -1 and
        all between to 0.

                :param threshold: Threshold value over which an amplitude counts
        non-zero.
                :type threshold: float
                :return: The created `Sound` object.
                :rtype: typing_extensions.Self
        """

    def volume(self, volume: float) -> typing_extensions.Self:
        """Changes the volume of a sound.

        :param volume: The new volume..
        :type volume: float
        :return: The created `Sound` object.
        :rtype: typing_extensions.Self
        """

    def write(
        self,
        filename: str,
        rate: int,
        channels: int,
        format: int,
        container: int,
        codec: int,
        bitrate: int,
        buffersize: int,
    ):
        """Writes the sound to a file.

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
        """

class Source:
    """The source object represents the source position of a binaural sound."""

    azimuth: typing.Any
    """ The azimuth angle."""

    distance: typing.Any
    """ The distance value. 0 is min, 1 is max."""

    elevation: typing.Any
    """ The elevation angle."""

class ThreadPool:
    """A ThreadPool is used to parallelize convolution efficiently."""

class error: ...

AP_LOCATION: typing.Any
""" Constant value 3
"""

AP_ORIENTATION: typing.Any
""" Constant value 4
"""

AP_PANNING: typing.Any
""" Constant value 1
"""

AP_PITCH: typing.Any
""" Constant value 2
"""

AP_VOLUME: typing.Any
""" Constant value 0
"""

CHANNELS_INVALID: typing.Any
""" Constant value 0
"""

CHANNELS_MONO: typing.Any
""" Constant value 1
"""

CHANNELS_STEREO: typing.Any
""" Constant value 2
"""

CHANNELS_STEREO_LFE: typing.Any
""" Constant value 3
"""

CHANNELS_SURROUND4: typing.Any
""" Constant value 4
"""

CHANNELS_SURROUND5: typing.Any
""" Constant value 5
"""

CHANNELS_SURROUND51: typing.Any
""" Constant value 6
"""

CHANNELS_SURROUND61: typing.Any
""" Constant value 7
"""

CHANNELS_SURROUND71: typing.Any
""" Constant value 8
"""

CODEC_AAC: typing.Any
""" Constant value 1
"""

CODEC_AC3: typing.Any
""" Constant value 2
"""

CODEC_FLAC: typing.Any
""" Constant value 3
"""

CODEC_INVALID: typing.Any
""" Constant value 0
"""

CODEC_MP2: typing.Any
""" Constant value 4
"""

CODEC_MP3: typing.Any
""" Constant value 5
"""

CODEC_OPUS: typing.Any
""" Constant value 8
"""

CODEC_PCM: typing.Any
""" Constant value 6
"""

CODEC_VORBIS: typing.Any
""" Constant value 7
"""

CONTAINER_AC3: typing.Any
""" Constant value 1
"""

CONTAINER_FLAC: typing.Any
""" Constant value 2
"""

CONTAINER_INVALID: typing.Any
""" Constant value 0
"""

CONTAINER_MATROSKA: typing.Any
""" Constant value 3
"""

CONTAINER_MP2: typing.Any
""" Constant value 4
"""

CONTAINER_MP3: typing.Any
""" Constant value 5
"""

CONTAINER_OGG: typing.Any
""" Constant value 6
"""

CONTAINER_WAV: typing.Any
""" Constant value 7
"""

DISTANCE_MODEL_EXPONENT: typing.Any
""" Constant value 5
"""

DISTANCE_MODEL_EXPONENT_CLAMPED: typing.Any
""" Constant value 6
"""

DISTANCE_MODEL_INVALID: typing.Any
""" Constant value 0
"""

DISTANCE_MODEL_INVERSE: typing.Any
""" Constant value 1
"""

DISTANCE_MODEL_INVERSE_CLAMPED: typing.Any
""" Constant value 2
"""

DISTANCE_MODEL_LINEAR: typing.Any
""" Constant value 3
"""

DISTANCE_MODEL_LINEAR_CLAMPED: typing.Any
""" Constant value 4
"""

FORMAT_FLOAT32: typing.Any
""" Constant value 36
"""

FORMAT_FLOAT64: typing.Any
""" Constant value 40
"""

FORMAT_INVALID: typing.Any
""" Constant value 0
"""

FORMAT_S16: typing.Any
""" Constant value 18
"""

FORMAT_S24: typing.Any
""" Constant value 19
"""

FORMAT_S32: typing.Any
""" Constant value 20
"""

FORMAT_U8: typing.Any
""" Constant value 1
"""

RATE_11025: typing.Any
""" Constant value 11025
"""

RATE_16000: typing.Any
""" Constant value 16000
"""

RATE_192000: typing.Any
""" Constant value 192000
"""

RATE_22050: typing.Any
""" Constant value 22050
"""

RATE_32000: typing.Any
""" Constant value 32000
"""

RATE_44100: typing.Any
""" Constant value 44100
"""

RATE_48000: typing.Any
""" Constant value 48000
"""

RATE_8000: typing.Any
""" Constant value 8000
"""

RATE_88200: typing.Any
""" Constant value 88200
"""

RATE_96000: typing.Any
""" Constant value 96000
"""

RATE_INVALID: typing.Any
""" Constant value 0
"""

STATUS_INVALID: typing.Any
""" Constant value 0
"""

STATUS_PAUSED: typing.Any
""" Constant value 2
"""

STATUS_PLAYING: typing.Any
""" Constant value 1
"""

STATUS_STOPPED: typing.Any
""" Constant value 3
"""
