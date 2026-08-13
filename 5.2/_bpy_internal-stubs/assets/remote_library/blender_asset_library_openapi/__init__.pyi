import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class AssetBlenderVersionsV1:
    """Minimum and (optionally) maximum versions of Blender that this asset
    should be shown in.This is a half-open interval: Blender shows the asset if min <= blender < until.
    """

    until: typing.Any

class AssetLibraryIndexPageV1:
    """Any number of assets."""

class AssetLibraryIndexV1:
    """The available assets at this library."""

    catalogs: typing.Any

class AssetLibraryMeta:
    """Meta-data of this asset library."""

class AssetMetadataV1:
    """Metadata of an asset, as defined by Blenders AssetMeta DNA struct.Fields should either be non-empty or absent."""

    author: typing.Any
    catalog_id: typing.Any
    copyright: typing.Any
    description: typing.Any
    license: typing.Any
    preferred_import_method: typing.Any
    properties: typing.Any
    tags: typing.Any

class AssetV1:
    """Representation of a single asset.Assets are always Blender data-blocks in some blend file. This asset
    may be stored in the same blend file as other assets, and so it does
    _not_ represent a single downloadable item.
    """

    meta: typing.Any
    thumbnail: typing.Any

class CatalogV1:
    """An asset catalog, which can be represented by one or more UUIDs."""

    simple_name: typing.Any

class Contact:
    """Owner / publisher of this asset library."""

    email: typing.Any
    url: typing.Any

class CustomPropertyTypeV1:
    """Type of IDProperty, see eIDPropertyType in DNA_ID_enumms.h.For now, type ID and IDPARRAY are not supported."""

    IDP_ARRAY: typing.Any
    IDP_BOOL: typing.Any
    IDP_DOUBLE: typing.Any
    IDP_FLOAT: typing.Any
    IDP_GROUP: typing.Any
    IDP_INT: typing.Any
    IDP_STRING: typing.Any

class CustomPropertyV1:
    """Single custom property value of the asset.The value should be compatible with the given type; GROUP properties
    should be represented as CustomPropertiesV1 object again. Arrays
    should specify an itemtype.
    """

    itemtype: typing.Any

class FileV1:
    """Single file in the asset library.Identified by its relative path in that library."""

    url: typing.Any

class URLWithHash:
    """Resource thats identified by a URL.The resource should be fetched by including the hash in the query
    string, like GET {URL}?hash={HASH}. Here {HASH} should _not_
    include the hash type. The purpose of including this on the URL is
    for cache busting, and thus the hash type is not relevant here.
    """
