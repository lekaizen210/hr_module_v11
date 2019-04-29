#-*- coding:utf-8 -*-
__author__ = 'lekaizen'


from odoo import fields, models, api, _
from odoo.exceptions import UserError


class HrPayroll(models.TransientModel):
    _name = 'hr.payroll.payroll'
    _description = "Gestion des livres de paie"

    name = fields.Char('Nom', required=True, size=155)
    # lot_id = fields.Many2one('h.payslip.run', 'Lot de paie', required=True)
    date_from = fields.Date('Date de début', required=True)
    date_to = fields.Date('Date de fin', required=True)
    company_id= fields.Many2one('res.company', 'Compagnie', required=True, default=1)
    type_employe = fields.Selection([('mensuel','Mensuel'),
                                     ('journalier','Journalier'),
                                     ('horaire','Horaire'),('all','Tous les employés')],"Livre de paie pour:", default="all")

    def _print_report(self, data):
        data['form'].update(self.read(['initial_balance', 'sortby'])[0])
        if data['form'].get('initial_balance') and not data['form'].get('date_from'):
            raise UserError(_("You must define a Start Date"))

        records = self.env[data['model']].browse(data.get('ids', []))
        return self.env.ref('hr_payroll_ci_raport.report_hr_payroll').with_context(landscape=True).report_action(self, data=data)

    @api.multi
    def check_report(self):
        self.ensure_one()
        print(self.id)
        data = {}
        data['ids'] = self.id
        data['model'] = 'hr.payroll.payroll'
        data['form'] = self.read(['name','date_from', 'date_to', 'company_id','type_employe'])[0]
        print(data)
        return self._print_report(data)


    @api.multi
    def export_xls(self):
        context = self._context
        datas = {'ids': context.get('active_ids', [])}
        datas['model'] = 'hr.payroll.payroll'
        datas['form'] = self.read()[0]
        for field in datas['form'].keys():
            if isinstance(datas['form'][field], tuple):
                datas['form'][field] = datas['form'][field][0]

        #return self.env.ref('hr_payroll_ci_raport.payroll_report_xlsx').report_action(self, data=datas, config=False)