# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    partner_id_credit_limit = fields.Float(
        compute='_compute_partner_id_credit_limit',
        store=False,
        string='Credit granted'
    )

    @api.multi
    @api.depends('partner_id')
    def _compute_partner_id_credit_limit(self):
        for item in self:
            if item.partner_id:
                item.partner_id_credit_limit = item.partner_id.credit_limit
