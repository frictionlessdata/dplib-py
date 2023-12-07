from rdflib import Namespace
from rdflib.namespace import FOAF, RDF

ADMS = Namespace("http://www.w3.org/ns/adms#")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCT = Namespace("http://purl.org/dc/terms/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")

ACCESS_URL = DCAT.accessURL
ACCURAL_PERIODICITY = DCT.accrualPeriodicity
ALTERNATE_IDENTIFIER = ADMS.identifier
BYTE_SIZE = DCAT.byteSize
COMFORMS_TO = DCT.conformsTo
DATASET = DCAT.Dataset
DESCRIPTION = DCT.description
DISTRIBUTION = DCAT.distribution
DOWNLOAD_URL = DCAT.downloadURL
HAS_VERSION = DCT.hasVersion
HOMEPAGE = FOAF.homepage
IDENTIFIER = DCT.identifier
ISSUED = DCT.issued
IS_VERSION_OF = DCT.isVersionOf
KEYWORD = DCAT.keyword
LANDING_PAGE = DCAT.landingPage
LANGUAGE = DCT.language
LICENSE = DCT.license
MEDIA_TYPE = DCAT.mediaType
MODIFIED = DCT.modified
PAGE = FOAF.page
PROVENANCE = DCT.provenance
RELATED_RESOURCE = DCT.relation
SAMPLE = ADMS.sample
SOURCE = DCT.source
THEME = DCAT.theme
TITLE = DCT.title
TYPE = RDF.type
VERSION = OWL.versionInfo

BINDINGS = {
    "adms": ADMS,
    "dcat": DCAT,
    "dct": DCT,
    "owl": OWL,
}
