# -*- coding:utf-8 -*-


from odoo import api, fields, models, exceptions
from itertools import groupby

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    overtime_ids= fields.One2many('hr.attendance.heure.supp', 'employee_id', "Heures supplémentaires")

    def getOvertime(self, date_start, date_end):
        res = []
        #Recuperation de toutes les heures supp comprises entre date_start et date_end
        overtimes = self.overtime_ids.filtered(lambda over : over.h_date >= date_start and over.h_date <= date_end and over.state == 'confirmed')
        if overtimes :
            #Regrouper les heures supp
            for type, lines in groupby(overtimes, lambda l: l.heure_supp_type_id):
                for line in lines:
                    dic = {
                        'code': type.code,
                        'number_of_hours': line.nb_heure,
                        'name': type.name,
                    }
                    res.append(dic)
        return res

