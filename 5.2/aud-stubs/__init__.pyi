"""
Audaspace (pronounced "outer space") is a high level audio library.


--------------------

This script shows how to use the classes: Device, Sound and
Handle.

```../examples/aud.0.py```

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class AnimateableProperty:
    """An AnimateableProperty object stores an array of float values for animating sound properties (e.g. pan, volume, pitch-scale)."""

    animated: typing.Any
    """ Whether the property is animated."""

    count: typing.Any
    """ The count of floats for a property."""

    def read(self, position: float) -> npt.NDArray:
        """Reads the properties value at the given position.

        :param position: The position in the animation in frames.
        :return: A numpy array of values representing the properties value.
        """

    def readSingle(self, position: float) -> float:
        """Reads the properties value at the given position, assuming there is exactly one value.

        :param position: The position in the animation in frames.
        :return: The value at that position.
        """

    def write(self, data, position: int) -> None:
        """Writes the properties value.If position is also given, the property is marked animated and
        the values are written starting at position.

                :param data: numpy array of float32 values.
                :param position: The starting position in frames.
        """

    def writeConstantRange(self, data, position_start: int, position_end: int) -> None:
        """Fills the properties frame range with a constant value and marks it animated.

        :param data: numpy array of float values representing the constant value.
        :param position_start: The start position in frames.
        :param position_end: The end position in frames.
        """

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

    def lock(self) -> None:
        """Locks the device so that its guaranteed, that no samples are
        read from the streams until `unlock` is called.
        This is useful if you want to do start/stop/pause/resume some
        sounds at the same time.

        """

    def play(self, sound: Sound, keep: bool = False) -> Handle:
        """Plays a sound.

                :param sound: The sound to play.
                :param keep: See `Handle.keep`.
                :return: The playback handle with which playback can be
        controlled with.
        """

    def stopAll(self) -> None:
        """Stops all playing and paused sounds."""

    def unlock(self) -> None:
        """Unlocks the device after a lock call, see `lock` for
        details.

        """

class DynamicMusic:
    """The DynamicMusic object allows to play music depending on a current scene, scene changes are managed by the class, with the possibility of custom transitions.
    The default transition is a crossfade effect, and the default scene is silent and has id 0.
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
        :return: The new scene id.
        """

    def addTransition(self, ini: int, end: int, transition: Sound) -> bool:
        """Adds a new scene.

        :param ini: the initial scene foor the transition.
        :param end: The final scene for the transition.
        :param transition: The transition sound.
        :return: false if the ini or end scenes dont exist, true otherwise.
        """

    def pause(self) -> bool:
        """Pauses playback of the scene.

        :return: Whether the action succeeded.
        """

    def resume(self) -> bool:
        """Resumes playback of the scene.

        :return: Whether the action succeeded.
        """

    def stop(self) -> bool:
        """Stops playback of the scene.

        :return: Whether the action succeeded.
        """

class HRTF:
    """An HRTF object represents a set of head related transfer functions as impulse responses. Its used for binaural sound."""

    def loadLeftHrtfSet(self, extension: str, directory) -> typing_extensions.Self:
        """Loads all HRTFs from a directory.

        :param extension: The file extension of the hrtfs.
        :param directory: The path to where the HRTF files are located.
        :return: The loaded `HRTF` object.
        """

    def loadRightHrtfSet(self, extension: str, directory) -> typing_extensions.Self:
        """Loads all HRTFs from a directory.

        :param extension: The file extension of the hrtfs.
        :param directory: The path to where the HRTF files are located.
        :return: The loaded `HRTF` object.
        """

    def addImpulseResponseFromSound(
        self, sound: Sound, azimuth: float, elevation: float
    ) -> bool:
        """Adds a new hrtf to the HRTF object

        :param sound: The sound that contains the hrtf.
        :param azimuth: The azimuth angle of the hrtf.
        :param elevation: The elevation angle of the hrtf.
        :return: Whether the action succeeded.
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
        """

    def resume(self) -> bool:
        """Resumes playback.

        :return: Whether the action succeeded.
        """

    def stop(self) -> bool:
        """Stops playback.

        :return: Whether the action succeeded.
        """

class ImpulseResponse:
    """An ImpulseResponse object represents a filter with which to convolve a sound."""

class PlaybackManager:
    """A PlaybackManager object allows to easily control groups of sounds organized in categories."""

    def addCategory(self, volume: float) -> int:
        """Adds a category with a custom volume.

        :param volume: The volume for ther new category.
        :return: The key of the new category.
        """

    def clean(self) -> None:
        """Cleans all the invalid and finished sound from the playback manager."""

    def getVolume(self, catKey: int) -> float:
        """Retrieves the volume of a category.

        :param catKey: the key of the category.
        :return: The volume of the category.
        """

    def pause(self, catKey: int) -> bool:
        """Pauses playback of the category.

        :param catKey: the key of the category.
        :return: Whether the action succeeded.
        """

    def play(self, sound: Sound, catKey: int) -> Handle:
        """Plays a sound through the playback manager and assigns it to a category.

                :param sound: The sound to play.
                :param catKey: the key of the category in which the sound will be added,
        if it doesnt exist, a new one will be created.
                :return: The playback handle with which playback can be controlled with.
        """

    def resume(self, catKey: int) -> bool:
        """Resumes playback of the catgory.

        :param catKey: the key of the category.
        :return: Whether the action succeeded.
        """

    def setVolume(self, volume: float, catKey: int) -> int:
        """Changes the volume of a category.

        :param volume: the new volume value.
        :param catKey: the key of the category.
        :return: Whether the action succeeded.
        """

    def stop(self, catKey: int) -> bool:
        """Stops playback of the category.

        :param catKey: the key of the category.
        :return: Whether the action succeeded.
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
        """

    def remove(self) -> None:
        """Removes an entry from the sequence."""

    def setAnimationData(self) -> None:
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

    def move(self) -> None:
        """Moves the entry."""

    def setAnimationData(self) -> None:
        """Writes animation data to a sequenced entry."""

class Sound:
    """Sound objects are immutable and represent a sound that can be played simultaneously multiple times. They are called factories because they create reader objects internally that are used for playback."""

    length: typing.Any
    """ The sample specification of the sound as a tuple with rate and channel count."""

    specs: typing.Any
    """ The sample specification of the sound as a tuple with rate and channel count."""

    @classmethod
    def buffer(cls, data: npt.NDArray, rate: float) -> typing_extensions.Self:
        """Creates a sound from a data buffer.

        :param data: The data as two dimensional numpy array.
        :param rate: The sample rate.
        :return: The created `Sound` object.
        """

    @classmethod
    def file(cls, filename: str) -> typing_extensions.Self:
        """Creates a sound object of a sound file.

        :param filename: Path of the file.
        :return: The created `Sound` object.
        """

    @classmethod
    def list(cls) -> typing_extensions.Self:
        """Creates an empty sound list that can contain several sounds.

        :return: The created `Sound` object.
        """

    @classmethod
    def sawtooth(cls, frequency: float, rate: int = 48000) -> typing_extensions.Self:
        """Creates a sawtooth sound which plays a sawtooth wave.

                :param frequency: The frequency of the sawtooth wave in Hz.
                :param rate: The sampling rate in Hz. Its recommended to set this
        value to the playback devices sampling rate to avoid resampling.
                :return: The created `Sound` object.
        """

    @classmethod
    def silence(cls, rate: int = 48000) -> typing_extensions.Self:
        """Creates a silence sound which plays simple silence.

                :param rate: The sampling rate in Hz. Its recommended to set this
        value to the playback devices sampling rate to avoid resampling.
                :return: The created `Sound` object.
        """

    @classmethod
    def sine(cls, frequency: float, rate: int = 48000) -> typing_extensions.Self:
        """Creates a sine sound which plays a sine wave.

                :param frequency: The frequency of the sine wave in Hz.
                :param rate: The sampling rate in Hz. Its recommended to set this
        value to the playback devices sampling rate to avoid resampling.
                :return: The created `Sound` object.
        """

    @classmethod
    def square(cls, frequency: float, rate: int = 48000) -> typing_extensions.Self:
        """Creates a square sound which plays a square wave.

                :param frequency: The frequency of the square wave in Hz.
                :param rate: The sampling rate in Hz. Its recommended to set this
        value to the playback devices sampling rate to avoid resampling.
                :return: The created `Sound` object.
        """

    @classmethod
    def triangle(cls, frequency: float, rate: int = 48000) -> typing_extensions.Self:
        """Creates a triangle sound which plays a triangle wave.

                :param frequency: The frequency of the triangle wave in Hz.
                :param rate: The sampling rate in Hz. Its recommended to set this
        value to the playback devices sampling rate to avoid resampling.
                :return: The created `Sound` object.
        """

    def ADSR(
        self, attack: float, decay: float, sustain: float, release: float
    ) -> typing_extensions.Self:
        """Attack-Decay-Sustain-Release envelopes the volume of a sound.
        Note: there is currently no way to trigger the release with this API.

                :param attack: The attack time in seconds.
                :param decay: The decay time in seconds.
                :param sustain: The sustain level.
                :param release: The release level.
                :return: The created `Sound` object.
        """

    def accumulate(self, additive=False) -> typing_extensions.Self:
        """Accumulates a sound by summing over positive input
        differences thus generating a monotonic sigal.
        If additivity is set to true negative input differences get added too,
        but positive ones with a factor of two.Note that with additivity the signal is not monotonic anymore.

                :param additive: Whether the accumulation should be additive or not.
                :return: The created `Sound` object.
        """

    def addSound(self, sound: typing_extensions.Self) -> None:
        """Adds a new sound to a sound list.

        :param sound: The sound that will be added to the list.
        """

    def animateableTimeStretchPitchScale(
        self,
        fps: float,
        time_stretch: float,
        pitch_scale: float,
        quality: int,
        preserve_formant: bool,
    ) -> typing_extensions.Self:
        """Applies time-stretching and pitch-scaling to the sound.

        :param fps: The FPS of the animation system.
        :param time_stretch: The factor by which to stretch or compress time.
        :param pitch_scale: The factor by which to adjust the pitch.
        :param quality:
        :param preserve_formant: Whether to preserve the vocal formants during pitch-shifting.
        :return: The created `Sound` object.
        """

    def binaural(self) -> typing_extensions.Self:
        """Creates a binaural sound using another sound as source. The original sound must be mono

        :return: The created `Sound` object.
        """

    def cache(self) -> typing_extensions.Self:
        """Caches a sound into RAM.This saves CPU usage needed for decoding and file access if the
        underlying sound reads from a file on the harddisk,
        but it consumes a lot of memory.

                :return: The created `Sound` object.
        """

    def convolver(self) -> typing_extensions.Self:
        """Creates a sound that will apply convolution to another sound.

        :return: The created `Sound` object.
        """

    def data(self) -> npt.NDArray:
        """Retrieves the data of the sound as numpy array.

        :return: A two dimensional numpy float array.
        """

    def delay(self, time: float) -> typing_extensions.Self:
        """Delays by playing adding silence in front of the other sounds data.

        :param time: How many seconds of silence should be added before the sound.
        :return: The created `Sound` object.
        """

    def Echo(self, delay: float, feedback: float, mix: float) -> typing_extensions.Self:
        """Adds Echo effect to the sound.

        :param delay: The delay time in seconds.
        :param feedback: The feedback amount (0.0 to 1.0).
        :param mix: The wet/dry mix (0.0 to 1.0).
        :return: The created `Sound` object.
        """

    def envelope(
        self, attack: float, release: float, threshold: float, arthreshold: float
    ) -> typing_extensions.Self:
        """Delays by playing adding silence in front of the other sounds data.

        :param attack: The attack factor.
        :param release: The release factor.
        :param threshold: The general threshold value.
        :param arthreshold: The attack/release threshold value.
        :return: The created `Sound` object.
        """

    def fadein(self, start: float, length: float) -> typing_extensions.Self:
        """Fades a sound in by raising the volume linearly in the given
        time interval.

                :param start: Time in seconds when the fading should start.
                :param length: Time in seconds how long the fading should last.
                :return: The created `Sound` object.
        """

    def fadeout(self, start: float, length: float) -> typing_extensions.Self:
        """Fades a sound in by lowering the volume linearly in the given
        time interval.

                :param start: Time in seconds when the fading should start.
                :param length: Time in seconds how long the fading should last.
                :return: The created `Sound` object.
        """

    def filter(self, b: list[float], a: list[float] = (1)) -> typing_extensions.Self:
        """Filters a sound with the supplied IIR filter coefficients.
        Without the second parameter youll get a FIR filter.If the first value of the a sequence is 0,
        it will be set to 1 automatically.
        If the first value of the a sequence is neither 0 nor 1, all
        filter coefficients will be scaled by this value so that it is 1
        in the end, you dont have to scale yourself.

                :param b: The nominator filter coefficients.
                :param a: The denominator filter coefficients.
                :return: The created `Sound` object.
        """

    def highpass(self, frequency: float, Q: float = 0.5) -> typing_extensions.Self:
        """Creates a second order highpass filter based on the transfer
        function H(s) = s^2 / (s^2 + s/Q + 1)

                :param frequency: The cut off trequency of the highpass.
                :param Q: Q factor of the lowpass.
                :return: The created `Sound` object.
        """

    def join(self, sound: typing_extensions.Self) -> typing_extensions.Self:
        """Plays two factories in sequence.

        :param sound: The sound to play second.
        :return: The created `Sound` object.
        """

    def limit(self, start: float, end: float) -> typing_extensions.Self:
        """Limits a sound within a specific start and end time.

        :param start: Start time in seconds.
        :param end: End time in seconds.
        :return: The created `Sound` object.
        """

    def loop(self, count: int) -> typing_extensions.Self:
        """Loops a sound.

                :param count: How often the sound should be looped.
        Negative values mean endlessly.
                :return: The created `Sound` object.
        """

    def lowpass(self, frequency: float, Q: float = 0.5) -> typing_extensions.Self:
        """Creates a second order lowpass filter based on the transfer    function H(s) = 1 / (s^2 + s/Q + 1)

        :param frequency: The cut off trequency of the lowpass.
        :param Q: Q factor of the lowpass.
        :return: The created `Sound` object.
        """

    def mix(self, sound: typing_extensions.Self) -> typing_extensions.Self:
        """Mixes two factories.

        :param sound: The sound to mix over the other.
        :return: The created `Sound` object.
        """

    def modulate(self, sound: typing_extensions.Self) -> typing_extensions.Self:
        """Modulates two factories.

        :param sound: The sound to modulate over the other.
        :return: The created `Sound` object.
        """

    def mutable(self) -> typing_extensions.Self:
        """Creates a sound that will be restarted when sought backwards.
        If the original sound is a sound list, the playing sound can change.

                :return: The created `Sound` object.
        """

    def pingpong(self) -> typing_extensions.Self:
        """Plays a sound forward and then backward.
        This is like joining a sound with its reverse.

                :return: The created `Sound` object.
        """

    def pitch(self, factor: float) -> typing_extensions.Self:
        """Changes the pitch of a sound with a specific factor.

        :param factor: The factor to change the pitch with.
        :return: The created `Sound` object.
        """

    def rechannel(self, channels: int) -> typing_extensions.Self:
        """Rechannels the sound.

        :param channels: The new channel configuration.
        :return: The created `Sound` object.
        """

    def resample(self, rate: float, quality: int) -> typing_extensions.Self:
        """Resamples the sound.

        :param rate: The new sample rate.
        :param quality: Resampler performance vs quality choice (0=fastest, 3=slowest).
        :return: The created `Sound` object.
        """

    def reverse(self) -> typing_extensions.Self:
        """Plays a sound reversed.

        :return: The created `Sound` object.
        """

    def sum(self) -> typing_extensions.Self:
        """Sums the samples of a sound.

        :return: The created `Sound` object.
        """

    def threshold(self, threshold: float = 0) -> typing_extensions.Self:
        """Makes a threshold wave out of an audio wave by setting all samples
        with a amplitude >= threshold to 1, all <= -threshold to -1 and
        all between to 0.

                :param threshold: Threshold value over which an amplitude counts
        non-zero.
                :return: The created `Sound` object.
        """

    def timeStretchPitchScale(
        self,
        time_stretch: float,
        pitch_scale: float,
        quality: int,
        preserve_formant: bool,
    ) -> typing_extensions.Self:
        """Applies time-stretching and pitch-scaling to the sound.

        :param time_stretch: The factor by which to stretch or compress time.
        :param pitch_scale: The factor by which to adjust the pitch.
        :param quality: Rubberband stretcher quality (STRETCHER_QUALITY_*).
        :param preserve_formant: Whether to preserve the vocal formants during pitch-shifting.
        :return: The created `Sound` object.
        """

    def volume(self, volume: float) -> typing_extensions.Self:
        """Changes the volume of a sound.

        :param volume: The new volume..
        :return: The created `Sound` object.
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
    ) -> None:
        """Writes the sound to a file.

        :param filename: The path to write to.
        :param rate: The sample rate to write with.
        :param channels: The number of channels to write with.
        :param format: The sample format to write with.
        :param container: The container format for the file.
        :param codec: The codec to use in the file.
        :param bitrate: The bitrate to write with.
        :param buffersize: The size of the writing buffer.
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

AP_LOCATION: int
""" Constant value 3
"""

AP_ORIENTATION: int
""" Constant value 4
"""

AP_PANNING: int
""" Constant value 1
"""

AP_PITCH: int
""" Constant value 2
"""

AP_PITCH_SCALE: int
""" Constant value 6
"""

AP_TIME_STRETCH: int
""" Constant value 5
"""

AP_VOLUME: int
""" Constant value 0
"""

CHANNELS_INVALID: int
""" Constant value 0
"""

CHANNELS_MONO: int
""" Constant value 1
"""

CHANNELS_STEREO: int
""" Constant value 2
"""

CHANNELS_STEREO_LFE: int
""" Constant value 3
"""

CHANNELS_SURROUND4: int
""" Constant value 4
"""

CHANNELS_SURROUND5: int
""" Constant value 5
"""

CHANNELS_SURROUND51: int
""" Constant value 6
"""

CHANNELS_SURROUND61: int
""" Constant value 7
"""

CHANNELS_SURROUND71: int
""" Constant value 8
"""

CODEC_AAC: int
""" Constant value 1
"""

CODEC_AC3: int
""" Constant value 2
"""

CODEC_FLAC: int
""" Constant value 3
"""

CODEC_INVALID: int
""" Constant value 0
"""

CODEC_MP2: int
""" Constant value 4
"""

CODEC_MP3: int
""" Constant value 5
"""

CODEC_OPUS: int
""" Constant value 8
"""

CODEC_PCM: int
""" Constant value 6
"""

CODEC_VORBIS: int
""" Constant value 7
"""

CONTAINER_AAC: int
""" Constant value 8
"""

CONTAINER_AC3: int
""" Constant value 1
"""

CONTAINER_FLAC: int
""" Constant value 2
"""

CONTAINER_INVALID: int
""" Constant value 0
"""

CONTAINER_MATROSKA: int
""" Constant value 3
"""

CONTAINER_MP2: int
""" Constant value 4
"""

CONTAINER_MP3: int
""" Constant value 5
"""

CONTAINER_OGG: int
""" Constant value 6
"""

CONTAINER_WAV: int
""" Constant value 7
"""

DISTANCE_MODEL_EXPONENT: int
""" Constant value 5
"""

DISTANCE_MODEL_EXPONENT_CLAMPED: int
""" Constant value 6
"""

DISTANCE_MODEL_INVALID: int
""" Constant value 0
"""

DISTANCE_MODEL_INVERSE: int
""" Constant value 1
"""

DISTANCE_MODEL_INVERSE_CLAMPED: int
""" Constant value 2
"""

DISTANCE_MODEL_LINEAR: int
""" Constant value 3
"""

DISTANCE_MODEL_LINEAR_CLAMPED: int
""" Constant value 4
"""

FORMAT_FLOAT32: int
""" Constant value 36
"""

FORMAT_FLOAT64: int
""" Constant value 40
"""

FORMAT_INVALID: int
""" Constant value 0
"""

FORMAT_S16: int
""" Constant value 18
"""

FORMAT_S24: int
""" Constant value 19
"""

FORMAT_S32: int
""" Constant value 20
"""

FORMAT_U8: int
""" Constant value 1
"""

RATE_11025: int
""" Constant value 11025
"""

RATE_16000: int
""" Constant value 16000
"""

RATE_192000: int
""" Constant value 192000
"""

RATE_22050: int
""" Constant value 22050
"""

RATE_32000: int
""" Constant value 32000
"""

RATE_44100: int
""" Constant value 44100
"""

RATE_48000: int
""" Constant value 48000
"""

RATE_8000: int
""" Constant value 8000
"""

RATE_88200: int
""" Constant value 88200
"""

RATE_96000: int
""" Constant value 96000
"""

RATE_INVALID: int
""" Constant value 0
"""

STATUS_INVALID: int
""" Constant value 0
"""

STATUS_PAUSED: int
""" Constant value 2
"""

STATUS_PLAYING: int
""" Constant value 1
"""

STATUS_STOPPED: int
""" Constant value 3
"""

STRETCHER_QUALITY_CONSISTENT: int
""" Constant value 2
"""

STRETCHER_QUALITY_FAST: int
""" Constant value 1
"""

STRETCHER_QUALITY_HIGH: int
""" Constant value 0
"""
