{
    'name':'Masques Impression Veone',
    'description':""" 
    Gestion de:
        - Masques d'impression(Vente-Facturation)
            """,
    'author':'Team Odoo(Veone)',
    'sequence':3,
    'depends':['base','sale','account','account_accountant'],
    'data':[
        'report/masques_veone_reports.xml',
        'data/report_templates.xml',
        'views/report_invoice.xml',
        'views/sale_report_templates.xml',
    ],
    'installable':True,
    'auto_install':False,
}