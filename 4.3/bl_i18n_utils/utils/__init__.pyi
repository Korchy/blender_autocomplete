import typing
import collections.abc
import typing_extensions

class I18n:
    """Internal representation of a whole translation set."""

    parsers: typing.Any
    py_file: typing.Any
    writers: typing.Any

    @classmethod
    def check_py_module_has_translations(cls, src, settings=None):
        """Check whether a given src (a py module, either a directory or a py file) has some i18n translation data,
        and returns a tuple (src_file, translations_tuple) if yes, else (None, None).

                :param src:
                :param settings:
        """

    def escape(self, do_all=False):
        """

        :param do_all:
        """

    def parse(self, kind, src, langs=set()):
        """

        :param kind:
        :param src:
        :param langs:
        """

    def parse_from_po(self, src, langs=set()):
        """

        :param src:
        :param langs:
        """

    def parse_from_py(self, src, langs=set()):
        """src must be a valid path, either a py file or a module directory (in which case all py files inside it
        will be checked, first file matching will win!).
        if langs set is void, all languages found are loaded.

                :param src:
                :param langs:
        """

    def print_stats(self, prefix="", print_msgs=True):
        """Print out some stats about an I18n object.
        If print_msgs is True, it will also print all its translations' stats.

                :param prefix:
                :param print_msgs:
        """

    def unescape(self, do_all=True):
        """

        :param do_all:
        """

    def update_info(self): ...
    def write(self, kind, langs=set()):
        """

        :param kind:
        :param langs:
        """

    def write_to_po(self, langs=set()):
        """

        :param langs:
        """

    def write_to_py(self, langs=set()):
        """

        :param langs:
        """

class I18nMessage:
    """Internal representation of a message."""

    comment_lines: typing.Any
    is_commented: typing.Any
    is_fuzzy: typing.Any
    is_tooltip: typing.Any
    msgctxt: typing.Any
    msgctxt_lines: typing.Any
    msgid: typing.Any
    msgid_lines: typing.Any
    msgstr: typing.Any
    msgstr_lines: typing.Any
    settings: typing.Any
    sources: typing.Any

    def copy(self): ...
    @classmethod
    def do_escape(cls, txt):
        """Replace some chars by their escaped versions!

        :param txt:
        """

    @classmethod
    def do_unescape(cls, txt):
        """Replace escaped chars by real ones!

        :param txt:
        """

    def escape(self, do_all=False):
        """

        :param do_all:
        """

    def normalize(self, max_len=80):
        """Normalize this message, call this before exporting it...
        Currently normalize msgctxt, msgid and msgstr lines to given max_len (if below 1, make them single line).

                :param max_len:
        """

    def unescape(self, do_all=True):
        """

        :param do_all:
        """

class I18nMessages:
    """Internal representation of messages for one language (iso code), with additional stats info."""

    parsers: typing.Any
    writers: typing.Any

    def check(self, fix=False):
        """Check consistency between messages and their keys!
        Check messages using format stuff are consistent between msgid and msgstr!
        If fix is True, tries to fix the issues.
        Return a list of found errors (empty if everything went OK!).

                :param fix:
        """

    def clean_commented(self): ...
    @classmethod
    def cleanup_callback(cls, lng, settings):
        """Cleanup a single PO file (specified by a filepath).Callback usable in a context where Blender specific modules (like bpy) are not available.

        :param lng:
        :param settings:
        """

    def escape(self, do_all=False):
        """

        :param do_all:
        """

    def find_best_messages_matches(
        self, msgs, msgmap, rna_ctxt, rna_struct_name, rna_prop_name, rna_enum_name
    ):
        """

        :param msgs:
        :param msgmap:
        :param rna_ctxt:
        :param rna_struct_name:
        :param rna_prop_name:
        :param rna_enum_name:
        """

    @classmethod
    def gen_empty_messages(
        cls,
        uid,
        blender_ver,
        blender_hash,
        bl_time,
        default_copyright=True,
        settings=None,
    ):
        """Generate an empty I18nMessages object (only header is present!).

        :param uid:
        :param blender_ver:
        :param blender_hash:
        :param bl_time:
        :param default_copyright:
        :param settings:
        """

    def invalidate_reverse_cache(self, rebuild_now=False):
        """Invalidate the reverse cache used by find_best_messages_matches.

        :param rebuild_now:
        """

    def merge(self, msgs, replace=False):
        """

        :param msgs:
        :param replace:
        """

    def normalize(self, max_len=80):
        """

        :param max_len:
        """

    def parse(self, kind, key, src):
        """

        :param kind:
        :param key:
        :param src:
        """

    def parse_messages_from_po(self, src, key=None):
        """

        :param src:
        :param key:
        """

    def print_info(self, prefix="", output=None, print_stats=True, print_errors=True):
        """Print out some info about an I18nMessages object.

        :param prefix:
        :param output:
        :param print_stats:
        :param print_errors:
        """

    def rtl_process(self): ...
    def unescape(self, do_all=True):
        """

        :param do_all:
        """

    def update(self, ref, use_similar=None, keep_old_commented=True):
        """Update this I18nMessage with the ref one. Translations from ref are never used. Source comments from ref
        completely replace current ones. If use_similar is not 0.0, it will try to match new messages in ref with an
        existing one. Messages no more found in ref will be marked as commented if keep_old_commented is True,
        or removed.

                :param ref:
                :param use_similar:
                :param keep_old_commented:
        """

    @classmethod
    def update_from_pot_callback(cls, pot, lng, settings):
        """Update or create a single PO file (specified by a filepath) from the given POT I18nMessages data.Callback usable in a context where Blender specific modules (like bpy) are not available.

        :param pot:
        :param lng:
        :param settings:
        """

    def update_info(self): ...
    @classmethod
    def update_to_blender_repo_callback(cls, lng, settings):
        """Cleanup and write a single PO file (specified by a filepath) into the relevant Blender source 'compact' PO file.Callback usable in a context where Blender specific modules (like bpy) are not available.

        :param lng:
        :param settings:
        """

    def write(self, kind, dest):
        """

        :param kind:
        :param dest:
        """

    def write_messages_to_mo(self, fname):
        """Write messages in fname mo file.

        :param fname:
        """

    def write_messages_to_po(self, fname, compact=False):
        """Write messages in fname po file.

        :param fname:
        :param compact:
        """

def enable_addons(addons=None, support=None, disable=False, check_only=False):
    """Enable (or disable) addons based either on a set of names, or a set of 'support' types.
    Returns the list of all affected addons (as fake modules)!
    If "check_only" is set, no addon will be enabled nor disabled.

    """

def find_best_isocode_matches(uid, iso_codes):
    """Return an ordered tuple of elements in iso_codes that can match the given uid, from most similar to lesser ones."""

def get_best_similar(data): ...
def get_po_files_from_dir(root_dir, langs=set()):
    """Yield tuples (uid, po_path) of translations for each po file found in the given directory, which should be either
    a directory containing po files using language uid's as names (e.g. fr.po, es_ES.po, etc.), or
    a directory containing directories which names are language uids, and containing po files of the same names.

    """

def is_valid_po_path(path): ...
def list_po_dir(root_path, settings):
    """Generator. List given directory (expecting one sub-directory per languages)
    and return all files matching languages listed in settings.Yield tuples (can_use, uid, num_id, name, isocode, po_path)Note that po_path may not actually exists.

    """

def locale_explode(locale):
    """Copies behavior of BLT_lang_locale_explode, keep them in sync."""

def locale_match(loc1, loc2): ...
