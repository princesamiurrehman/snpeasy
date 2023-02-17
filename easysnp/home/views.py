from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from Bio import Entrez



def index(request):
    Entrez.email = "princesamiurrehman9299@gmail.com"
    handle = Entrez.einfo(db="snp")
    result = Entrez.read(handle)

    template = loader.get_template('home.html')

    context = {

        'dbnamevalue':result['DbInfo']['DbName'],
        'dbdescriptionvalue': result['DbInfo']['Description'],
        'dbbuildvalue': result['DbInfo']['DbBuild'],
        'dbcountvalue': result['DbInfo']['Count'],
        'dblastupdatedvalue': result['DbInfo']['LastUpdate'],

        'dbtermsinformationvalue1': result['DbInfo']['FieldList'][0]['Description'],
        'dbtermsinformationvalue2': result['DbInfo']['FieldList'][0]['TermCount'],


        'dbtermuiddescriptionvalue': result['DbInfo']['FieldList'][1]['Description'],
        'dbtermuidcount': result['DbInfo']['FieldList'][1]['TermCount'],

        'dbtermfiltervalue': result['DbInfo']['FieldList'][2]['FullName'],
        'dbtermfilterdescriptionvalue': result['DbInfo']['FieldList'][2]['Description'],
        'dbtermfiltercount': result['DbInfo']['FieldList'][2]['TermCount'],

        'dbrsdescription': result['DbInfo']['FieldList'][3]['Description'],
        'dbrscount': result['DbInfo']['FieldList'][3]['TermCount'],

        'chrcount': result['DbInfo']['FieldList'][4]['TermCount'],

        'genecount': result['DbInfo']['FieldList'][5]['TermCount'],

        'hancount': result['DbInfo']['FieldList'][6]['TermCount'],

        'genecount': result['DbInfo']['FieldList'][6]['TermCount'],

        'sscount': result['DbInfo']['FieldList'][11]['TermCount'],

        'cposcount': result['DbInfo']['FieldList'][14]['TermCount'],

        'gmafcount': result['DbInfo']['FieldList'][18]['TermCount'],

    }

    return HttpResponse(template.render(context,request))



