from rdflib import Namespace
from rdflib.namespace import FOAF, RDF

ADMS = Namespace("http://www.w3.org/ns/adms#")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCT = Namespace("http://purl.org/dc/terms/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")

LICENSE = DCT.license
ACCESS_URL = DCAT.accessURL
DOWNLOAD_URL = DCAT.downloadURL
DISTRIBUTION = DCAT.Distribution
DATASET = DCAT.Dataset
TYPE = RDF.type
IDENTIFIER = DCT.identifier
TITLE = DCT.title
DESCRIPTION = DCT.description
VERSION = OWL.versionInfo
LANDING_PAGE = DCAT.landingPage
ISSUED = DCT.issued
MODIFIED = DCT.modified
ACCURAL_PERIODICITY = DCT.accrualPeriodicity
PROVENANCE = DCT.provenance
KEYWORD = DCAT.keyword
LANGUAGE = DCT.language
SOURCE = DCT.source
SAMPLE = ADMS.sample
THEME = DCAT.theme
ALTERNATE_IDENTIFIER = ADMS.identifier
COMFORMS_TO = DCT.conformsTo
DOCUMENTATION = FOAF.page
RELATED_RESOURCE = DCT.relation
HAS_VERSION = DCT.hasVersion
IS_VERSION_OF = DCT.isVersionOf

BINDINGS = {
    "adms": ADMS,
    "dcat": DCAT,
    "dct": DCT,
    "owl": OWL,
}
