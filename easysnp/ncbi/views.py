from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import requests
from Bio import Entrez
from Bio import SeqIO
import xmltodict
import pprint
import json
import collections
from numpy import asarray
from numpy import savetxt
import sys

def id_txt(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=idsList.txt'

    lines = ["this is line 1\n",
             "this is line 2\n",
             "this is line 3\n"]

    response.writelines(lines)
    return response



def ncbi(request):
    template = loader.get_template('snpdata.html')

    return HttpResponse(template.render())


@csrf_exempt
def actor(request):
    searchedterm = request.POST['geneid']
    Entrez.email = "princesamiurrehman9299@gmail.com"
    handle = Entrez.esearch(db="snp", term=searchedterm + ' AND missense variant[Function_Class]' , retmax=5000)
    result = Entrez.read(handle)

    ids = result['IdList']
    context = {
        'reference': 'rs',
        'searchterm': 'Searched Term : ' + searchedterm,
        'snpcount': 'Total : ' + result['Count'],
        'keys': result,
        'searchedids': result['IdList'],
        'srno': 0,
        'button1': "Download Ids"
    }

    template = loader.get_template('snpdata.html')
    return HttpResponse(template.render(context,request))


@csrf_exempt
def idinfo(request):
    ide = request.POST['currentid']

    Entrez.email = "princesamiurrehman9299@gmail.com"
    handle2 = Entrez.esummary(db="snp", id=ide)
    result2 = Entrez.read(handle2)
    detailedinfo = {
        'reference' : 'rs',
        'snpId' : result2['DocumentSummarySet']['DocumentSummary'][0]['SNP_ID'],
        'gmafStudy': result2['DocumentSummarySet']['DocumentSummary'][0]['GLOBAL_MAFS'][0]['STUDY'],
        'gmafFreq': result2['DocumentSummarySet']['DocumentSummary'][0]['GLOBAL_MAFS'][0]['FREQ'],
        'geneName': result2['DocumentSummarySet']['DocumentSummary'][0]['GENES'][0]['NAME'],
        'geneId': result2['DocumentSummarySet']['DocumentSummary'][0]['GENES'][0]['GENE_ID'],
        'acc': result2['DocumentSummarySet']['DocumentSummary'][0]['ACC'],
        'chr': result2['DocumentSummarySet']['DocumentSummary'][0]['CHR'],
        'spdi': result2['DocumentSummarySet']['DocumentSummary'][0]['SPDI'],
        'fxnclass': result2['DocumentSummarySet']['DocumentSummary'][0]['FXN_CLASS'],
        'validated': result2['DocumentSummarySet']['DocumentSummary'][0]['VALIDATED'],
        'docsum': result2['DocumentSummarySet']['DocumentSummary'][0]['DOCSUM'],
        'taxId': result2['DocumentSummarySet']['DocumentSummary'][0]['TAX_ID'],
        'origBuild': result2['DocumentSummarySet']['DocumentSummary'][0]['ORIG_BUILD'],
        'alle': result2['DocumentSummarySet']['DocumentSummary'][0]['ALLELE'],
        'snpClass': result2['DocumentSummarySet']['DocumentSummary'][0]['SNP_CLASS'],
        'chrpos': result2['DocumentSummarySet']['DocumentSummary'][0]['CHRPOS'],
    }

    template = loader.get_template('idsinfo.html')
    return HttpResponse(template.render(detailedinfo,request))

@csrf_exempt
def actortwo(request):
    identity = request.POST['geneid']

    requestURL = "https://www.ebi.ac.uk/proteins/api/proteins?offset=0&gene=" + identity

    r = requests.get(requestURL, headers={"Accept": "application/json"})

    r2 = r.json()

    information = {
        'databaseName':'EMBL-EBI',
        'accession': r2[0]['accession'],
        'id' : r2[0]['id'],
        'proteinExistence': r2[0]['proteinExistence'],
        'info' : r2[0]['info']['type'],
        'infoCreated': r2[0]['info']['created'],
        'infoModified': r2[0]['info']['modified'],

        'organismTax' : r2[0]['organism']['taxonomy'],
        'organismSci' : r2[0]['organism']['names'][0]['value'],
        'organismCom': r2[0]['organism']['names'][2]['value'],

        'protein' : r2[0]['protein']['submittedName'][0]['fullName']['value'],
        'proteinSourceName': r2[0]['protein']['submittedName'][0]['fullName']['evidences'][0]['source']['name'],
        'proteinSourceId': r2[0]['protein']['submittedName'][0]['fullName']['evidences'][0]['source']['id'],
        'proteinSourceUrl': r2[0]['protein']['submittedName'][0]['fullName']['evidences'][0]['source']['url'],

        'gene': r2[0]['gene'][0]['name']['value'],
        'geneSourceName': r2[0]['gene'][0]['name']['evidences'][0]['source']['name'],
        'geneSourceId': r2[0]['gene'][0]['name']['evidences'][0]['source']['id'],
        'geneSourceUrl':r2[0]['gene'][0]['name']['evidences'][0]['source']['url'],






    }

    template = loader.get_template('uniprot.html')
    return HttpResponse(template.render(information, request))





@csrf_exempt
def actorsix(request):

    identity = request.POST['geneid']

    requestURL = "https://rest.uniprot.org/uniprotkb/"+ identity

    r = requests.get(requestURL).json()

    proteininfo = {
        'all' : 'r',
        'databaseName': r['entryType'],
        'primaryAccession':r['primaryAccession'],
        'secondaryAccessions': r['secondaryAccessions'],
        'uniProtkbId': r['uniProtkbId'],
        'organism': r['organism']['scientificName'],
        'commonName': r['organism']['commonName'],
        'taxonId': r['organism']['taxonId'],
        'lineage': r['organism']['lineage'],
        'proteinExistence': r['proteinExistence'],
        'proteinDescriptionfullName': r['proteinDescription']['recommendedName']['fullName']['value'],
        'proteinDescriptionevidenceCode': r['proteinDescription']['alternativeNames'][0]['fullName']['evidences'][0]['evidenceCode'],
        'proteinDescriptionevidencesource': r['proteinDescription']['alternativeNames'][0]['fullName']['evidences'][0]['source'],
        'proteinDescriptionevidenceid': r['proteinDescription']['alternativeNames'][0]['fullName']['evidences'][0]['id'],
        'proteinDescriptionfullNamevalue': r['proteinDescription']['alternativeNames'][0]['fullName']['value'],
        'proteinDescriptionshortNamevalue': r['proteinDescription']['alternativeNames'][0]['shortNames'][0]['value'],

        'genevalue': r['genes'][0]['geneName']['value'],
        'genes1': r['genes'][0]['geneName']['evidences'][0]['source'],
        'genes1id': r['genes'][0]['geneName']['evidences'][0]['id'],
        'genes2': r['genes'][0]['geneName']['evidences'][1]['source'],
        'genes2id': r['genes'][0]['geneName']['evidences'][1]['id'],

        'sequence': r['sequence']['value'],
        'length': r['sequence']['length'],
        'molWeight': r['sequence']['molWeight'],
        'crc64': r['sequence']['crc64'],
        'md5': r['sequence']['md5'],


    }
    template = loader.get_template('uniprotorg.html')
    return HttpResponse(template.render(proteininfo,request))

