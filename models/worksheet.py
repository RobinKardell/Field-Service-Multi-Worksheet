from odoo import models, fields

class FieldServiceWorksheet(models.Model):
    _name = 'field.service.worksheet'
    _description = 'Field Service Worksheet'

    service_id = fields.Many2one('field.service', string="Service Record", required=True)
    name = fields.Char(string="Worksheet Name", required=True)
    details = fields.Text(string="Worksheet Details")
    signature = fields.Binary(string="Signature")
    date = fields.Datetime(string="Date", default=fields.Datetime.now)

class FieldService(models.Model):
    _inherit = 'field.service'

    worksheet_ids = fields.One2many('field.service.worksheet', 'service_id', string="Worksheets")
